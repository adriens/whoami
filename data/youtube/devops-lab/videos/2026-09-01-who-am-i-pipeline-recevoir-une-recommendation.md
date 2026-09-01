---
duration_seconds: 643
id: pi3kmAfxIGw
lang: fr
likes: null
published_at: '2026-09-01'
tags: [json-resume, ai-agents, civic-tech, interoperability, services-web, nouvelle-caledonie]
title: 'Who am I pipeline - Recevoir une recommendation'
url: https://youtu.be/pi3kmAfxIGw
views: 4
---

Démonstration du pipeline "whoami" : comment une recommandation LinkedIn reçue (ici de Stéphanie Bouvet, Direction du Numérique et de la Modernisation de la Nouvelle-Calédonie) est transformée en données actionnables et versionnées dans le CV, via Claude. Le processus : lecture du resume.json (schéma JSON Resume strict) et de l'index des recommandations existantes, extraction sémantique (relation cross-company, tags métier), enrichissement du resume.json et du markdown miroir, validation de schéma, commits séparés data/CV, montée de version. Illustre aussi l'analyse d'impact d'une nouvelle recommandation : tags en première occurrence (signal fort, ex. positionnement au carrefour public/privé) vs tags renforcés (convergence, ex. civic-tech via plusieurs recommandants indépendants).

Vidéo utile en ressource #HackAVP : illustre concrètement comment industrialiser son CV à partir de retours terrain, dans la même logique candidat que le teaser #HackAVP (https://youtu.be/jHE-4l2Gwbk).

Repo : https://adriens.github.io/whoami/
