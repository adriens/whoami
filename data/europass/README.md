# Europass — CV généré depuis resume.json

[Europass](https://europa.eu/europass/fr) est la plateforme gratuite de la Commission européenne pour le profil et le CV ; ses sélecteurs de compétences et de métiers sont [ESCO](../esco/README.md).

## Fichier généré — `europass-cv.xml`

**Ne pas éditer à la main** — régénérer avec `task export-europass` (validé contre le schéma par `xmllint`).

Format : document **Europass Candidate** (HR-XML 3 + extensions Europass/EURES), celui que l'éditeur Europass importe et exporte depuis 2020 (l'ancien XML « SkillsPassport » v3 est refusé).

| Section Europass | Source `resume.json` |
|---|---|
| Informations personnelles | `basics` (nom, e-mail, téléphone, site, profils sociaux, adresse) ; langue maternelle = `x-cefr: "native"` |
| À propos | `basics.label` en gras + `basics.summary` |
| Expérience professionnelle | `work[]` (summary + highlights, `x-location`, secteur `x-nace`) |
| Éducation et formation | `education[]` (`x-location`, niveau `x-eqf`) |
| Compétences linguistiques | `languages[]` : code `x-iso639`, niveaux CECRL par dimension `x-cefr` |
| Compétences numériques | `skills[]` en `x-europass: digital` : un groupe par skill, keywords dédoublonnés |
| Publications | `publications[]` : auteurs (`x-authors`, sinon JSON-LD Zenodo, sinon `basics.name`), DOI joint depuis `data/zenodo/` par URL, lien en référence sinon |
| Sections libres | Compétences transversales (`x-europass: transversal`), Recommandations (`references[]` en `x-featured`, texte intégral), Certifications, Bénévolat, Distinctions & interventions, Projets, Centres d'intérêt (`pro`/`mixed`), Référentiel ESCO |

**ESCO** : le format ne porte pas d'URI. Les concepts sont repris en texte (libellés FR exacts) dans la section libre « Référentiel ESCO » ; pour des compétences *reliées* à ESCO dans le profil Europass, les re-sélectionner dans l'éditeur à partir de ces libellés (ou de `data/esco/_index.csv`).

## Import

1. Se connecter sur https://europa.eu/europass (EU Login)
2. Mon Europass → Créer un CV (ou le profil) **en français** → **importer** `europass-cv.xml` (le XML est en français, `languageCode="fr"` ; pas de version anglaise pour l'instant)
3. Relire, ajuster la mise en page, exporter en PDF (le PDF embarque le XML : réimportable)

## Schéma — `schema/`

XSD **non officielle** (la Commission ne publie pas ce format), reconstruite à partir d'exports réels et du comportement de l'importeur : [J0ker98/europass-cv](https://github.com/J0ker98/europass-cv) (commit `2478b34`), licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Point d'entrée : `europass-candidate.xsd`.
