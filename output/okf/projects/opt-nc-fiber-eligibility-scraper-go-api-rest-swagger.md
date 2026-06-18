---
type: Project
title: OPT-NC Fiber Eligibility — Scraper Go + API REST + Swagger
description: Scraper Go (Chromium headless) exposant l'éligibilité fibre et ADSL de
  l'OPT-NC sous forme d'API REST avec documentation Swagger/OpenAPI 3.0 interactive.
  Archi…
resource: https://github.com/adriens/optnc-fiber-eligibility
tags:
- interoperability
- civic-tech
- go
- scraping
- api-fication
- open-source
- pacifique
- nouvelle-caledonie
timestamp: 2025-12
---

Scraper Go (Chromium headless) exposant l'éligibilité fibre et ADSL de l'OPT-NC sous forme d'API REST avec documentation Swagger/OpenAPI 3.0 interactive. Architecture clean (cmd/internal/pkg), dual mode CLI + API, image Docker Hub publique, Taskfile. Fait sur temps personnel — data citizen.
- Scraping Chromium headless en Go — approche plus robuste que HtmlUnit Java (2017), gère le JavaScript des formulaires OPT-NC
- API REST sémantique : 200 (numéro trouvé), 404 (inconnu), 400 (format invalide) — retourne fibre, ADSL, liste des FAIs NC disponibles
- Swagger UI embarqué (OpenAPI 3.0) : documentation interactive générée depuis annotations Go
- **439 pulls** Docker Hub — image publique rastadidi/optnc-fiber-eligibility + Taskfile pour build/run/test/logs

*Type : open-source*

**Tags :** [api-fication](../tags/api-fication.md), [civic-tech](../tags/civic-tech.md), [go](../tags/go.md), [interoperability](../tags/interoperability.md), [nouvelle-caledonie](../tags/nouvelle-caledonie.md), [open-source](../tags/open-source.md), [pacifique](../tags/pacifique.md), [scraping](../tags/scraping.md)
