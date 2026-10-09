"""Export du profil ESCO depuis manual/resume.json → data/esco/.

Artefact généré (ne pas éditer à la main) — resume.json reste la source de vérité
(`skills[].x-esco`, `basics.x-esco-occupations`, `work[].x-esco-occupations`).

Produit :
- _index.csv     : une ligne par lien (concept ESCO × entrée du profil), labels FR + EN
- profile.jsonld : profil schema.org (Person → knowsAbout / hasOccupation → DefinedTerm ESCO)

Les labels EN sont récupérés via l'API ESCO au moment de l'export.
"""

import csv
import json
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
RESUME = ROOT / "manual" / "resume.json"
OUT = ROOT / "data" / "esco"
API = "https://ec.europa.eu/esco/api/resource"
SCHEMES = {
    "skill": "http://data.europa.eu/esco/concept-scheme/skills",
    "occupation": "http://data.europa.eu/esco/concept-scheme/occupations",
}


def kind_of(uri: str) -> str:
    return uri.split("/")[-2]


def fetch_en(uri: str) -> str:
    resp = requests.get(f"{API}/{kind_of(uri)}", params={"uri": uri, "language": "en"}, timeout=15)
    resp.raise_for_status()
    return resp.json()["preferredLabel"]["en"]


def defined_term(uri, label_fr, label_en, extra=None):
    term = {
        "@type": "DefinedTerm",
        "@id": uri,
        "termCode": uri.split("/")[-1],
        "name": [{"@language": "fr", "@value": label_fr}, {"@language": "en", "@value": label_en}],
        "inDefinedTermSet": SCHEMES[kind_of(uri)],
    }
    term.update(extra or {})
    return term


def main():
    r = json.loads(RESUME.read_text(encoding="utf-8"))
    b = r["basics"]

    # (kind, uri, label_fr, esco_type/code, profile_entry, level, covers)
    links = []
    for s in r.get("skills", []):
        for e in s.get("x-esco", []):
            links.append(("skill", e["uri"], e["label"], e["type"], s["name"], s.get("level", ""), e.get("covers", [])))
    for o in b.get("x-esco-occupations", []):
        links.append(("occupation", o["uri"], o["label"], o["code"], "basics", "", []))
    for w in r.get("work", []):
        entry = f"{w.get('position', '')} @ {w.get('name', '')}"
        for o in w.get("x-esco-occupations", []):
            links.append(("occupation", o["uri"], o["label"], o["code"], entry, "", []))
    for v in r.get("volunteer", []):
        entry = f"volunteer: {v.get('position', '')} @ {v.get('organization', '')}"
        for o in v.get("x-esco-occupations", []):
            links.append(("occupation", o["uri"], o["label"], o["code"], entry, "", []))
    for l in r.get("languages", []):
        for e in l.get("x-esco", []):
            links.append(("skill", e["uri"], e["label"], e["type"], f"language: {l['language']}", l.get("fluency", ""), []))
    for c in r.get("certificates", []):
        for e in c.get("x-esco", []):
            links.append(("skill", e["uri"], e["label"], e["type"], f"certificate: {c['name']}", "", []))
    for it in r.get("interests", []):
        for e in it.get("x-esco", []):
            links.append(("skill", e["uri"], e["label"], e["type"], f"interest: {it['name']}", it.get("x-context", ""), []))
    for ref in r.get("references", []):
        for e in ref.get("x-esco", []):
            links.append(("skill", e["uri"], e["label"], e["type"], f"reference: {ref['name']}", ref.get("x-date", ""), []))

    uris = sorted({l[1] for l in links})
    print(f"Fetching EN labels for {len(uris)} ESCO concepts...")
    en = {u: fetch_en(u) for u in uris}

    OUT.mkdir(parents=True, exist_ok=True)
    with open(OUT / "_index.csv", "w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(["kind", "esco_id", "uri", "label_fr", "label_en", "esco_type_or_code", "profile_entry", "level", "covers"])
        for kind, uri, lab, typ, entry, level, covers in links:
            wr.writerow([kind, uri.split("/")[-1], uri, lab, en[uri], typ, entry, level, " | ".join(covers)])

    # JSON-LD : un DefinedTerm par concept unique, rattaché aux skills groupes du profil
    skill_terms = {}
    for kind, uri, lab, typ, entry, level, _ in links:
        if kind == "skill":
            t = skill_terms.setdefault(uri, defined_term(uri, lab, en[uri], {"x-esco-type": typ, "x-profile-skills": []}))
            t["x-profile-skills"].append(entry)

    def occupation(o, extra=None):
        occ = {
            "@type": "Occupation",
            "name": o["label"],
            "occupationalCategory": defined_term(o["uri"], o["label"], en[o["uri"]], {"x-isco-code": o["code"]}),
        }
        occ.update(extra or {})
        return occ

    occupations = [occupation(o) for o in b.get("x-esco-occupations", [])]
    for v in r.get("volunteer", []):
        for o in v.get("x-esco-occupations", []):
            occupations.append(occupation(o, {
                "x-position": v.get("position", ""),
                "x-organization": v.get("organization", ""),
                "x-volunteer": True,
            }))
    for w in r.get("work", []):
        for o in w.get("x-esco-occupations", []):
            occupations.append(occupation(o, {
                "x-position": w.get("position", ""),
                "x-employer": w.get("name", ""),
                "x-startDate": w.get("startDate", ""),
                "x-endDate": w.get("endDate", ""),
            }))

    profile = {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": b.get("url", "https://adriens.github.io/whoami/"),
        "name": b["name"],
        "jobTitle": b.get("label", ""),
        "url": b.get("url", ""),
        "x-esco-retrieved": r.get("meta", {}).get("x-esco-retrieved", ""),
        "x-source": r.get("meta", {}).get("canonical", ""),
        "x-resume-version": r.get("meta", {}).get("version", ""),
        "hasOccupation": occupations,
        "knowsAbout": list(skill_terms.values()),
        "knowsLanguage": [
            {"@type": "Language", "name": l["language"], "x-fluency": l.get("fluency", ""),
             "x-esco": [defined_term(e["uri"], e["label"], en[e["uri"]]) for e in l.get("x-esco", [])]}
            for l in r.get("languages", [])
        ],
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential", "name": c["name"],
             "recognizedBy": {"@type": "Organization", "name": c.get("issuer", "")},
             "about": [defined_term(e["uri"], e["label"], en[e["uri"]]) for e in c.get("x-esco", [])]}
            for c in r.get("certificates", [])
        ],
        "x-endorsements": [
            {"author": ref["name"], "date": ref.get("x-date", ""), "source": ref.get("x-source", ""),
             "attests": [e["uri"] for e in ref.get("x-esco", [])]}
            for ref in r.get("references", []) if ref.get("x-esco")
        ],
    }
    (OUT / "profile.jsonld").write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    n_occ = len({l[1] for l in links if l[0] == "occupation"})
    print(f"✓ {len(links)} links, {len(skill_terms)} skills + {n_occ} occupations → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
