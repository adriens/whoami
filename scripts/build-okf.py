"""Générer un bundle Open Knowledge Format (OKF v0.1) depuis manual/resume.json.

OKF (https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) :
arborescence de fichiers markdown + frontmatter YAML, reliés par des liens
markdown pour former un graphe de concepts. Champs frontmatter : type, title,
description, resource, tags, timestamp.

Ici : chaque entrée de resume.json devient un document. Les `x-tags` deviennent
des nœuds-hub `tags/<tag>.md` qui relient les sections entre elles — le graphe
de connaissances du profil, navigable sans Neo4j.

resume.json reste la seule source de vérité ; ce bundle est un artefact généré.
"""

import argparse
import re
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

OUTPUT = Path("output/okf")
RESUME = Path("manual/resume.json")

import json  # noqa: E402

RESUME_DATA = json.loads(RESUME.read_text(encoding="utf-8"))
META = RESUME_DATA.get("meta", {})
CANONICAL = META.get("canonical", "")
DEFAULT_TS = META.get("lastModified", str(date.today()))


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower())
    return text.strip("-") or "item"


# --- Record model ---------------------------------------------------------
# Un record = un document OKF. tags = tags-graphe (présents dans tags/).
class Record:
    def __init__(self, section, slug, type_, title, description, resource, tags, timestamp, body):
        self.section = section
        self.slug = slug
        self.type = type_
        self.title = title
        self.description = description
        self.resource = resource
        self.tags = tags
        self.timestamp = timestamp
        self.body = body  # liste de lignes


def truncate(text: str, n: int = 160) -> str:
    text = " ".join(text.split())
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def tag_links(tags, depth_to_root=".."):
    """Ligne markdown reliant un doc à ses nœuds-tag (depth relatif au root okf)."""
    if not tags:
        return []
    links = ", ".join(f"[{t}]({depth_to_root}/tags/{t}.md)" for t in sorted(tags))
    return ["", f"**Tags :** {links}"]


def main():
    parser = argparse.ArgumentParser(description="Générer un bundle OKF depuis resume.json")
    parser.add_argument("--with-data", action="store_true", help="(non implémenté) miroir de data/**")
    args = parser.parse_args()
    if args.with_data:
        print("Note : --with-data n'est pas encore implémenté ; génération resume-only.")

    r = RESUME_DATA
    records: list[Record] = []

    # 1re passe : sections porteuses de x-tags → univers de tags
    tag_universe: set[str] = set()

    def reg(rec: Record):
        records.append(rec)
        for t in rec.tags:
            tag_universe.add(t)

    # work
    for w in r.get("work", []):
        slug = slugify(f"{w.get('name','')}-{w.get('position','')}")
        body = [w.get("summary", "")]
        body += [f"- {h}" for h in w.get("highlights", [])]
        period = w.get("startDate", "")
        if w.get("endDate") or "startDate" in w:
            period = f"{w.get('startDate','')} → {w.get('endDate','présent')}"
        body.append("")
        body.append(f"*Période : {period}*")
        reg(Record("work", slug, "Work Experience",
                   f"{w.get('position','')} @ {w.get('name','')}",
                   truncate(w.get("summary", "")),
                   w.get("url", CANONICAL), w.get("x-tags", []),
                   w.get("startDate", DEFAULT_TS), body))

    # projects
    for p in r.get("projects", []):
        slug = slugify(p.get("name", ""))
        body = [p.get("description", "")]
        body += [f"- {h}" for h in p.get("highlights", [])]
        body.append("")
        body.append(f"*Type : {p.get('type','')}*")
        reg(Record("projects", slug, "Project", p.get("name", ""),
                   truncate(p.get("description", "")),
                   p.get("url", CANONICAL), p.get("x-tags", []),
                   p.get("startDate", DEFAULT_TS), body))

    # awards
    for a in r.get("awards", []):
        slug = slugify(a.get("title", ""))
        body = [a.get("summary", ""), "", f"*Décerné par : {a.get('awarder','')}*"]
        reg(Record("awards", slug, "Award", a.get("title", ""),
                   truncate(a.get("summary", "")),
                   a.get("url", CANONICAL), a.get("x-tags", []),
                   a.get("date", DEFAULT_TS), body))

    # publications
    for p in r.get("publications", []):
        slug = slugify(p.get("name", ""))
        body = [p.get("summary", ""), "", f"*Éditeur : {p.get('publisher','')}*"]
        reg(Record("publications", slug, "Publication", p.get("name", ""),
                   truncate(p.get("summary", "")),
                   p.get("url", CANONICAL), p.get("x-tags", []),
                   p.get("releaseDate", DEFAULT_TS), body))

    # volunteer
    for v in r.get("volunteer", []):
        slug = slugify(f"{v.get('organization','')}-{v.get('position','')}")
        body = [v.get("summary", "")]
        body += [f"- {h}" for h in v.get("highlights", [])]
        reg(Record("volunteer", slug, "Volunteer",
                   f"{v.get('position','')} @ {v.get('organization','')}",
                   truncate(v.get("summary", "")),
                   v.get("url", CANONICAL), v.get("x-tags", []),
                   v.get("startDate", DEFAULT_TS), body))

    # references
    for ref in r.get("references", []):
        slug = slugify(ref.get("name", ""))
        text = ref.get("reference", "")
        body = [text, ""]
        if ref.get("x-position"):
            body.append(f"*{ref['x-position']}*")
        meta_bits = [b for b in (ref.get("x-relationship"), ref.get("x-source"), ref.get("x-date")) if b]
        if meta_bits:
            body.append(f"*{' · '.join(meta_bits)}*")
        reg(Record("references", slug, "Reference", ref.get("name", ""),
                   truncate(text),
                   ref.get("x-url", CANONICAL), ref.get("x-tags", []),
                   ref.get("x-date", DEFAULT_TS), body))

    # certificates
    for c in r.get("certificates", []):
        slug = slugify(c.get("name", ""))
        body = [f"*Émetteur : {c.get('issuer','')}*"]
        reg(Record("certificates", slug, "Certificate", c.get("name", ""),
                   f"Certificat — {c.get('issuer','')}",
                   c.get("url", CANONICAL), c.get("x-tags", []),
                   c.get("date", DEFAULT_TS), body))

    # 2e passe : skills & interests s'accrochent au graphe via name/keywords
    def matched_tags(*candidates):
        slugs = {slugify(c) for c in candidates}
        return sorted(slugs & tag_universe)

    for s in r.get("skills", []):
        slug = slugify(s.get("name", ""))
        kws = s.get("keywords", [])
        tags = matched_tags(s.get("name", ""), *kws)
        body = [f"**Niveau : {s.get('level','')}**", ""]
        if kws:
            body.append("Mots-clés : " + ", ".join(kws))
        records.append(Record("skills", slug, "Skill", s.get("name", ""),
                              f"{s.get('level','')} — {truncate(', '.join(kws), 120)}",
                              CANONICAL, tags, DEFAULT_TS, body))

    for i in r.get("interests", []):
        slug = slugify(i.get("name", ""))
        kws = i.get("keywords", [])
        tags = matched_tags(i.get("name", ""), *kws)
        body = ["Mots-clés : " + ", ".join(kws)] if kws else []
        if i.get("x-context"):
            body += ["", f"*Contexte : {i['x-context']}*"]
        records.append(Record("interests", slug, "Interest", i.get("name", ""),
                              truncate(", ".join(kws)) or i.get("name", ""),
                              CANONICAL, tags, DEFAULT_TS, body))

    # education (pas de x-tags → pas dans le graphe, mais documenté)
    for e in r.get("education", []):
        slug = slugify(f"{e.get('institution','')}-{e.get('area','')}")
        body = [f"**{e.get('studyType','')}** — {e.get('area','')} @ {e.get('institution','')}"]
        if e.get("courses"):
            body += [""] + [f"- {c}" for c in e["courses"]]
        records.append(Record("education", slug, "Education",
                              f"{e.get('studyType','')} — {e.get('area','')}",
                              f"{e.get('institution','')}",
                              e.get("url", CANONICAL), [],
                              e.get("endDate", e.get("startDate", DEFAULT_TS)), body))

    # profile (basics)
    b = r["basics"]
    prof_body = [b.get("summary", "")]
    loc = b.get("location", {})
    if loc:
        prof_body += ["", f"*Localisation : {loc.get('city','')}, {loc.get('countryCode','')}*"]
    if b.get("profiles"):
        prof_body += ["", "**Profils :**"]
        prof_body += [
            f"- [{p['network']}]({p['url']})" if p.get("url") else f"- {p['network']}: {p.get('username','')}"
            for p in b["profiles"]
        ]
    records.append(Record("profile", slugify(b["name"]), "Profile", b["name"],
                          b.get("x-summary-short", truncate(b.get("summary", ""))),
                          b.get("url", CANONICAL), [], DEFAULT_TS, prof_body))

    # --- Écriture ---------------------------------------------------------
    if OUTPUT.exists():
        import shutil
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    # uniquité des slugs par section
    seen = defaultdict(set)
    for rec in records:
        base = rec.slug
        n = 2
        while rec.slug in seen[rec.section]:
            rec.slug = f"{base}-{n}"
            n += 1
        seen[rec.section].add(rec.slug)

    tag_map: dict[str, list[Record]] = defaultdict(list)
    by_section: dict[str, list[Record]] = defaultdict(list)

    def write_doc(path: Path, meta: dict, body_lines):
        path.parent.mkdir(parents=True, exist_ok=True)
        fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
        content = "\n".join(body_lines).strip()
        path.write_text(f"---\n{fm}\n---\n\n{content}\n", encoding="utf-8")

    for rec in records:
        by_section[rec.section].append(rec)
        for t in rec.tags:
            tag_map[t].append(rec)
        meta = {
            "type": rec.type,
            "title": rec.title,
            "description": rec.description,
            "resource": rec.resource,
            "tags": rec.tags,
            "timestamp": rec.timestamp,
        }
        body = list(rec.body) + tag_links(rec.tags)
        write_doc(OUTPUT / rec.section / f"{rec.slug}.md", meta, body)

    # tags/<tag>.md — nœuds-hub du graphe
    tags_dir = OUTPUT / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)
    for tag, recs in sorted(tag_map.items()):
        body = [f"Concept transversal reliant {len(recs)} entrées du profil.", ""]
        for rec in sorted(recs, key=lambda x: (x.section, x.title)):
            body.append(f"- [{rec.title}](../{rec.section}/{rec.slug}.md) — *{rec.type}*")
        write_doc(tags_dir / f"{tag}.md", {
            "type": "Tag",
            "title": tag,
            "description": f"{len(recs)} entrées taguées « {tag} »",
            "resource": CANONICAL,
            "tags": [],
            "timestamp": DEFAULT_TS,
        }, body)

    # index.md par section
    for section, recs in by_section.items():
        body = [f"{len(recs)} entrées.", ""]
        for rec in sorted(recs, key=lambda x: x.title):
            body.append(f"- [{rec.title}]({rec.slug}.md) — {truncate(rec.description, 100)}")
        write_doc(OUTPUT / section / "index.md", {
            "type": "Index",
            "title": section.capitalize(),
            "description": f"Index de la section {section}",
            "resource": CANONICAL,
            "tags": [],
            "timestamp": DEFAULT_TS,
        }, body)

    # tags/index.md
    body = [f"{len(tag_map)} concepts transversaux (graphe de connaissances).", ""]
    for tag, recs in sorted(tag_map.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        body.append(f"- [{tag}]({tag}.md) — {len(recs)} entrées")
    write_doc(tags_dir / "index.md", {
        "type": "Index", "title": "Tags", "description": "Graphe de concepts (x-tags)",
        "resource": CANONICAL, "tags": [], "timestamp": DEFAULT_TS,
    }, body)

    # index.md racine
    body = [f"Bundle Open Knowledge Format v0.1 — profil de {b['name']}.",
            f"> {b.get('label','')}", "", b.get("x-summary-short", ""), "",
            "## Sections", ""]
    for section in sorted(by_section):
        body.append(f"- [{section.capitalize()}]({section}/index.md) — {len(by_section[section])} entrées")
    body += ["", f"- [Tags]({'tags'}/index.md) — {len(tag_map)} concepts (graphe)"]
    write_doc(OUTPUT / "index.md", {
        "type": "Index", "title": f"{b['name']} — OKF Bundle",
        "description": b.get("x-summary-short", b.get("label", "")),
        "resource": CANONICAL, "tags": [], "timestamp": DEFAULT_TS,
    }, body)

    # --- Self-check : tous les liens internes .md résolvent ---------------
    broken = 0
    total_links = 0
    link_re = re.compile(r"\]\(([^)]+\.md)\)")
    for md in OUTPUT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in link_re.finditer(text):
            target = m.group(1)
            if target.startswith("http"):
                continue
            total_links += 1
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                broken += 1
                print(f"  LIEN CASSÉ : {md.relative_to(OUTPUT)} → {target}")

    n_docs = sum(1 for _ in OUTPUT.rglob("*.md"))
    size_kb = sum(f.stat().st_size for f in OUTPUT.rglob("*.md")) // 1024
    print(f"Done. {OUTPUT}/ — {n_docs} documents, {len(tag_map)} tags, "
          f"{total_links} liens internes ({broken} cassés), {size_kb} Ko")
    if broken:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
