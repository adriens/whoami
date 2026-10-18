---
duration_seconds: 304
id: cKV_tJ6qdSo
lang: fr
likes: null
published_at: '2026-10-18'
tags: [hackathon, open-data, civic-tech, embeddings, data, interoperability, nouvelle-caledonie]
title: 'HackAVP - Relier des AVPs avec le référentiel ESCO'
url: https://youtu.be/cKV_tJ6qdSo
views: 2
---

Démo de la 2ème soumission personnelle #HackAVP (track SaaS, Kaggle) : mapping automatique des avis de vacance de poste (AVP) de l'OPT-NC vers le référentiel européen ESCO.

Pipeline en 3 étapes dans un notebook Kaggle :

1. **Embeddings** (`intfloat/multilingual-e5-large`) — ~12 métiers ESCO et ~12 compétences candidats par AVP, à partir d'un dataset ESCO v1.2.1 préparé en amont (nettoyage des CSV natifs ESCO, publié en open data)
2. **Validation LLM-as-a-judge** (`Qwen/Qwen3-32B-AWQ` via vLLM, mode raisonnement) — retient ou rejette chaque candidat, en conservant les traces de raisonnement
3. **Analyses / dataviz** — compétences ESCO les plus demandées, profil de compétences par direction (postal vs SI : transversal vs compétences dures), drill-down dans la hiérarchie des métiers ESCO/ISCO, apport du raisonnement Qwen vs score brut d'embedding

Article : https://dev.to/adriens/jai-mappe-les-offres-demploi-public-de-lopt-nc-avec-le-referentiel-esco-a-laide-dembeddings-5765
Notebook : https://www.kaggle.com/code/adriensales/avp-opt-nc-esco-qwen/notebook
Dataset ESCO v1.2.1 : https://www.kaggle.com/datasets/adriensales/esco-v1-2-1
