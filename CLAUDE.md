# whoami — CV Adrien Sales

CV et profil en données structurées (JSON Resume), source de vérité pour agents IA, embeddings et graph data science.
Site portfolio Astro déployé sur GitHub Pages : https://adriens.github.io/whoami/

## Stack

- **uv** — gestion des dépendances Python (`pyproject.toml` + `uv.lock`)
- **bun** — gestion des dépendances JS (`package.json` + `bun.lock`)
- **task** (go-task) — interface unifiée pour toutes les tâches (`Taskfile.yml`)
- **Astro 6.x** — site portfolio statique dans `site/`, déployé via GitHub Actions sur GitHub Pages

## Fichiers clés

- `manual/resume.json` — le CV au format JSON Resume (**seul fichier à éditer pour le contenu**)
- `site/src/pages/index.astro` — page unique du site portfolio (data-driven depuis resume.json)
- `site/astro.config.mjs` — config Astro (`base: '/whoami'`, `site: 'https://adriens.github.io'`)
- `scripts/validate-json-resume.py` — validation du resume.json
- `.github/workflows/deploy-site.yml` — CI/CD déploiement GitHub Pages
- `.github/workflows/validate.yml` — CI validation resume.json sur push/PR

## Structure des données

```
data/
  dev_to/adriens/         # articles DEV.to @adriens
  dev_to/opt-nc/          # articles DEV.to @opt-nc
  youtube/devops-lab/     # vidéos + _stats.json (subscriber_count) + playlists/*.md + _playlists_index.csv
  goodreads/124105866/    # livres lus
  kaggle/adriensales/     # datasets Kaggle
  huggingface/rastadidi/  # datasets + spaces HuggingFace
  github/adriens/         # repos publics non-forks (repos/*.md + _index.csv + _stats.json)
  hackster/adriensales/   # projets Hackster.io (projects/*.md + _index.csv + _stats.json)
  dockerhub/rastadidi/   # images Docker Hub (images/*.md + _index.csv + _stats.json)
  pypi/rastadidi/        # packages PyPI (packages/*.md + _index.csv + _stats.json)
  linkedin/adrien-sales/
    articles/             # articles LinkedIn Pulse (*.md)
    recommendations/      # recos reçues (*.md + _index.csv) — miroir de references[] dans resume.json
    recommendations-given/ # recos données par Adrien (*.md + _index.csv) — data only, pas dans resume.json
  iot/adriens/            # inventaire devices IoT/Maker (devices/*.md + _index.csv + _stats.json)
  stagiaires/adriens/    # inventaire stagiaires et projets tutorés encadrés (stagiaires/*.md + _index.csv + _stats.json)
  zenodo/adriens/        # publications scientifiques Zenodo (publications/*.json + _index.csv) — JSON-LD schema.org/ScholarlyArticle, saisie manuelle
manual/resume.json        # source de vérité CV
```

## Tâches disponibles (toujours utiliser `task`)

### Site portfolio Astro

```sh
task site-dev      # Dev local (localhost:4321)
task site-build    # Build statique → site/dist/
task site-preview  # Prévisualiser le build
task site-install  # Installer les dépendances Astro
```

### Pipeline de données

```sh
task fetch-all              # Fetch toutes les sources + knowledge base
task fetch-devto            # Articles DEV.to (adriens + opt-nc)
task fetch-youtube          # Vidéos + playlists YouTube (devops-lab)
task fetch-youtube-playlists  # Playlists uniquement (devops-lab)
task fetch-goodreads        # Livres Goodreads
task fetch-kaggle           # Datasets Kaggle
task fetch-hf               # Datasets & spaces HuggingFace (rastadidi)
task fetch-github           # Repos GitHub publics non-forks (adriens)
task fetch-hackster         # Projets Hackster.io @adriensales (Algolia API + HTML scraping)
task fetch-dockerhub        # Images Docker Hub @rastadidi (Hub API v2)
task fetch-pypi             # Packages PyPI @rastadidi (PyPI JSON API)
task build-knowledge-base   # Générer output/knowledge-base.md (full)
task build-knowledge-base-lite  # Générer output/knowledge-base.md (lite)
task build-okf              # Générer output/okf/ — bundle Open Knowledge Format v0.1
```

### Bundle OKF (Open Knowledge Format)

`task build-okf` génère `output/okf/` : un bundle [Open Knowledge Format v0.1](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) (arborescence de `.md` + frontmatter YAML reliés par liens markdown) depuis `manual/resume.json`. Artefact **généré** — `resume.json` reste la seule source de vérité ; ne jamais éditer `output/okf/` à la main. Local-only (gitignoré via `output/*`).

Particularité : les `x-tags` deviennent des **nœuds-hub** `tags/<tag>.md` reliant les sections entre elles (le graphe de connaissances du profil, navigable sans Neo4j). `skills` et `interests` (sans `x-tags`) s'accrochent au graphe par correspondance `name`/`keywords` ↔ taxonomie `x-tags`. Le script vérifie en fin de run que tous les liens internes résolvent.

### CV JSON Resume classique

```sh
task validate    # Valider manual/resume.json contre le schéma
task build       # Générer public/index.html (thème elegant)
task serve       # Prévisualiser (localhost:4000)
task export-html # Exporter resume.html autonome
task install     # Installer les dépendances JS racine
task clean       # Supprimer tous les fichiers générés
```

## Commandes directes

```sh
uv run scripts/validate-json-resume.py   # validation Python
cd site && bun run dev                   # dev Astro
cd site && bun run build                 # build Astro
```

## Extensions custom du schéma (`x-*`)

Le schéma JSON Resume accepte des propriétés additionnelles. Les champs `x-*` permettent de stocker métadonnées et filtres sans casser la validation. Utilisés sur : `basics.profiles` (jamais), `references`, `interests`, `work`, `volunteer`, `awards`, `publications`, `certificates`, `projects`, et certaines entrées d'`education`.

**`skills` n'a pas de `x-tags`** — décision explicite : `name` + `level` + `keywords` constituent déjà 3 dimensions de filtrage suffisantes. La valeur des `x-tags` est sur les sections narratives où l'on doit *cacher des entrées entières* selon l'offre ; les skills sont quasi-systématiquement montrés en intégralité.

| Champ | Où | Rôle |
|---|---|---|
| `x-tags` | toutes les sections (sauf `interests`) | Filtrage cross-section pour générer versions light par offre |
| `x-context` | `interests` | `personal` / `pro` / `mixed` — filtrer interests pour version pro |
| `x-position`, `x-relationship`, `x-date`, `x-source`, `x-url`, `x-language`, `x-context` | `references` | Traçabilité et filtrage (`x-url` pour sources non-LinkedIn : YouTube, etc.) |
| `x-label-url` | `education` | URL du label/accréditation (ex: CGE) |
| `x-summary-short` | `basics` | Version synthétique du `summary` (1 phrase) pour LinkedIn headline / signature email / header version light |

## Workflow : ajouter une recommandation LinkedIn

Quand l'utilisateur colle une reco LinkedIn brute :

### 1. Parser le format LinkedIn

LinkedIn duplique souvent les lignes (Nom doublé, headline doublée, date+relation doublée). Extraire :

- **Nom complet** → `name`
- **Headline** → `x-position` (nettoyée, garder la version pro la plus parlante)
- **Date + relation** (ex: "August 1, 2024, Adrien was Sébastien's client") → `x-date` (`YYYY-MM-DD`) + `x-relationship`
- **Texte intégral** → `reference` (langue originale, `\n` pour paragraphes)
- **Langue détectée** → `x-language` (`fr` / `en`)
- Toujours : `x-source: "LinkedIn"`

### 2. Mapper la relation

| Formulation LinkedIn | `x-relationship` | Tag central |
|---|---|---|
| `was X's client` | "Prestataire — Adrien était son client" | `client-relationship` |
| `managed Adrien directly` | "Manager direct d'Adrien" | `manager-recommendation` |
| `reported directly to Adrien` | "Direct report d'Adrien" | `direct-report-recommendation` |
| `worked on the same team` | "Collègue — même équipe" | `peer-recognition` |
| `worked but at different companies` | "Collaboration cross-company" | `cross-company` |
| Étudiant / stagiaire | "Étudiant — tuteur d'Adrien" | `student-recommendation` ou `intern-recommendation` |

### 3. Construire `x-tags`

Combiner :
- **Type de relation** (1 tag central, voir tableau ci-dessus)
- **Thèmes mentionnés dans le texte** (innovation, technical-expertise, mentorat, leadership, communication…)
- **Domaines/techs cités** (data, neo4j, schemacrawler, fintech…) — utiliser la taxonomie canonique
- **Contexte employeur si déductible** (`dsi-noumea`, `opt-nc`, `experian`)

### 4. Après chaque ajout

1. `task validate` — toujours
2. Audit cohérence des tags : `grep -oP '"x-tags": \[\K[^\]]+' manual/resume.json | grep -oP '"[^"]+"' | sort | uniq -c | sort -rn`
3. **Analyser l'apport metadata de la nouvelle reco** — deux cas distincts :
   - **Tag en 1ère occurrence** : nouvelle facette du profil jamais validée par un tiers (ex: `api-fication` et `open-data` apparus pour la 1ère fois avec Sabrina Vérolle en 2026) → signal fort, potentiellement à promouvoir en skill ou keyword
   - **Tag renforcé** : convergence entre recommandants indépendants → crédibilité accrue (ex: `innovation` à 7x, `transmission` à 4x)
4. Si un nouveau thème récurrent émerge (validé par ≥2 recos indépendantes), envisager un keyword/skill dédié dans `skills` (ex: la transmission, validée par 4 recos, est devenue une skill Expert)
5. Créer le fichier `.md` miroir dans `data/linkedin/adrien-sales/recommendations/` + mettre à jour `_index.csv`
6. Bump `meta.version` + commit + tag (MINOR — toute nouvelle entrée dans `references[]`)
7. **Toujours conclure par un feedback structuré** à l'utilisateur :
   - **1ères occurrences** : nouveaux tags jamais validés par un tiers — nommer le tag et expliquer pourquoi c'est un signal fort
   - **Tags renforcés** : tableau `tag | nouveau compte | signal` pour les plus significatifs
   - **Valeur qualitative unique** : ce que cette reco apporte que les autres n'ont pas dit (formulation spécifique, angle inédit, niveau de détail)
   - **Signal à surveiller** : si un tag atteint 2 occurrences en refs, mentionner qu'à la 3ème il vaut la peine de le promouvoir en skill

## Workflow : ajouter une recommandation donnée (LinkedIn)

Les recos données par Adrien sont **data-only** : elles ne vont pas dans `resume.json` mais uniquement dans `data/linkedin/adrien-sales/recommendations-given/`. Même formalisme que les recos reçues.

### 1. Parser le format LinkedIn

Même logique que les recos reçues. Extraire :
- **Nom complet** → `name`
- **Headline** → `position`
- **Date + relation** → `x-date` (`YYYY-MM-DD`) + `x-relationship`
- **Texte intégral** → corps du `.md` (langue originale, paragraphes séparés par ligne vide)
- **Langue** → `lang`
- Toujours : `source: "LinkedIn"`

### 2. Mapper la relation

| Contexte | `x-relationship` |
|---|---|
| Adrien était le manager direct | "Adrien — manager direct" |
| Adrien était senior sans management | "Adrien — senior, sans management direct" |
| Collaborateur / même équipe | "Adrien — collègue même équipe" |
| Prestataire recommandé | "Adrien — client du prestataire" |
| Étudiant encadré | "Adrien — tuteur industriel / intervenant" |

### 3. Construire les tags

Mêmes principes que les recos reçues : compétences et qualités de la personne recommandée, contexte employeur, relation. Ces tags décrivent **la personne recommandée**, pas Adrien.

### 4. Créer le fichier `.md`

Dans `data/linkedin/adrien-sales/recommendations-given/` avec le frontmatter suivant :

```markdown
---
slug: YYYY-MM-DD-prenom-nom
name: "Prénom Nom"
position: "Poste actuel"
relationship: "Adrien — [contexte]"
date: YYYY-MM-DD
lang: fr
source: LinkedIn
tags: [tag1, tag2, ...]
---

Texte intégral de la recommandation donnée.
```

### 5. Mettre à jour `_index.csv`

`data/linkedin/adrien-sales/recommendations-given/_index.csv` — même colonnes que les recos reçues.

### 6. Commit

Pas de bump de `meta.version` (pas de modification de `resume.json`). Commit `chore(data)` ou `feat(data)` selon le volume.

## Workflow : ajouter un témoignage YouTube

Quand l'utilisateur fournit l'URL d'un clip YouTube (élève, collaborateur, prestataire) :

### 1. Récupérer le transcript

```sh
uv run --with youtube-transcript-api scripts/yt-transcript.py <video_id_ou_url>
```

Accepte un `video_id` brut ou une URL complète (`youtu.be/xxx`, `youtube.com/watch?v=xxx`). Tente le français puis l'anglais en fallback.

### 2. Vérifier si la vidéo est dans le channel devops-lab

```sh
grep "<video_id>" data/youtube/devops-lab/_index.csv
```

Si présente → récupérer la date de publication exacte et le titre. Sinon, noter la date de publication YouTube visible sur la page.

### 3. Extraire les infos

- **Nom** → `name` (depuis le titre de la vidéo ou le transcript)
- **Position** → `x-position` (formation/rôle mentionné dans le titre ou contexte)
- **Date** → `x-date` (`YYYY-MM-DD`) = date de publication de la vidéo
- **Texte nettoyé** → `reference` : supprimer les "euh", artefacts de sous-titres auto, restructurer en paragraphes logiques avec `\n\n`
- **Langue** → `x-language`
- Toujours : `x-source: "YouTube"`, `x-url: "<url_du_clip>"`

### 4. Mapper la relation

Même tableau que LinkedIn, adapté au contexte vidéo :

| Contexte | `x-relationship` | Tag central |
|---|---|---|
| Étudiant cours UNC/MIAGE | "Étudiant [formation] UNC — Adrien intervenant pédagogique" | `student-recommendation` |
| Élève lycée (projet tutoré) | "Élève [lycée/filière] — Adrien tuteur industriel" | `student-recommendation` |
| Collaborateur / collègue | "Collègue — [contexte]" | `peer-recognition` |
| Prestataire | "Prestataire — Adrien était son client" | `client-relationship` |

### 5. Construire `x-tags`

Même logique que LinkedIn : type de relation + thèmes du transcript + contexte géo/employeur.

### 6. Après chaque ajout

1. `task validate` — toujours
2. Audit tags (Python) :
   ```sh
   python3 -c "
   import json; from collections import Counter
   data = json.load(open('manual/resume.json'))
   refs = [t for r in data.get('references',[]) for t in r.get('x-tags',[])]
   [print(f'{c:3d}  {t}') for t, c in Counter(refs).most_common()]
   "
   ```
3. Analyser l'apport : tags en 1ère occurrence (nouvelle facette) vs renforcés (convergence)
4. Créer le fichier `.md` miroir dans `data/linkedin/adrien-sales/recommendations/` (même dossier que LinkedIn, `x-source` différencie)
5. Mettre à jour `_index.csv`
6. Bump `meta.version` + commit + tag (MINOR — toute nouvelle entrée dans `references[]`)
7. **Toujours conclure par un feedback structuré** : 1ères occurrences / tags renforcés (tableau) / valeur qualitative unique / signal à surveiller (voir étape 7 du workflow LinkedIn)

## Format des fichiers vidéo `.md`

Tout fichier `data/youtube/devops-lab/videos/YYYY-MM-DD-slug.md` doit avoir ce frontmatter :

```yaml
---
duration_seconds: <int>
id: <video_id>
lang: <fr|en|fr/en>
likes: <int ou null>
published_at: 'YYYY-MM-DD'
tags: []
title: '<titre exact YouTube>'
url: https://youtu.be/<id>
views: <int>
---
```

- **`lang`** : langue parlée dans la vidéo — `fr`, `en`, ou `fr/en` (code-switching fréquent en contexte NC/international). Déterminée en lisant le transcript, pas seulement le titre.
- **`tags`** : liste vide par défaut ; enrichir si des tags thématiques sont évidents.
- Le corps du fichier contient le lien vers l'article ou projet associé + les chapitres horodatés.

## Règle : lire le transcript pour toute vidéo

**Obligatoire pour toute vidéo ajoutée**, quelle que soit l'origine (nouvelle vidéo, vidéo rendue publique, témoignage) :

```sh
uv run --with youtube-transcript-api scripts/yt-transcript.py <video_id_ou_url>
```

Le titre seul ne suffit pas. Le transcript permet de :
- Déterminer la langue réelle (`lang`) — le titre peut être dans une langue, la vidéo dans une autre
- Identifier les entrées `resume.json` liées (projets, awards, skills mentionnés)
- Détecter les tags manquants dans les entrées existantes
- Extraire les highlights pertinents pour les enrichissements

## Workflow : rendre publiques des vidéos YouTube existantes

Quand l'utilisateur indique qu'une ou plusieurs vidéos privées viennent d'être rendues publiques :

### 1. Lire le transcript + fetcher les métadonnées

Pour chaque vidéo :

```sh
uv run yt-dlp --dump-json --skip-download <url>   # uv run — jamais le yt-dlp du PATH (voir règle CLI Python)
uv run --with youtube-transcript-api scripts/yt-transcript.py <video_id>
```

Créer le fichier `data/youtube/devops-lab/videos/YYYY-MM-DD-slug.md` (format ci-dessus, `lang` déterminé par le transcript) et ajouter la ligne dans `_index.csv` (trié du plus récent au plus ancien).

### 2. Identifier les entrées `resume.json` liées

**Obligatoire** — vérifier si la vidéo se rattache à une entrée existante (`awards`, `publications`, `projects`, `work`, `volunteer`) :

- Grep le titre, le sujet ou les mots-clés de la vidéo dans `resume.json`
- Si une entrée liée existe → passer à l'étape 3
- Si aucune entrée → commit data-only (`chore(youtube)`) sans bump de version

### 3. Enrichir l'entrée liée dans `resume.json`

- **`x-tags`** : ajouter les tags manquants au regard du contenu — notamment `devrel` (talk public), `nouvelle-caledonie` (si projet NC à l'international), tags tech/domaine absents
- **`summary`** ou **`highlights`** : référencer les URLs des vidéos publiques + enrichir le contexte (ex : Nème participation consécutive, CFP sélectionné, etc.)

### 4. Valider, bumper, commiter

1. `task validate`
2. Bump `meta.version` (PATCH)
3. Commit `feat(<section>)` pour l'enrichissement `resume.json` (séparé du commit data `chore(youtube)`) + tag

## Workflow : ajouter une publication Zenodo

Quand l'utilisateur fournit une URL ou un DOI Zenodo :

### 1. Récupérer les métadonnées

Fetch la page Zenodo pour extraire : titre, DOI, date, abstract, keywords, licence, repo GitHub associé.

### 2. Créer le fichier JSON-LD

Dans `data/zenodo/adriens/publications/YYYY-MM-DD-slug.json` en suivant le schéma `schema.org/ScholarlyArticle` documenté dans `data/zenodo/README.md`.

### 3. Mettre à jour `_index.csv`

`data/zenodo/adriens/_index.csv` — colonnes : `slug, name, doi, datePublished, inLanguage, keywords, url`

### 4. Ajouter l'entrée dans `resume.json`

Section `publications[]` :
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

### 5. Auditer les skills

Comparer les `keywords` de la publication et les outils/technologies mentionnés dans l'`abstract` avec les `skills[]` du resume.json :

- **Keyword absent d'un skill existant** → l'ajouter dans `keywords[]` du skill concerné
- **Technologie non présente dans aucun skill** → évaluer si elle mérite un skill dédié (niveau + keywords)
- **Domaine renforcé** → vérifier que le `level` du skill reflète bien la profondeur démontrée

Une publication est un signal **en première personne** — plus direct qu'une recommandation tierce pour valider une compétence.

### 6. Valider et commiter

1. `task validate` — toujours
2. Bump `meta.version` + commit `feat(publications):` + tag MINOR (nouvelle entrée dans `publications[]`)

## Concept : saga

Une **saga** est un projet ou thème exploré progressivement sur plusieurs médias et dans la durée — typiquement : une série d'articles Dev.to, une playlist YouTube dédiée, des composants open source multiples, et/ou des datasets/espaces HuggingFace. La saga se distingue d'un projet ponctuel par son **caractère évolutif et documenté** : chaque nouveau medium enrichit le même sujet sans le clore.

**Critères pour tagger `saga`** (au moins 2 des 3) :
- ≥ 2 articles Dev.to sur le même sujet
- ≥ 1 playlist YouTube ou série de vidéos dédiée
- ≥ 2 composants/repos/packages distincts autour du même thème

**Sagas actives** : ColisNC, domaine.nc, temps d'attente OPT-NC, geol, auptitcafe

**Pourquoi c'est important** : le tag `saga` permet de filtrer les projets qui illustrent la capacité à construire un écosystème complet autour d'un problème — signal fort de profondeur et de durabilité, contrairement à un one-shot.

## Taxonomie `x-tags` canonique

Pour cohérence du filtrage **cross-section**, utiliser **uniquement** ces tags. Avant d'introduire un nouveau tag, vérifier qu'aucun équivalent n'existe.

**Convention** : anglais par défaut (`interoperability`, `pedagogy`). Français admis pour soft skills sans équivalent immédiat (`mentorat`, `transmission`, `curiosite`).

- **Domaine** : `data`, `architecture`, `devsecops`, `devrel`, `management`, `pedagogy`, `interoperability`, `iot`, `mobile`, `fintech`, `civic-tech`, `ai-agents`
- **Tech** : `neo4j`, `duckdb`, `airflow`, `kafka`, `python`, `go`, `java`, `quarkus`, `spring`, `flutter`, `huggingface`, `elk-stack`, `kibana`, `power-platform`, `oracle`
- **Pattern** : `api-fication`, `open-source`, `open-data`, `scraping`, `knowledge-graph`, `mcp`, `embeddings` *(recherche sémantique, RAG, reranking cross-encoder, embeddings vectoriels — ex: resume-to-pokemon, aquavena MCP, OpenSearch vector search)*, `lean`, `frugal`, `umbrella`, `packaging`, `saga` *(projet exploré progressivement sur plusieurs médias : articles Dev.to + playlist YouTube + composants multiples — ex: ColisNC, domaine.nc, temps d'attente, geol, auptitcafe)*
- **Géo** : `pacifique`, `nouvelle-caledonie`, `international`, `monaco`
- **Rôle** : `solo`, `team-lead`, `mentor`, `speaker`, `maintainer`, `product`
- **Recognition / Recos** : `recognition`, `peer-recognition`, `manager-recommendation`, `direct-report-recommendation`, `student-recommendation`, `intern-recommendation`, `upstream-recognition`, `client-relationship`, `cross-company`
- **Soft skills (refs)** : `leadership`, `mentorat`, `transmission`, `pedagogie`, `innovation`, `communication`, `curiosite`, `team-culture`, `human-centric`, `business-acumen`, `delivery-focus`, `force-de-proposition`, `responsiveness`, `disponibilite`, `autonomy`, `trust-building`, `knowledge-sharing`, `continuous-improvement`, `pragmatisme-techno`, `polyvalence`, `tech-enthusiasm`, `exploration-techno`, `comprehension-besoins`, `multi-technology`, `industrialisation`, `interim-management`, `long-term-collaboration`, `qualites-humaines`, `endorsement-court`, `lasting-impact`, `internship-to-hire`, `team-fit`, `dynamism`, `pleasure-to-work-with`, `broad-skills`, `technical-expertise`, `technical-excellence`, `code-quality`, `performance`, `services-web`, `api-design`, `architecture-logicielle`, `management-agile`, `veille-technologique`, `unc-partnership`, `projet-tutore`, `polytech-nice`, `premiere-experience-pro`, `stage`, `linux`, `debian`, `community-contribution`, `networking`, `geomatique`, `sig`, `dsi-noumea`, `opt-nc`, `data-science`, `database`, `curiosity`, `business-acumen`

## Conventions Git — Taxonomie et ontologie des commits

> **Objectif** : messages de commits analysables par ML, embeddings et reporting de tokens. Vocabulaire entièrement fermé — chaque commit est une ligne parseable par regex : `type(scope): verb entity [quantity] [(vX.Y.Z)]`.

### Format canonique

```
<type>(<scope>): <verb> <entity> [(vX.Y.Z)]

[corps structuré optionnel]
```

**Contraintes strictes :**

- **Subject en anglais uniquement** — toujours. Le corps peut être en français.
- **Subject ≤ 72 caractères**
- **Aucun emoji dans le subject** — les emojis cassent le parsing regex et ajoutent du bruit aux tokenizers. Tolérés dans le corps uniquement.
- **Un seul scope par commit** — jamais de composés (`skills/interests`, `projects,iot`)
- **Version** `(vX.Y.Z)` en fin de subject uniquement quand un bump est effectué dans ce commit
- Si plusieurs sections touchées → scope de la section la plus impactante narrativement

---

### Types (vocabulaire fermé)

| Type | Sémantique | Modifie `resume.json` ? |
|---|---|---|
| `feat` | Nouveau contenu (nouvelle entrée ou enrichissement) | Oui |
| `fix` | Correction (date, doublon, champ erroné) | Oui ou non |
| `chore` | Maintenance : data-only, rebuild, bump standalone | Non (ou bump seul) |
| `docs` | Documentation : CLAUDE.md, READMEs, workflows | Non |
| `perf` | Optimisation site ou build (images, bundle) | Non |
| `refactor` | Restructuration sans contenu nouveau | Non |

**Règle `feat` vs `chore`** : si `resume.json` est modifié avec du contenu nouveau → `feat`. Sinon → `chore`.

---

### Verbes canoniques (vocabulaire fermé)

Un seul verbe par subject. Choisir dans cette liste — ne pas inventer de synonymes.

| Verbe | Intention |
|---|---|
| `add` | Nouvelle entrée ou fichier créé |
| `enrich` | Entrée existante augmentée (tags, summary, keywords, URLs) |
| `fix` | Correction d'une valeur erronée |
| `remove` | Suppression d'une entrée ou d'un champ |
| `fetch` | Mise à jour de données depuis une source externe |
| `rebuild` | Régénération d'un artefact (knowledge base, site) |
| `bump` | Incrément de version seul (scope `release` uniquement) |

---

### Quantification

Indiquer systématiquement le volume quand > 1, pour l'agrégation directe en reporting :

```
chore(youtube): add 3 NODES24 CFP videos
chore(iot): fetch 18 new devices
feat(skills): enrich 4 keywords — JSON Schema, schema.org
feat(references): add recommendation — J. Dupont   ← singulier = 1 implicite
```

---

### Entité nommée dans le subject

Pour les sections `references`, `awards`, `publications`, `projects` : nommer l'entité principale après un tiret long `—`.

```
feat(references): add recommendation — Jean Dupont
feat(awards): add speaker — NODES24 (Neo4j, international)
feat(publications): add paper — SchemaCrawler on Zenodo
feat(projects): add geol — CLI EOL management
chore(goodreads): add review — Accelerate (5 stars)
```

---

### Corps structuré (optionnel, machine-readable)

Pour les commits riches (multi-tags, signal fort, première occurrence), un corps en liste de faits brefs — parseable ligne par ligne par regex ou embeddings :

```
feat(references): add recommendation — Sébastien Bourlart

- tags: peer-recognition, neo4j, innovation (first occurrence)
- signal: innovation reaches 7x — strongest recurring theme
- version: v1.19.1
```

---

### Scopes — Famille 1 : sections `resume.json`

Ces scopes correspondent aux nœuds de contenu du CV. Toujours utiliser le nom exact de la clé JSON.

| Scope | Section JSON | Exemple |
|---|---|---|
| `basics` | `basics` (summary, profiles, x-summary-short) | `feat(basics): add x-summary-short` |
| `work` | `work[]` | `feat(work): add OPT-NC GLIA section head` |
| `education` | `education[]` | `feat(education): add Mastère MIAGE` |
| `skills` | `skills[]` | `feat(skills): add DuckDB — Expert level` |
| `projects` | `projects[]` | `feat(projects): add geol — CLI EOL management` |
| `awards` | `awards[]` | `feat(awards): add speaker — NODES24` |
| `publications` | `publications[]` | `feat(publications): add paper — SchemaCrawler` |
| `references` | `references[]` | `feat(references): add recommendation — J. Dupont` |
| `volunteer` | `volunteer[]` | `feat(volunteer): add Neo4j Ninja` |
| `interests` | `interests[]` | `feat(interests): enrich Maker — add Lo-tech keyword` |
| `certificates` | `certificates[]` | `feat(certificates): add AWS Solutions Architect` |

### Scopes — Famille 2 : sources de données

Ces scopes correspondent aux dossiers `data/<source>/`. Commits quasi-exclusivement `chore`.

| Scope | Dossier | Exemple |
|---|---|---|
| `youtube` | `data/youtube/` | `chore(youtube): add 3 NODES24 CFP videos` |
| `devto` | `data/dev_to/` | `chore(devto): fetch 3 new articles` |
| `goodreads` | `data/goodreads/` | `chore(goodreads): add review — Accelerate (5 stars)` |
| `kaggle` | `data/kaggle/` | `chore(kaggle): fetch dataset stats` |
| `huggingface` | `data/huggingface/` | `chore(huggingface): add space — job-offers-nc` |
| `github-data` | `data/github/` | `chore(github-data): fetch public repos` |
| `hackster` | `data/hackster/` | `chore(hackster): add project — Person Counter` |
| `dockerhub` | `data/dockerhub/` | `chore(dockerhub): fetch image stats` |
| `pypi` | `data/pypi/` | `chore(pypi): add package — geol` |
| `linkedin` | `data/linkedin/` | `chore(linkedin): add recommendation-given — M. Gault` |
| `iot` | `data/iot/` | `chore(iot): add Raspberry Pi 5` |
| `stagiaires` | `data/stagiaires/` | `chore(stagiaires): add Thomas Quillet` |
| `zenodo` | `data/zenodo/` | `chore(zenodo): add publication JSON-LD` |

### Scopes — Famille 3 : infra et méta

| Scope | Périmètre | Exemple |
|---|---|---|
| `claude` | `CLAUDE.md` | `docs(claude): add YouTube publish workflow` |
| `ci` | `.github/workflows/` | `chore(ci): update deploy action` |
| `site` | `site/` (Astro) | `perf(site): convert hero PNG to WebP` |
| `scripts` | `scripts/` | `feat(scripts): add yt-transcript.py` |
| `release` | bump seul sans contenu | `chore(release): bump to v1.19.0` |
| `kb` | `output/knowledge-base.md` | `chore(kb): rebuild knowledge base` |

---

### Règles d'arbitrage

1. **Data + résumé enrichi → deux commits séparés** : d'abord `chore(<source>)` pour les fichiers data, puis `feat(<section>)` pour l'enrichissement `resume.json`.
2. **Scope de la section primaire** : si `awards` et `skills` sont enrichis dans le même commit, choisir `awards` (section la plus impactante narrativement).
3. **`references` toujours au pluriel** — jamais `refs`.
4. **`github-data`** pour la source de données — jamais `github` seul (ambigu avec la plateforme).

---

### Versioning sémantique

Suivre [Semantic Versioning](https://semver.org/) — `vMAJOR.MINOR.PATCH`. Synchroniser `meta.version` dans `manual/resume.json` avant de créer le tag.

| Incrément | Quand |
|---|---|
| `PATCH` | Correction, précision, enrichissement mineur (tags, summary, URLs) |
| `MINOR` | Ajout de contenu (nouvelle entrée dans une section) |
| `MAJOR` | Refonte structurelle du resume |

**Règle absolue — régénérer le bundle OKF à chaque tag.** Avant de poser le tag, régénérer et commiter le bundle OKF (artefact versionné, embarqué dans le commit taggé + déployé sur le site) :

```sh
task build-okf-viz   # régénère output/okf/ + viz.html (build-okf est en dépendance)
git add output/okf && git commit -m "chore(kb): rebuild OKF bundle (vX.Y.Z)"
```

`build-okf-viz` exécute `build-okf` puis génère `output/okf/viz.html`. Le bundle est lié dans le footer du site (`/whoami/okf/viz.html`).

**Règle absolue — pousser le tag et créer la release immédiatement.** `git push` ne pousse pas les tags. Après chaque `git tag vX.Y.Z`, enchaîner sans exception :

```sh
git push origin vX.Y.Z
gh release create vX.Y.Z --title "vX.Y.Z — <titre court>" --notes "<release notes>"
```

La release note doit lister : les changements de contenu (`resume.json`), les données ajoutées, et les évolutions de docs/workflows. S'appuyer sur `git log vX.Y.(Z-1)..vX.Y.Z --oneline` pour la construire.

## Workflow : enrichir le CV après une lecture Goodreads

Adrien met systématiquement en œuvre ce qu'il lit. **À chaque ajout d'un livre avec review personnelle**, enrichir `resume.json` avant de committer — ne pas se limiter au data-only.

### 1. Analyser la review

Lire le corps du `.md` du livre (la review Goodreads fetchée). Extraire :
- Les **thèmes principaux** du livre
- Les **actions concrètes** que la lecture a déclenchées ("ce livre m'a conduit à...", "j'ai créé...", "j'ai organisé...")

### 2. Mapper aux sections du CV

| Signal dans la review | Section à enrichir | Action |
|---|---|---|
| Thème récurrent dans la bibliothèque (≥ 2 livres) | `interests.Lecture.keywords[]` | Ajouter le keyword si absent |
| Livre a déclenché une action concrète citée dans le CV | `awards` / `projects` / `work` → `summary` | Ajouter la référence causale |
| Livre valide/démontre un skill existant | `skills[].keywords[]` | Enrichir les keywords |
| Thème absent de tout skill existant mais récurrent (≥ 3 livres) | `skills[]` | Envisager un skill dédié |

### 3. Tagger le fichier `.md` du livre

Ajouter `tags:` dans le frontmatter du fichier book généré par le fetch :

```yaml
tags: [design-thinking, innovation, creativity, human-centric, ...]
```

Tags = thèmes du livre mappés à la taxonomie canonique `x-tags`.

Le champ `tags` est **créé vide (`tags: []`) pour chaque livre** au fetch et **préservé d'un fetch à l'autre** (`scripts/fetch-goodreads.py` relit les tags existants avant de réécrire le fichier). C'est le seul enrichissement manuel qui survit au refetch — le corps (review) et le reste du frontmatter sont toujours réécrits depuis Goodreads.

### 4. Valider et commiter

1. `task validate`
2. Bump `meta.version` (PATCH si enrichissement, MINOR si nouvelle entrée)
3. Deux commits séparés : `chore(goodreads):` pour les data, `feat(interests):` (ou autre section) pour `resume.json`
4. Tag + release

## Règle absolue — Python

> **Ne jamais exécuter un script Python directement.** Toujours et uniquement `uv run`.

```sh
# INTERDIT
python script.py
python3 script.py

# OBLIGATOIRE
uv run script.py
uv run --with some-package script.py
```

Cette règle s'applique à **tous les scripts** sans exception, y compris les one-liners `-c`.

Si une lib est chargée via `--with` (usage ponctuel), l'ajouter immédiatement dans `pyproject.toml` pour la documenter et la tracer.

### Outils CLI Python (yt-dlp) — même règle

La règle vaut aussi pour les **outils CLI en Python**, `yt-dlp` en tête. Un `yt-dlp` système traîne dans `/usr/bin` (paquet distro, souvent périmé de plusieurs années → cassé par la détection bot YouTube). **Ne jamais appeler le `yt-dlp` du PATH sans savoir lequel répond.**

```sh
# À ÉVITER — peut résoudre vers /usr/bin/yt-dlp (périmé)
yt-dlp --version

# FIABLE — version pinnée du repo (celle qu'utilisent les fetchers)
uv run yt-dlp --version
```

- La version qui fait foi est celle pinnée dans `pyproject.toml` (`yt-dlp>=…`) — la maintenir fraîche (YouTube casse yt-dlp très régulièrement ; bump + `uv lock` dès qu'un fetch échoue).
- **`deno` est requis** : sans runtime JS, yt-dlp émet un warning de dépréciation et peut manquer des formats/métadonnées YouTube. Installé via `brew install deno`.

## Points importants

- **Toujours valider** `manual/resume.json` après modification (`task validate`)
- **Le site est 100% data-driven** : toute modification du resume.json se reflète au prochain build
- Le champ `type` sur les projets (`"open-source"` ou `"professional"`) contrôle l'affichage dans les deux sections distinctes du site
- Le badge `RÉCENT` est automatique (fenêtre glissante de 18 mois) sur les distinctions et projets
- `site/public/` est exclu du `.gitignore` via une exception `!site/public`
