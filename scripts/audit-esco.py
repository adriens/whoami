"""Audit du rattachement ESCO de manual/resume.json.

Vérifie hors-ligne (pas d'appel à l'API ESCO, compatible CI) :

- ERREUR (exit 1) :
  - skill sans `x-esco` (tout skill doit être rattaché au référentiel)
  - URI mal formée (`http://data.europa.eu/esco/(skill|occupation)/<uuid>`)
  - `label` vide, `type` hors {knowledge, skill/competence}
  - `covers` qui cite un keyword absent des `keywords` du skill (mapping périmé)
  - occupation (`basics` / `work[]` / `volunteer[]`) sans `code` ISCO-ESCO
  - `languages[].x-esco` / `certificates[].x-esco` / `references[].x-esco` mal formés (URI, label, type)
- RAPPORT : couverture des keywords par groupe — chaque keyword est soit
  couvert par au moins un concept ESCO (`covers`), soit listé comme non couvert
  (typiquement une techno de niche absente d'ESCO).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESUME = ROOT / "manual" / "resume.json"

URI_RE = re.compile(r"^http://data\.europa\.eu/esco/(skill|occupation)/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
TYPES = {"knowledge", "skill/competence"}


def check_occupations(where, occs, errors):
    for o in occs:
        if not URI_RE.match(o.get("uri", "")) or "/occupation/" not in o["uri"]:
            errors.append(f"{where}: URI occupation invalide {o.get('uri')!r}")
        if not o.get("label"):
            errors.append(f"{where}: label vide pour {o.get('uri')}")
        if not o.get("code"):
            errors.append(f"{where}: code ISCO manquant pour {o.get('uri')}")


def check_skill_links(where, links, errors):
    for e in links:
        uri = e.get("uri", "")
        if not URI_RE.match(uri) or "/skill/" not in uri:
            errors.append(f"{where} : URI invalide {uri!r}")
        if not e.get("label"):
            errors.append(f"{where} : label vide pour {uri}")
        if e.get("type") not in TYPES:
            errors.append(f"{where} : type {e.get('type')!r} pour {uri}")


def main():
    r = json.loads(RESUME.read_text(encoding="utf-8"))
    errors = []
    total = covered_total = 0
    concepts = set()

    print("Couverture ESCO des skills\n")
    for s in r.get("skills", []):
        name = s.get("name", "?")
        links = s.get("x-esco", [])
        if not links:
            errors.append(f"skill « {name} » : aucun x-esco")
        kws = s.get("keywords", [])
        covered = set()
        for e in links:
            uri = e.get("uri", "")
            if not URI_RE.match(uri) or "/skill/" not in uri:
                errors.append(f"skill « {name} » : URI invalide {uri!r}")
            if not e.get("label"):
                errors.append(f"skill « {name} » : label vide pour {uri}")
            if e.get("type") not in TYPES:
                errors.append(f"skill « {name} » : type {e.get('type')!r} pour {uri}")
            for k in e.get("covers", []):
                if k not in kws:
                    errors.append(f"skill « {name} » : covers cite un keyword inconnu {k!r}")
            covered.update(e.get("covers", []))
            concepts.add(uri)
        uncovered = [k for k in kws if k not in covered]
        total += len(kws)
        covered_total += len(kws) - len(uncovered)
        print(f"  {len(kws) - len(uncovered):3d}/{len(kws):<3d} {name} ({len(links)} concepts)")
        for k in uncovered:
            print(f"          non couvert : {k}")

    check_occupations("basics", r.get("basics", {}).get("x-esco-occupations", []), errors)
    for w in r.get("work", []):
        occs = w.get("x-esco-occupations", [])
        if not occs:
            print(f"\n  ⚠ work « {w.get('name')} » : aucune occupation ESCO")
        check_occupations(f"work « {w.get('name')} »", occs, errors)
    for v in r.get("volunteer", []):
        check_occupations(f"volunteer « {v.get('organization')} »", v.get("x-esco-occupations", []), errors)
    for ref in r.get("references", []):
        check_skill_links(f"references « {ref.get('name')} »", ref.get("x-esco", []), errors)
    for section, key in (("languages", "language"), ("certificates", "name")):
        for item in r.get(section, []):
            links = item.get("x-esco", [])
            if not links:
                print(f"  ⚠ {section} « {item.get(key)} » : aucun x-esco")
            check_skill_links(f"{section} « {item.get(key)} »", links, errors)
            concepts.update(e.get("uri", "") for e in links)

    pct = covered_total / total if total else 0
    print(f"\nTotal : {covered_total}/{total} keywords couverts ({pct:.0%}), {len(concepts)} concepts ESCO uniques")
    print(f"Référentiel récupéré le : {r.get('meta', {}).get('x-esco-retrieved', '?')}")

    if errors:
        print(f"\n✗ {len(errors)} erreur(s) :")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("✓ rattachement ESCO cohérent")


if __name__ == "__main__":
    main()
