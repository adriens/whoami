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
  youtube/devops-lab/     # vidéos + _stats.json (subscriber_count)
  goodreads/124105866/    # livres lus
  kaggle/adriensales/     # datasets Kaggle
  huggingface/rastadidi/  # datasets + spaces HuggingFace
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
task fetch-youtube          # Vidéos YouTube (devops-lab)
task fetch-goodreads        # Livres Goodreads
task fetch-kaggle           # Datasets Kaggle
task fetch-hf               # Datasets & spaces HuggingFace (rastadidi)
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
