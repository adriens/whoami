---
name: whoami
url: https://github.com/adriens/whoami
description: "Mon CV et profil en données structurées — knowledge graph personnel pour agents, embeddings et graph data science"
language: Astro
topics: [curriculum, curriculum-vitae, resume, resume-website]
stars: 0
created_at: 2026-05-22
updated_at: 2026-05-24
archived: false
has_readme: true
---

# whoami

[![JSON Resume](https://img.shields.io/badge/JSON%20Resume-schema-5A0FC8?logo=json&logoColor=white)](https://jsonresume.org/schema)
[![JSON Resume Registry](https://img.shields.io/badge/Registry-adriens-5A0FC8?logo=json&logoColor=white)](https://registry.jsonresume.org/adriens)
[![Validate](https://github.com/adriens/whoami/actions/workflows/validate.yml/badge.svg)](https://github.com/adriens/whoami/actions/workflows/validate.yml)
[![Monthly fetch](https://github.com/adriens/whoami/actions/workflows/fetch-all.yml/badge.svg)](https://github.com/adriens/whoami/actions/workflows/fetch-all.yml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Bun](https://img.shields.io/badge/Bun-black?logo=bun&logoColor=white)](https://bun.sh)
[![Task](https://img.shields.io/badge/Task-taskfile.dev-29BEB0?logo=task&logoColor=white)](https://taskfile.dev)
[![Astro](https://img.shields.io/badge/Astro-site-FF5D01?logo=astro&logoColor=white)](https://astro.build)

Mon CV et profil en données structurées — knowledge graph personnel pour agents, embeddings et graph data science.

## Sources de données

| Source | Contenu | Fréquence |
|---|---|---|
| `manual/resume.json` | CV au format JSON Resume | Manuel |
| `data/dev_to/adriens/` | 206 articles DEV.to @adriens | Mensuel (CI) |
| `data/dev_to/opt-nc/` | Articles DEV.to @opt-nc écrits par adriens | Mensuel (CI) |
| `data/youtube/devops-lab/` | 284 vidéos YouTube @devopslabs2812 | Mensuel (CI) |
| `data/goodreads/` | 43 livres lus (Goodreads) | Mensuel (CI) |

## Quickstart

```sh
# Validation du CV
task validate

# Fetch toutes les sources + knowledge base
task fetch-all

# Prévisualiser le CV dans le navigateur
task serve

# Générer le knowledge base pour NotebookLM
task build-knowledge-base        # full (844 Ko)
task build-knowledge-base-lite   # frontmatters uniquement

# Exports
task export-html

# Nettoyage
task clean
```

## Structure

```
manual/resume.json                    # Le CV (seul fichier à éditer manuellement)
data/
  dev_to/{user}/articles/*.md         # Articles DEV.to (frontmatter + contenu)
  dev_to/{user}/_index.csv            # Index avec is_dev_challenge
  youtube/{channel}/videos/*.md       # Vidéos YouTube
  youtube/{channel}/_index.csv        # Index avec vues, durée
  goodreads/{id}/books/*.md           # Livres + reviews
  goodreads/{id}/_index.csv           # Index avec rating
output/
  knowledge-base.md                   # Agrégat pour NotebookLM
scripts/
  validate-json-resume.py
  fetch-devto-articles.py             # --user, --author
  fetch-youtube-channel.py            # --channel
  fetch-goodreads.py                  # --user
  build-knowledge-base.py             # --lite
.github/workflows/
  validate.yml                        # CI validation JSON Resume
  fetch-all.yml                       # Cron mensuel fetch + commit
```