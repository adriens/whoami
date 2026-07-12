---
type: Project
title: resume-to-pokemon — CV en données × PokéAPI × embeddings
description: 'Prototype d''automatisation autour du CV-en-données : mettre en interopérabilité
  le resume.json (JSON Resume, livré en continu sur registry.jsonresume.org/adrie…'
resource: https://huggingface.co/spaces/rastadidi/resume-to-pokemon
tags:
- data
- interoperability
- api-fication
- huggingface
- ai-agents
- mcp
- frugal
- open-source
- devrel
- pacifique
- nouvelle-caledonie
timestamp: 2026-07
---

Prototype d'automatisation autour du CV-en-données : mettre en interopérabilité le resume.json (JSON Resume, livré en continu sur registry.jsonresume.org/adriens) avec la PokéAPI v2 pour découvrir « quel Pokémon on est » et pourquoi. 100% open source, on-premise, sans GPU (Core i5, 8 Gio). Réalisé pour le DEV.to Weekend Challenge (Passion edition, juillet 2026) — l'innovation frugale qui relie art, data et fun.
- HuggingFace Space `rastadidi/resume-to-pokemon` (Gradio + serveur MCP) — pur open source, aucune dépendance GPU
- Pipeline : dataset PokéAPI construit une fois (types, stats, profil-archétype métier dérivé) → embeddings `BAAI/bge-m3` → reranking cross-encoder `BAAI/bge-reranker-v2-m3` → cartes de matching partageables avec explication du score et confiance calibrée (z-score sur la shortlist)
- Interopérabilité : le CV JSON Resume publié en continu sur le registry sert de source d'entrée directe — démonstration concrète de la valeur d'un CV en données structurées
- Soumission DEV.to Weekend Challenge : https://dev.to/adriens/find-the-pokemon-you-are-w-pokeapi-your-resume-embeddings-3bb5 + démo vidéo : https://youtu.be/P1IEkb5g07I

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [api-fication](../tags/api-fication.md), [data](../tags/data.md), [devrel](../tags/devrel.md), [frugal](../tags/frugal.md), [huggingface](../tags/huggingface.md), [interoperability](../tags/interoperability.md), [mcp](../tags/mcp.md), [nouvelle-caledonie](../tags/nouvelle-caledonie.md), [open-source](../tags/open-source.md), [pacifique](../tags/pacifique.md)
