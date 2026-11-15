---
name: hermes-eol-plugin
url: https://github.com/adriens/hermes-eol-plugin
description: "End-of-life checks for Hermes Agent: live support and EOL dates from endoflife.date, geol stack files, purl/CPE input"
language: Python
topics: [devops, endoflife, eol, geol, hermes-agent, hermes-plugin, purl, sbom]
stars: 0
created_at: 2026-11-13
updated_at: 2026-11-13
archived: false
has_readme: true
---

# eol — end-of-life checks for Hermes Agent

Ask Hermes *"is Python 3.9 still supported?"* and it answers from training data
that may be a year old. This plugin gives the agent live lifecycle data from
[endoflife.date](https://endoflife.date) — 480+ products: languages, operating
systems, databases, frameworks, cloud services — so support dates come from the
source, not from memory.

Written by a contributor to [geol](https://github.com/opt-nc/geol), the endoflife.date CLI.
This plugin calls the endoflife.date API directly: no binary to install, stdlib
only, no API key. It reads and writes geol's `.geol.yaml` stack files, so what
the agent inventories can be enforced in CI with `geol check --strict`.

## Tools

| Tool | What it does |
|---|---|
| `eol_search` | Find a product's identifier from a name, alias, category or tag (`postgres` → `postgresql`, `k8s` → `kubernetes`), or list every category / tag. |
| `eol_product` | All release cycles of a product: release date, LTS, end of active support, end of life, latest patch — plus its package identifiers (purl, CPE). |
| `eol_check` | Check one or many components: status (`supported`, `security-only`, `eol`, `unknown`), days until EOL, newer patch available, upgrade target (next LTS for an LTS line) and the list of cycles still maintained. Components can be given as product + version, **purl** (`pkg:pypi/django@4.2.11`) or **CPE**, and checked **at any date** (`date: 2027-06-01`). |
| `eol_stack_check` | Check a geol `.geol.yaml` with the same rules as `geol check --strict`: OK / WARN / EOL per component, `skip`, `manual_eol`, `lts_strategy` (`any` / `latest`), `lts_grace_days`, `always-latest`. |
| `eol_stack_file` | Generate a `.geol.yaml` from the components the agent found in a project (Dockerfile, `.nvmrc`, `pyproject.toml`, CI images, SBOM…). Products are resolved to their endoflife.date id, versions to the release cycle geol expects, unknown products are kept with `skip: true`. The tool returns the text; the agent saves it with Hermes' own `write_file`, under the usual approvals. |

### Context hint

Hermes keeps plugin tools behind its tool search, where the model only sees a
one-line summary of each, so a model asked *"should we upgrade?"* tends to
answer from memory. When a message is about versions, upgrades, end of life,
CVEs or files that pin versions (Dockerfile, `docker-compose.yml`, `.nvmrc`,
`requirements.txt`, `.geol.yaml`, SBOMs…), a `pre_llm_call` hook appends one
fixed note to that turn pointing the model at the `eol_*` tools. The match is a
local keyword regex; nothing is sent anywhere. Turn it off with:

```bash
hermes config set plugins.entries.eol.settings.context_hint false
```

Things to try:

```
Which Node.js versions are still supported?
Is Ubuntu 22.04 still getting security updates? Until when?
Our stack is Python 3.9.7, PostgreSQL 13, Kubernetes 1.30 — what needs upgrading first?
What in this stack will be end-of-life by June 2027?
Inventory the runtimes and base images of this repo and write a .geol.yaml for it.
Check our .geol.yaml and tell me what blocks the release.
Here is our CycloneDX SBOM: which components are end-of-life?
```

## Install

```bash
hermes plugins install https://github.com/adriens/hermes-eol-plugin
hermes plugins enable eol
```

Or for development:

```bash
git clone https://github.com/adriens/hermes-eol-plugin ~/.hermes/plugins/eol
hermes plugins enable eol
hermes plugins doctor ~/.hermes/plugins/eol --ci
```

## Works well with

The Hermes catalog has plugins that answer *"is this vulnerable?"*; this one
answers *"is this version still supported by its vendor?"*. A version can be
patched today and unsupported tomorrow, and an EOL version stops receiving the
fixes those scanners look for — the two questions complement each other.
Package URLs (purl) are the shared vocabulary: components listed in an SBOM
produced by one of these can be passed straight to `eol_check`.

| Plugin | What it adds next to `eol` |
|---|---|
| [Patch Sentinel](https://github.com/thebangarang/Patch-Sentinel) (`patch-sentinel`) | "Are we patched?" for the host: OS packages, kernel, containers and 9 language ecosystems against vendor advisories and OSV, plus a CycloneDX SBOM (`cve_sbom`) whose purls `eol_check` accepts. |
| [warden](https://gitlab.com/Zaygalx1/warden) | Defensive security operations with scoped vulnerability assessment (Grype and Trivy over one Syft SBOM). |
| [Snyk](https://github.com/NousResearch/hermes-official-plugins) (`snyk`, official) | Snyk scans of code, dependencies, container images, IaC and SBOMs. |
| [OSV references](https://github.com/EloquentBrush0x/hermes-context-refs) (`osv-ref`) | `@cve:`, `@ghsa:`, `@osv:` references that attach an OSV.dev vulnerability record, with affected and fixed versions, to a message. |
| [hermes-security-audit](https://github.com/dafka007/hermes-security-audit) | Approval-gated local audit with Gitleaks, OSV-Scanner and Semgrep CE. |
| [Compound Security](https://github.com/offense-research/compound-security-plugin) (`compound-security`) | Skills for security audit, dependency inspection, remediation and verification. |
| [Security](https://github.com/NousResearch/hermes-official-plugins) (`hermes-security`, official) | Threat-model-driven security review of a repository. |

### Combinations worth trying

Scenarios to test `eol` together with other catalog plugins. The osv-ref and
patch-sentinel ones were run end to end (see the catalog PR); the others are
suggestions.

| With | Try asking | What each plugin contributes |
|---|---|---|
| `osv-ref` | `@ghsa:<id>` *Are we affected? Which version should we move to, and must the rest of the stack move with it?* | osv-ref: the advisory and its fixed versions. eol: whether the affected branch will ever get a fix, and the status of every other component. |
| `patch-sentinel` | *Audit this machine: is it patched, and is what it runs still supported?* | Patch Sentinel: missing patches on the host and a CycloneDX SBOM. eol: support and end-of-life dates for the OS release and the components in that SBOM (by purl). |
| [`kubernetes`](https://github.com/TakeshiTGAL/hermes-plugin-kubernetes) | *Which images running in namespace X are end-of-life?* | kubernetes: the images and versions actually running in the pods. eol: their status, plus the cluster version itself. |
| [`terraform-drift`](https://github.com/TakeshiTGAL/hermes-plugin-terraform-drift) | *What is outdated or end-of-life in this infrastructure?* | terraform-drift: providers and modules behind the registry. eol: the managed services and engines they deploy (`amazon-rds-postgresql`, `amazon-eks`, `azure-kubernetes-service`, …). |
| [`cooldown`](https://github.com/Savage27z/cooldown) | *Upgrade this project off its end-of-life versions.* | eol: the target versions. cooldown: checks each package install for malicious or too-recent releases before it runs. |
| [`ci-red-to-green`](https://github.com/kinnuworks/ci-red-to-green) | *(after the upgrade lands)* | eol: the upgrade plan. ci-red-to-green: which tests broke in GitHub Actions and the commits since the last green run. |
| [`gh-ref`](https://github.com/EloquentBrush0x/hermes-context-refs) | `@gh:owner/repo#123` *Work on this upgrade issue.* | gh-ref: the issue as context. eol: the facts to plan the upgrade on. |
| Hermes cron (built in) | *Every Monday, run eol_stack_check on .geol.yaml and message me if anything turns WARN or EOL.* | A scheduled run turns the stack file into an early warning. |

Outside Hermes, [geol](https://github.com/opt-nc/geol) runs the same checks on
the `.geol.yaml` in CI (`geol ci-github init` generates the GitHub Actions
workflow) and exports endoflife.date to DuckDB or SQLite.

## What it does on your machine (disclosure)

- **Network:** HTTPS GET requests to `https://endoflife.date/api/v1/` only, when
  one of the tools is called. Requests carry product names (and fetch the public
  purl/CPE mapping tables) — never file contents, paths or other session data.
- **No file access:** the plugin reads and writes no files. `eol_stack_check`
  receives the YAML text from the agent; `eol_stack_file` returns text that the
  agent writes with `write_file`, through Hermes' approvals.
- **Context hint:** a `pre_llm_call` hook reads the current user message,
  matches it against a keyword list locally and, on a match, appends a fixed
  one-paragraph note to that turn. Disable it with the `context_hint` setting.
- **No credentials**, no environment variables, no shell commands,
  no background processes, no telemetry.
- Responses are cached in memory for 6 hours to stay polite to the API; nothing
  is persisted.

## Development

```bash
~/.hermes/hermes-agent/venv/bin/python -m unittest discover -s tests -v   # offline, HTTP mocked
hermes plugins validate . --install-deps                                  # what catalog CI runs
```

Stack-file tests need a YAML parser: Hermes' `hermes_yaml` (hence Hermes'
Python above) or PyYAML; with neither, they are skipped.

## Credits

Data: [endoflife.date](https://endoflife.date) (MIT), maintained by its
community. Please contribute product data there.

## License

MIT