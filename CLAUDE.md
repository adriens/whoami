# whoami — CV Adrien Sales

CV et profil en données structurées (JSON Resume), source de vérité pour agents IA, embeddings et graph data science.

## Stack

- **uv** — gestion des dépendances Python (`pyproject.toml` + `uv.lock`)
- **bun** — gestion des dépendances JS (`package.json` + `bun.lock`)
- **task** (go-task) — interface unifiée pour toutes les tâches (`Taskfile.yml`)

## Tâches disponibles

Toujours passer par `task` pour lancer les opérations :

```sh
task validate     # Valider manual/resume.json contre le schema JSON Resume
task build        # Générer public/index.html + fonts
task serve        # Prévisualiser dans le navigateur (localhost:4000)
task export-html  # Exporter en HTML autonome (resume.html)
task install      # Installer les dépendances JS (bun)
task clean        # Supprimer les fichiers générés
```

## Fichiers clés

- `manual/resume.json` — le CV au format JSON Resume (seul fichier à éditer)
- `scripts/validate-json-resume.py` — script de validation (dépendances via `pyproject.toml`)
- `.github/workflows/validate.yml` — CI de validation sur push/PR

## Commandes directes

```sh
uv run scripts/validate-json-resume.py   # validation Python
bun install                               # install deps JS
```
