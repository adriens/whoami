---
type: Project
title: Person Counter — Comptage ML pour optimiser l'occupation des salles de réunion
description: API Java de détection et comptage d'entités par vision par ordinateur,
  basée sur DJL (Deep Java Library) et TensorFlow. Alimentait un dashboard ELK Stack
  en KP…
resource: https://github.com/adriens/person-counter-api
tags:
- ai-agents
- architecture
- java
- open-source
- pacifique
- nouvelle-caledonie
timestamp: 2020-11
---

API Java de détection et comptage d'entités par vision par ordinateur, basée sur DJL (Deep Java Library) et TensorFlow. Alimentait un dashboard ELK Stack en KPIs temps réel et heatmaps pour optimiser l'occupation des salles de réunion à l'OPT-NC. Distribuée en image Docker sur DockerHub. Documentée dans un article LinkedIn Pulse.
- DJL + TensorFlow : inférence ML en Java sans dépendance Python — intégration native Spring Boot, image Docker publique sur DockerHub
- Dashboard Kibana temps réel : KPIs d'occupation + heatmaps issues des flux API — aide à la décision sur la gestion des espaces de travail
- API REST avec filtres par classe d'objet et seuil de confiance, endpoints de visualisation, métadonnées et analyse
- Article LinkedIn Pulse publié : démonstration de la valeur métier du ML appliqué à l'optimisation des espaces
- API conteneurisée (person-counter-api) : **91 pulls** Docker Hub
- Système d'alerte from scratch sur Raspberry Pi 4 + caméra : détection temps réel + appels webhooks — implémenté avec un stagiaire (Guillaume Bertherat, 2021)

*Type : professional*

**Tags :** [ai-agents](../tags/ai-agents.md), [architecture](../tags/architecture.md), [java](../tags/java.md), [nouvelle-caledonie](../tags/nouvelle-caledonie.md), [open-source](../tags/open-source.md), [pacifique](../tags/pacifique.md)
