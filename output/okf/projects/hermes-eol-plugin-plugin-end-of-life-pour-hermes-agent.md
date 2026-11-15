---
type: Project
title: hermes-eol-plugin — Plugin end-of-life pour Hermes Agent
description: 'Plugin Python pour Hermes Agent (Nous Research), publié sur la marketplace
  officielle : statut de support et dates de fin de vie en direct pour 480+ produits
  v…'
resource: https://hermes-agent.nousresearch.com/marketplace/eol
tags:
- devsecops
- ai-agents
- open-source
- python
- geol
- maintainer
- solo
- international
timestamp: 2026-11
---

Plugin Python pour Hermes Agent (Nous Research), publié sur la marketplace officielle : statut de support et dates de fin de vie en direct pour 480+ produits via l'API endoflife.date, afin que l'agent ne réponde plus de mémoire sur les dates de support. Prolonge la saga geol dans l'écosystème des agents IA.
- Publié sur la marketplace Hermes (Nous Research), catégorie Tools — v0.3.0, MIT, sans dépendance externe
- 5 outils : eol_search, eol_product, eol_check (produit+version, purl ou CPE, à n'importe quelle date), eol_stack_check et eol_stack_file (fichiers .geol.yaml, règles geol check --strict)
- Hook pre_llm_call : ajoute un rappel quand la conversation porte sur des versions, des montées de version, l'EOL ou des CVE
- Divulgations claires : appels réseau uniquement vers endoflife.date, pas d'accès fichiers, pas de télémétrie, cache mémoire de 6 h

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [devsecops](../tags/devsecops.md), [geol](../tags/geol.md), [international](../tags/international.md), [maintainer](../tags/maintainer.md), [open-source](../tags/open-source.md), [python](../tags/python.md), [solo](../tags/solo.md)
