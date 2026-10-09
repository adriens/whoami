"""Export du CV au format Europass (XML « Candidate ») depuis manual/resume.json.

Artefact généré (ne pas éditer à la main) — resume.json reste la source de vérité.
Le fichier produit s'importe tel quel dans l'éditeur https://europa.eu/europass
(« Créer un CV » → importer un fichier) : expériences, formations, langues (CECRL),
compétences numériques, publications et sections libres sont pré-remplies.

Format : HR-XML 3 « Candidate » + extensions Europass/EURES, documenté (non
officiellement) par https://github.com/J0ker98/europass-cv (CC BY 4.0) ; schéma
copié dans data/europass/schema/ et vérifié par xmllint.

Les URIs ESCO ne sont pas portées par ce format : les concepts sont repris en
texte (libellés FR exacts) dans une section libre « Référentiel ESCO ».

Usage :
    uv run scripts/export-europass.py
"""

import html
import json
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESUME = ROOT / "manual" / "resume.json"
OUT = ROOT / "data" / "europass" / "adriens" / "europass-cv.xml"
XSD = ROOT / "data" / "europass" / "schema" / "europass-candidate.xsd"

NS = {
    "": "http://www.europass.eu/1.0",
    "hr": "http://www.hr-xml.org/3",
    "oa": "http://www.openapplications.org/oagis/9",
    "eures": "http://www.europass_eures.eu/1.0",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
}
for prefix, uri in NS.items():
    ET.register_namespace(prefix, uri)

# Codifications Europass
SOCIAL = {"linkedin": "linkedin", "youtube": "youtube", "x (twitter)": "twitter", "twitter": "twitter"}
LANG_ISO = {"Français": "fra", "Anglais": "eng", "Allemand": "deu", "Espagnol": "spa"}
# Premier mot de `fluency` → niveau CECRL (identique sur les 5 dimensions)
CEFR = {"Professionnel": "C1", "Courant": "C1", "Intermédiaire": "B1", "Notions": "A1"}
CEF_DIMENSIONS = [
    "CEF-Understanding-Listening", "CEF-Understanding-Reading",
    "CEF-Speaking-Interaction", "CEF-Speaking-Production", "CEF-Writing-Production",
]
# studyType → niveau EQF (premier motif trouvé)
EQF = [("Mastère", 7), ("DEA", 7), ("Master", 7), ("Maîtrise", 6), ("Licence", 6), ("DEUG", 5), ("primaire", 1)]
# Groupes de skills non numériques → section libre plutôt que « Compétences numériques »
SOFT_SKILLS = {
    "Developer Relations & Communication", "Management & Leadership", "Pédagogie & Transmission",
    "Créativité & Apprentissage autodidacte", "Savoir-être validé par les pairs",
}
SECTIONS = ["work-experience", "education-training", "language", "profile-skills", "publication"]


def q(tag: str) -> str:
    prefix, _, local = tag.rpartition(":")
    return f"{{{NS[prefix]}}}{local}"


def sub(parent, tag, text=None, **attrs):
    el = ET.SubElement(parent, q(tag), attrs)
    if text is not None:
        el.text = str(text)
    return el


def rich(*paragraphs, items=()):
    """HTML (stocké échappé par ElementTree) : paragraphes + liste à puces."""
    out = "".join(f"<p>{html.escape(p)}</p>" for p in paragraphs if p)
    if items:
        out += "<ul>" + "".join(f"<li>{html.escape(i)}</li>" for i in items) + "</ul>"
    return out


def date(parent, tag, value):
    if value:
        sub(sub(parent, tag), "hr:FormattedDateTime", value)


def person_name(parent, basics):
    given, _, family = basics["name"].partition(" ")
    pn = sub(parent, "PersonName")
    sub(pn, "oa:GivenName", given)
    sub(pn, "hr:FamilyName", family)


def other(profile, section, title, description="", start=None, end=None, links=()):
    """Section libre : un `Others` par entrée (l'importeur ne garde que le dernier `Other`)."""
    others = sub(profile, "Others")
    sub(others, "Title", section)
    entry = sub(others, "Other")
    sub(entry, "Title", title)
    if start or end:
        d = sub(entry, "Date")
        date(d, "StartDate", start)
        date(d, "EndDate", end)
    if description:
        sub(entry, "Description", description)
    for link in links:
        if link:
            sub(entry, "Link", link)


def candidate_person(root, b):
    p = sub(root, "CandidatePerson")
    person_name(p, b)
    c = sub(p, "Communication")
    sub(c, "ChannelCode", "Email")
    sub(c, "oa:URI", b["email"])
    m = re.match(r"\+(\d+)\s+(.+)", b.get("phone", ""))
    if m:
        c = sub(p, "Communication")
        sub(c, "ChannelCode", "Telephone")
        sub(c, "UseCode", "mobile")
        sub(c, "CountryDialing", m[1])
        sub(c, "oa:DialNumber", re.sub(r"\D", "", m[2]))
        sub(c, "CountryCode", b["location"]["countryCode"].lower())
    c = sub(p, "Communication")
    sub(c, "ChannelCode", "Web")
    sub(c, "oa:URI", b["url"])
    for prof in b.get("profiles", []):
        if not prof.get("url"):
            continue
        c = sub(p, "Communication")
        media = SOCIAL.get(prof["network"].lower())
        sub(c, "ChannelCode", "Social Media" if media else "Web")
        if media:
            sub(c, "UseCode", media)
        sub(c, "oa:URI", prof["url"])
    loc = b.get("location", {})
    c = sub(p, "Communication")
    sub(c, "UseCode", "home")
    a = sub(c, "Address", type="home")
    sub(a, "oa:CityName", loc.get("city", ""))
    sub(a, "CountryCode", loc.get("countryCode", "").lower())
    sub(a, "oa:PostalCode", loc.get("postalCode", ""))
    return p


def main():
    r = json.loads(RESUME.read_text(encoding="utf-8"))
    b = r["basics"]
    country = b["location"]["countryCode"].lower()
    doc_id = f"whoami-{r.get('meta', {}).get('version', 'dev')}"

    root = ET.Element(q("Candidate"), {q("xsi:schemaLocation"): "http://www.europass.eu/1.0 Candidate.xsd"})
    sub(root, "hr:DocumentID", schemeID=doc_id, schemeName="DocumentIdentifier",
        schemeAgencyName="EUROPASS", schemeVersionID="4.0")

    supplier = sub(root, "CandidateSupplier")
    sub(supplier, "hr:PartyID", schemeID=doc_id, schemeName="PartyID", schemeAgencyName="EUROPASS", schemeVersionID="1.0")
    sub(supplier, "hr:PartyName", "Owner")
    contact = sub(supplier, "PersonContact")
    person_name(contact, b)
    c = sub(contact, "Communication")
    sub(c, "ChannelCode", "Email")
    sub(c, "oa:URI", b["email"])
    sub(supplier, "hr:PrecedenceCode", 1)

    person = candidate_person(root, b)
    warnings = []
    for lang in r.get("languages", []):
        if lang.get("fluency", "").startswith("Natif"):
            sub(person, "PrimaryLanguageCode", LANG_ISO.get(lang["language"], lang["language"]),
                name="NORMAL" if lang["language"] in LANG_ISO else "FREE_TEXT")

    profile = sub(root, "CandidateProfile", languageCode="fr")
    sub(profile, "hr:ExecutiveSummary", rich(*[p for p in b.get("summary", "").split("\n\n")]))

    # Expériences
    hist = sub(profile, "EmploymentHistory")
    for w in r.get("work", []):
        eh = sub(hist, "EmployerHistory")
        sub(eh, "hr:OrganizationName", w["name"])
        if w.get("url"):
            sub(eh, "Link", w["url"])
        ph = sub(eh, "PositionHistory")
        sub(ph, "PositionTitle", w["position"], typeCode="FREETEXT")
        period = sub(ph, "eures:EmploymentPeriod")
        date(period, "eures:StartDate", w.get("startDate"))
        date(period, "eures:EndDate", w.get("endDate"))
        sub(period, "hr:CurrentIndicator", "false" if w.get("endDate") else "true")
        sub(ph, "oa:Description", rich(w.get("summary", ""), items=w.get("highlights", [])))

    # Formations
    edu = sub(profile, "EducationHistory")
    for e in r.get("education", []):
        att = sub(edu, "EducationOrganizationAttendance")
        sub(att, "hr:OrganizationName", e["institution"])
        if e.get("url"):
            sub(att, "Link", e["url"])
        period = sub(att, "AttendancePeriod")
        date(period, "StartDate", e.get("startDate"))
        date(period, "EndDate", e.get("endDate"))
        sub(period, "Ongoing", "false" if e.get("endDate") else "true")
        deg = sub(att, "EducationDegree")
        sub(deg, "hr:DegreeName", f"{e.get('studyType', '')} — {e.get('area', '')}".strip(" —"))
        if e.get("courses"):
            sub(deg, "OccupationalSkillsCovered", rich(items=e["courses"]))
        level = next((lvl for pat, lvl in EQF if pat in e.get("studyType", "")), None)
        if level:
            sub(att, "EducationLevelCode", level)
        else:
            warnings.append(f"education « {e.get('studyType')} » : niveau EQF inconnu")

    sub(profile, "Certifications")

    # Publications
    pubs = sub(profile, "PublicationHistory")
    for p in r.get("publications", []):
        pub = sub(pubs, "Publication")
        sub(pub, "Title", p["name"])
        if p.get("releaseDate"):
            sub(pub, "Year", p["releaseDate"][:4])
        if p.get("publisher"):
            sub(pub, "Publisher", p["publisher"])
        if p.get("url"):
            sub(sub(pub, "DOI"), "Link", p["url"])
        if p.get("summary"):
            sub(pub, "hr:FormattedPublicationDescription", rich(p["summary"]))

    # Langues étrangères (CECRL)
    quals = sub(profile, "PersonQualifications")
    for lang in r.get("languages", []):
        fluency = lang.get("fluency", "")
        if fluency.startswith("Natif"):
            continue
        level = CEFR.get(fluency.split()[0].strip("—,") if fluency else "")
        if not level:
            warnings.append(f"langue « {lang['language']} » : niveau CECRL inconnu pour {fluency!r}")
            continue
        pc = sub(quals, "PersonCompetency")
        iso = LANG_ISO.get(lang["language"])
        sub(pc, "CompetencyID", iso or lang["language"], schemeName="NORMAL" if iso else "FREE_TEXT")
        sub(pc, "hr:TaxonomyID", "language")
        for dim in CEF_DIMENSIONS:
            d = sub(pc, "eures:CompetencyDimension")
            sub(d, "hr:CompetencyDimensionTypeCode", dim)
            sub(sub(d, "eures:Score"), "hr:ScoreText", level)

    # Compétences numériques : un groupe par skill technique, keywords dédoublonnés (≤ 99 car.)
    skills = sub(profile, "Skills")
    seen = set()
    for s in r.get("skills", []):
        if s["name"] in SOFT_SKILLS:
            continue
        group = sub(skills, "SkillsGroup")
        sub(group, "Title", f"{s['name']} ({s['level']})" if s.get("level") else s["name"])
        for k in s.get("keywords", []):
            k = k[:99]
            if k.lower() in seen:
                continue
            seen.add(k.lower())
            pc = sub(group, "PersonCompetency")
            sub(pc, "hr:TaxonomyID", "Digital_Skill")
            sub(pc, "hr:CompetencyName", k)

    # Sections libres
    for s in r.get("skills", []):
        if s["name"] in SOFT_SKILLS:
            other(profile, "Compétences transversales", f"{s['name']} ({s.get('level', '')})".replace(" ()", ""),
                  rich(", ".join(s.get("keywords", []))))
    for c in r.get("certificates", []):
        other(profile, "Certifications", f"{c['name']} — {c.get('issuer', '')}", rich(c.get("summary", "")),
              start=c.get("date"), links=[c.get("url")])
    for v in r.get("volunteer", []):
        other(profile, "Bénévolat", f"{v['position']} — {v['organization']}",
              rich(v.get("summary", ""), items=v.get("highlights", [])),
              start=v.get("startDate"), end=v.get("endDate"), links=[v.get("url")])
    for a in sorted(r.get("awards", []), key=lambda a: a.get("date", ""), reverse=True):
        other(profile, "Distinctions & interventions", a["title"],
              rich(a.get("awarder", ""), a.get("summary", "")), start=a.get("date"), links=[a.get("url")])
    for p in r.get("projects", []):
        other(profile, "Projets", p["name"], rich(p.get("description", ""), items=p.get("highlights", [])),
              start=p.get("startDate"), end=p.get("endDate"), links=[p.get("url")])
    for i in r.get("interests", []):
        if i.get("x-context") in ("pro", "mixed"):
            other(profile, "Centres d'intérêt", i["name"], rich(", ".join(i.get("keywords", []))))

    # Référentiel ESCO (texte : le format ne porte pas les URIs)
    occs = b.get("x-esco-occupations", [])
    if occs:
        other(profile, "Référentiel ESCO", "Métiers ESCO",
              rich(items=[f"{o['label']} (ISCO {o['code']})" for o in occs]))
    for s in r.get("skills", []):
        if s.get("x-esco"):
            other(profile, "Référentiel ESCO", s["name"], rich(items=[e["label"] for e in s["x-esco"]]))

    design = sub(sub(root, "RenderingInformation"), "Design")
    for tag, value in (("Template", "Template1"), ("Color", "Default"), ("FontSize", "Medium"),
                       ("Logo", "FirstPage"), ("PageNumbers", "true")):
        sub(design, tag, value)
    order = sub(design, "SectionsOrder")
    for s in SECTIONS:
        sub(sub(order, "Section"), "Title", s)

    ET.indent(root, space="  ")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    xml = ET.tostring(root, encoding="unicode")
    OUT.write_text('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' + xml + "\n", encoding="utf-8")

    for w in warnings:
        print(f"  ⚠ {w}")
    print(f"✓ {OUT.relative_to(ROOT)} — {len(r.get('work', []))} postes, {len(r.get('education', []))} formations, "
          f"{len(seen)} compétences numériques")

    if shutil.which("xmllint"):
        res = subprocess.run(["xmllint", "--noout", "--schema", str(XSD), str(OUT)], capture_output=True, text=True)
        if res.returncode:
            print(res.stderr, file=sys.stderr)
            sys.exit(1)
        print("✓ conforme au schéma Europass Candidate (xmllint)")
    else:
        print("⚠ xmllint absent : validation XSD non faite")


if __name__ == "__main__":
    main()
