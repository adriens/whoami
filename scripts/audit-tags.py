"""Audit de la taxonomie x-tags canonique.

Compare les tags utilisés dans le repo à la taxonomie canonique définie dans
CLAUDE.md (section « Taxonomie x-tags canonique »).

Deux niveaux de sévérité :
- ERREUR (exit 1) : tag hors-taxonomie dans manual/resume.json (le vocabulaire
  est fermé — c'est l'épine dorsale du filtrage cross-section), ou doublon
  dans la liste canonique elle-même.
- WARNING (exit 0) : tag hors-taxonomie dans les sources data/ (linkedin,
  youtube, goodreads, stagiaires) — enrichissement thématique toléré mais
  visible, et quasi-doublons dans la taxonomie (distance d'édition ≤ 2).

Hors périmètre : data/iot (vocabulaire matériel dédié), tags de plateformes
(huggingface, dockerhub…).
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CLAUDE_MD = ROOT / "CLAUDE.md"
RESUME = ROOT / "manual" / "resume.json"

# Sources data/ scannées en mode warning : (label, glob)
DATA_SOURCES = [
    ("linkedin/recommendations", "data/linkedin/adrien-sales/recommendations/*.md"),
    ("linkedin/recommendations-given", "data/linkedin/adrien-sales/recommendations-given/*.md"),
    ("youtube/videos", "data/youtube/devops-lab/videos/*.md"),
    ("goodreads/books", "data/goodreads/*/books/*.md"),
    ("stagiaires", "data/stagiaires/adriens/stagiaires/*.md"),
]

# Paires documentées comme distinctes :
# - pedagogy (Domaine) vs pedagogie (soft skill refs)
# - mentor (Rôle) vs mentorat (soft skill refs)
DOCUMENTED_PAIRS = {
    frozenset({"pedagogy", "pedagogie"}),
    frozenset({"mentor", "mentorat"}),
}


def parse_taxonomy(text: str) -> tuple[list[str], list[str]]:
    """Extrait les tags backtickés des bullets de la section taxonomie.

    Retourne (tags uniques ordonnés, doublons détectés dans la liste).
    """
    m = re.search(
        r"^## Taxonomie `x-tags` canonique\n(.*?)(?=^## )", text, re.M | re.S
    )
    if not m:
        sys.exit("ERREUR : section « Taxonomie x-tags canonique » introuvable dans CLAUDE.md")
    tags, dups, seen = [], [], set()
    for line in m.group(1).splitlines():
        if not line.startswith("- **"):
            continue
        # ignorer les exemples dans les parenthèses italiques *(…)*
        line = re.sub(r"\*\(.*?\)\*", "", line)
        for tag in re.findall(r"`([^`]+)`", line):
            if tag in seen:
                dups.append(tag)
            else:
                seen.add(tag)
                tags.append(tag)
    return tags, dups


def resume_tags() -> Counter:
    counts: Counter = Counter()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "x-tags" and isinstance(value, list):
                    counts.update(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(json.loads(RESUME.read_text(encoding="utf-8")))
    return counts


def frontmatter_tags(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return []
    parts = text.split("---", 2)
    if len(parts) < 3:
        return []
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return []
    tags = fm.get("tags")
    return [str(t) for t in tags] if isinstance(tags, list) else []


def edit_distance(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def main() -> int:
    canonical, taxonomy_dups = parse_taxonomy(CLAUDE_MD.read_text(encoding="utf-8"))
    canon_set = set(canonical)
    errors, warnings = [], []

    # 1. Doublons dans la liste canonique elle-même
    for dup in taxonomy_dups:
        errors.append(f"taxonomie CLAUDE.md : `{dup}` listé plusieurs fois")

    # 2. resume.json — vocabulaire fermé, strict
    used = resume_tags()
    for tag in sorted(set(used) - canon_set):
        errors.append(f"resume.json : tag hors-taxonomie `{tag}` ({used[tag]}x)")

    # 3. Sources data/ — warning
    for label, pattern in DATA_SOURCES:
        source_counts: Counter = Counter()
        for path in sorted(ROOT.glob(pattern)):
            for tag in frontmatter_tags(path):
                if tag not in canon_set:
                    source_counts[tag] += 1
        for tag, n in source_counts.most_common():
            warnings.append(f"{label} : tag hors-taxonomie `{tag}` ({n}x)")

    # 4. Quasi-doublons dans la taxonomie (hors paires documentées)
    for i, a in enumerate(canonical):
        for b in canonical[i + 1:]:
            if frozenset({a, b}) in DOCUMENTED_PAIRS:
                continue
            if edit_distance(a, b) <= 2 and min(len(a), len(b)) > 4:
                warnings.append(f"taxonomie : quasi-doublons `{a}` / `{b}`")

    # 5. Tags canoniques jamais utilisés dans resume.json (info)
    unused = sorted(canon_set - set(used))

    print(f"Taxonomie canonique : {len(canonical)} tags")
    print(f"resume.json : {len(used)} tags distincts, {sum(used.values())} occurrences")
    if unused:
        print(f"Canoniques non utilisés dans resume.json : {', '.join(unused)}")
    print()
    for w in warnings:
        print(f"  WARN  {w}")
    for e in errors:
        print(f"  ERROR {e}")
    print()
    if errors:
        print(f"✗ audit-tags : {len(errors)} erreur(s), {len(warnings)} warning(s)")
        return 1
    print(f"✓ audit-tags : OK ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
