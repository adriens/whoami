# whoami — CV Adrien Sales

CV et profil en données structurées (JSON Resume), source de vérité pour agents IA, embeddings et graph data science.
Site portfolio Astro déployé sur GitHub Pages : https://adriens.github.io/whoami/

## Stack

- **uv** — gestion des dépendances Python (`pyproject.toml` + `uv.lock`)
- **bun** — gestion des dépendances JS (`package.json` + `bun.lock`)
- **task** (go-task) — interface unifiée pour toutes les tâches (`Taskfile.yml`)
- **Astro 5.x** — site portfolio statique dans `site/`, déployé via GitHub Actions sur GitHub Pages

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
    recommendations/      # recos LinkedIn (*.md + _index.csv) — miroir de references[] dans resume.json
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
```

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
| `x-position`, `x-relationship`, `x-date`, `x-source`, `x-language`, `x-context` | `references` | Traçabilité et filtrage |
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
6. Bump `meta.version` + commit + tag (PATCH pour 1-2 recos, MINOR pour batch ou changement structurel)

## Taxonomie `x-tags` canonique

Pour cohérence du filtrage **cross-section**, utiliser **uniquement** ces tags. Avant d'introduire un nouveau tag, vérifier qu'aucun équivalent n'existe.

**Convention** : anglais par défaut (`interoperability`, `pedagogy`). Français admis pour soft skills sans équivalent immédiat (`mentorat`, `transmission`, `curiosite`).

- **Domaine** : `data`, `architecture`, `devsecops`, `devrel`, `management`, `pedagogy`, `interoperability`, `iot`, `mobile`, `fintech`, `civic-tech`, `ai-agents`
- **Tech** : `neo4j`, `duckdb`, `airflow`, `kafka`, `python`, `go`, `java`, `quarkus`, `spring`, `flutter`, `huggingface`, `elk-stack`, `kibana`, `power-platform`, `oracle`
- **Pattern** : `api-fication`, `open-source`, `open-data`, `scraping`, `knowledge-graph`, `mcp`, `lean`, `frugal`, `umbrella`, `packaging`
- **Géo** : `pacifique`, `nouvelle-caledonie`, `international`, `monaco`
- **Rôle** : `solo`, `team-lead`, `mentor`, `speaker`, `maintainer`, `product`
- **Recognition / Recos** : `recognition`, `peer-recognition`, `manager-recommendation`, `direct-report-recommendation`, `student-recommendation`, `intern-recommendation`, `upstream-recognition`, `client-relationship`, `cross-company`
- **Soft skills (refs)** : `leadership`, `mentorat`, `transmission`, `pedagogie`, `innovation`, `communication`, `curiosite`, `team-culture`, `human-centric`, `business-acumen`, `delivery-focus`, `force-de-proposition`, `responsiveness`, `disponibilite`, `autonomy`, `trust-building`, `knowledge-sharing`, `continuous-improvement`, `pragmatisme-techno`, `polyvalence`, `tech-enthusiasm`, `exploration-techno`, `comprehension-besoins`, `multi-technology`, `industrialisation`, `interim-management`, `long-term-collaboration`, `qualites-humaines`, `endorsement-court`, `lasting-impact`, `internship-to-hire`, `team-fit`, `dynamism`, `pleasure-to-work-with`, `broad-skills`, `technical-expertise`, `technical-excellence`, `code-quality`, `performance`, `services-web`, `api-design`, `architecture-logicielle`, `management-agile`, `veille-technologique`, `unc-partnership`, `projet-tutore`, `polytech-nice`, `premiere-experience-pro`, `stage`, `linux`, `debian`, `community-contribution`, `networking`, `geomatique`, `sig`, `dsi-noumea`, `opt-nc`, `data-science`, `database`, `curiosity`, `business-acumen`

## Conventions Git

- **Commits sémantiques** : suivre [Conventional Commits](https://www.conventionalcommits.org/) — `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`
- **Tags sémantiques** : suivre [Semantic Versioning](https://semver.org/) — `vMAJOR.MINOR.PATCH`
  - `PATCH` : corrections, précisions, suppressions de doublons
  - `MINOR` : ajout de contenu (nouveaux projets, highlights, enrichissements)
  - `MAJOR` : refonte structurelle du resume
- **Synchroniser** `meta.version` dans `manual/resume.json` avec le tag git avant de créer le tag

## Points importants

- **Toujours valider** `manual/resume.json` après modification (`task validate`)
- **Le site est 100% data-driven** : toute modification du resume.json se reflète au prochain build
- Le champ `type` sur les projets (`"open-source"` ou `"professional"`) contrôle l'affichage dans les deux sections distinctes du site
- Le badge `RÉCENT` est automatique (fenêtre glissante de 18 mois) sur les distinctions et projets
- `site/public/` est exclu du `.gitignore` via une exception `!site/public`
- Python : toujours utiliser `uv run` (jamais `python` directement)
