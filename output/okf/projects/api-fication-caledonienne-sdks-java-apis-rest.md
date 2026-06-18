---
type: Project
title: API-fication calédonienne — SDKs Java & APIs REST
description: 'Démarche systématique de création d''interopérabilité là où elle n''existe
  pas — deux familles. Scraping : reverse-engineering de sites sans API → SDK Java
  (JitP…'
resource: https://github.com/adriens/tickets-resto-nc-sdk
tags:
- interoperability
- civic-tech
- data
- api-fication
- scraping
- open-source
- open-data
- java
- python
- ai-agents
- mcp
- huggingface
- umbrella
- pacifique
- nouvelle-caledonie
timestamp: 2017-04
---

Démarche systématique de création d'interopérabilité là où elle n'existe pas — deux familles. Scraping : reverse-engineering de sites sans API → SDK Java (JitPack/Travis CI) → API REST Spring Boot (Heroku) → intégrations mobiles et no-code. Open data & original : sources officielles (data.gouv.nc) ou contenu original → même stack, données durables. Série LinkedIn Pulse API-fication S01/S02 + plusieurs articles DEV.to.
- Scraping — tickets-resto-nc-sdk (HtmlUnit, JitPack) + API Spring Boot : tickets restaurant NC (neocarte.nc) — aboutit à une app mobile Kotlin/Android en 3 week-ends de dev lean (LinkedIn S02E01)
- Scraping — carte-conso-plus : SDK Java (JitPack) + API Spring Boot (Heroku) pour la carte Conso+ NC — solde, partenaires, magazines, Google Sheets ; puis app mobile Kotlin/Android MVP (2019) et refonte Flutter open innovation (2020)
- Scraping — cine-city-noumea : SDK Java (JitPack) + API REST Spring Boot pour le cinéma CineCity NC. Aujourd'hui hors service (refonte upstream — même cause que mon-1012-nc)
- Scraping — eaux-baignade-noumea : scraping données publiques Ville de Nouméa + SDK Java + BeachCagouBot (bot Twitter CircleCI cron) — genèse directe du projet edb-noumea (LinkedIn S01E04)
- Scraping — mon-1012-nc : API Spring Boot sur l'annuaire 1012.nc (numéros Mobilis) — prototypée pour une app React/React Native (LinkedIn S01E04). Aujourd'hui hors service : refonte complète du site source ayant cassé le scraper — illustration concrète du coût de maintenance des approches scraping vs API officielle (et argument fort pour la stratégie catalogue APIGEE OPT-NC)
- Scraping — scalair4j (JitPack) + noumea-smartcity-api (Heroku) : SDK Java + hub d'APIs agrégeant la qualité de l'air NC (Scal-Air) et autres endpoints smart city Nouméa. Statut actuel : hébergement Heroku abandonné. Évolution prévue : refonte Python (uv) + app HuggingFace Spaces + MCP — modernisation complète de la stack avec les outils data/IA actuels
- Open data — ridetnc4j (JitPack) + ridetnc-api : SDK Java + API REST sur le registre RIDET officiel (data.gouv.nc) — **136 pulls** Docker Hub — 2 articles DEV.to (2021, 2023)
- Original — kalolo-api / kalolo-2.0 : API d'expressions caldoches publiée sur la marketplace RapidAPI — **127 pulls** Docker Hub — article DEV.to + LinkedIn 2020. Évolution prévue : dataset open d'expressions caldoches + MCP (Model Context Protocol) — exposition directe aux clients LLM (Claude, etc.) pour conversations localisées NC, démarche d'inclusivité culturelle Pacifique dans les agents IA
- Original — excuses-sdk (JitPack) + excuses-api : SDK Java + API REST, même pattern appliqué à du contenu humoristique. Évolution prévue : dataset open d'excuses + MCP — donner du caractère/humour aux agents IA via Model Context Protocol, exemple typique d'augmentation conversationnelle ludique

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [api-fication](../tags/api-fication.md), [civic-tech](../tags/civic-tech.md), [data](../tags/data.md), [huggingface](../tags/huggingface.md), [interoperability](../tags/interoperability.md), [java](../tags/java.md), [mcp](../tags/mcp.md), [nouvelle-caledonie](../tags/nouvelle-caledonie.md), [open-data](../tags/open-data.md), [open-source](../tags/open-source.md), [pacifique](../tags/pacifique.md), [python](../tags/python.md), [scraping](../tags/scraping.md), [umbrella](../tags/umbrella.md)
