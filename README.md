# whoami

[![JSON Resume](https://img.shields.io/badge/JSON%20Resume-schema-5A0FC8?logo=json&logoColor=white)](https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json)
[![Validate](https://github.com/adriens/whoami/actions/workflows/validate.yml/badge.svg)](https://github.com/adriens/whoami/actions/workflows/validate.yml)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Bun](https://img.shields.io/badge/Bun-black?logo=bun&logoColor=white)](https://bun.sh)
[![Task](https://img.shields.io/badge/Task-taskfile.dev-29BEB0?logo=task&logoColor=white)](https://taskfile.dev)

Mon CV et profil en données structurées — knowledge graph personnel pour agents, embeddings et graph data science.

## Quickstart

```sh
task validate     # Valider le resume.json
task serve        # Prévisualiser dans le navigateur (localhost:4000)
task export-html  # Exporter en HTML autonome
task clean        # Supprimer les fichiers générés
```

## Structure

```
manual/resume.json                  # Le CV (seul fichier à éditer)
scripts/validate-json-resume.py     # Validation JSON Resume
.github/workflows/validate.yml      # CI GitHub Actions
Taskfile.yml                        # Tâches disponibles
```
