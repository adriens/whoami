# ESCO — rattachement du profil au référentiel européen

[ESCO](https://esco.ec.europa.eu/fr) (European Skills, Competences, Qualifications and Occupations) est la classification multilingue officielle de l'UE des compétences et métiers. Chaque concept a une **URI stable** qui sert d'identifiant :

```
http://data.europa.eu/esco/skill/<uuid>        # compétence / connaissance
http://data.europa.eu/esco/occupation/<uuid>   # métier (avec code ISCO-08 étendu)
```

## Source de vérité

`manual/resume.json` — les références exactes y sont stockées :

| Champ | Contenu |
|---|---|
| `skills[].x-esco[]` | `{uri, label, type, covers}` — `covers` = keywords du skill couverts par ce concept |
| `basics.x-esco-occupations[]` | métiers ESCO du profil global `{uri, label, code}` |
| `work[].x-esco-occupations[]` | métiers ESCO par poste `{uri, label, code}` |
| `meta.x-esco-retrieved` | date de récupération des concepts depuis l'API ESCO |

## Export généré — `adriens/`

**Ne pas éditer à la main** — régénérer avec `task export-esco` (labels EN récupérés via l'API ESCO).

| Fichier | Usage |
|---|---|
| `_index.csv` | 1 ligne par lien concept × entrée du profil : `kind, esco_id, uri, label_fr, label_en, esco_type_or_code, profile_entry, level, covers` — tableur, recherche par id |
| `profile.jsonld` | profil schema.org `Person` → `knowsAbout` (compétences) / `hasOccupation` (métiers), chaque concept en `DefinedTerm` ESCO — agents IA, matching, moteurs |

## Contrôler la complétude

```sh
task audit-esco
```

Échoue (aussi en CI) si un skill n'a aucun concept ESCO, si une URI est mal formée ou si `covers` cite un keyword disparu. Affiche la **couverture keyword par keyword** : chaque keyword est soit couvert par un concept ESCO, soit listé comme non couvert (techno de niche absente d'ESCO, ex. Flutter, LED matrix, Hackathons).

## Rattacher le profil ailleurs

- **Europass** (profil + CV, [europa.eu/europass](https://europa.eu/europass/fr)) et **EURES** : les sélecteurs de compétences et de métiers *sont* ESCO. Rechercher le `label_fr` ou `label_en` du CSV → le concept sélectionné a la même URI.
- **API ESCO** — à partir d'une URI :
  ```sh
  curl -s "https://ec.europa.eu/esco/api/resource/skill?uri=<uri>&language=fr"
  curl -s "https://ec.europa.eu/esco/api/resource/occupation?uri=<uri>&language=fr"
  ```
  → labels dans 28 langues, métiers pour lesquels la compétence est essentielle/optionnelle, compétences voisines : base pour le matching d'offres.
- **Graphe / embeddings** : `profile.jsonld` et le bundle OKF (`output/okf/esco/`) exposent les mêmes URIs → jointure directe avec le référentiel ESCO complet (téléchargeable en CSV/RDF sur le portail ESCO, importable dans Neo4j) ou avec des offres d'emploi annotées ESCO.
- **Site** : le portfolio publie le même profil en JSON-LD (`<script type="application/ld+json">`), lisible par les moteurs de recherche.

## Ajouter / modifier un rattachement

Voir le workflow « Mapper un skill à ESCO » dans `CLAUDE.md`.
