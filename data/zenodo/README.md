# Zenodo — Adrien Sales

Publications scientifiques déposées sur [Zenodo](https://zenodo.org). Alimentation **manuelle via Claude Code**. Chaque publication est un fichier JSON-LD conforme à [schema.org/ScholarlyArticle](https://schema.org/ScholarlyArticle).

```mermaid
flowchart LR
    U([URL Zenodo / DOI]) --> CC[Claude Code]
    CC --> F[(publications/*.json\n_index.csv)]
    CC -->|entrée publications[]| R[(resume.json)]
    F & R --> KB([knowledge-base.md])
```

## Schéma d'une publication

```json
{
  "@context": "https://schema.org",
  "@type": "ScholarlyArticle",
  "name": "Titre de la publication",
  "author": {
    "@type": "Person",
    "name": "Adrien Sales"
  },
  "datePublished": "YYYY-MM-DD",
  "version": "v1",
  "inLanguage": "en",
  "abstract": "Résumé de la publication.",
  "keywords": ["mot-cle-1", "mot-cle-2"],
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "url": "https://zenodo.org/records/<id>",
  "sameAs": "https://doi.org/10.5281/zenodo.<id>",
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "doi",
    "value": "10.5281/zenodo.<id>"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Zenodo"
  },
  "isBasedOn": {
    "@type": "SoftwareSourceCode",
    "codeRepository": "https://github.com/adriens/<repo>"
  }
}
```

> `isBasedOn` est optionnel — à inclure uniquement si la publication s'appuie sur un repo GitHub.

## Workflow — ajouter une publication

1. **Récupérer les métadonnées** depuis la page Zenodo (titre, DOI, date, abstract, keywords, licence, repo associé)
2. **Créer le fichier JSON-LD** dans `publications/YYYY-MM-DD-slug.json` en suivant le schéma ci-dessus
3. **Mettre à jour `_index.csv`** — colonnes : `slug, name, doi, datePublished, inLanguage, keywords, url`
4. **Ajouter l'entrée dans `resume.json`** → section `publications[]` :
   ```json
   {
     "name": "Titre",
     "publisher": "Zenodo",
     "releaseDate": "YYYY-MM-DD",
     "url": "https://zenodo.org/records/<id>",
     "summary": "Résumé court.",
     "x-tags": ["devsecops", "open-source", ...]
   }
   ```
5. **Auditer les skills** dans `resume.json` :
   - Keywords de la publication absents d'un skill existant → les ajouter
   - Outil/techno non couverts → évaluer un skill dédié
   - Une publication est un signal **en première personne**, plus direct qu'une recommandation tierce
6. **`task validate`** — toujours
7. **Bump `meta.version`** + commit `feat(publications):` + tag PATCH
