---
slug: 2026-10-ml-commits-semantiques-geol
name: "Lucas"
school: "Université de Nouvelle-Calédonie"
formation: "Licence Informatique"
type: stage
employer: "OPT-NC"
uo: "DSI/SMO/GLIA"
date_cadrage: 2026-07-22
date_debut: 2026-10
date_soutenance: ""
status: planned
etudiants: ["Lucas"]
origins:
  "Lucas": "Nouméa"
subject: "ML/NLP — classification des messages de commits sémantiques sur le code source de geol"
current_position: "Étudiant — Licence Informatique UNC"
url_git: "https://github.com/opt-nc/geol"
url_youtube: ""
url_article: ""
tags: [ml, data-science, nlp, embeddings, python, huggingface, kaggle, open-source, open-data, devsecops, go, pedagogy, unc-partnership, opt-nc, nouvelle-caledonie]
---

Stage à démarrer en octobre 2026. Cadrage présenté à Lucas lors de l'entrevue du **22 juillet 2026**, puis sujet rendu public devant la Licence Info UNC lors de la présentation de `geol` à la Station N le 6 août 2026 (commissions Data-IA et Cyber réunies) — l'auditoire comptait des étudiants et enseignants de la Licence Informatique de l'UNC.

## Sujet

Analyser la data du code source de [geol](https://github.com/opt-nc/geol) — spécifiquement l'historique de **commits sémantiques**, sur deux variables :

- le **message** du commit (texte)
- le **verbe / type** (`fix`, `feat`, `doc`, `ci`…)

Le repo sert de terrain de recherche appliquée : historique de commits suivant une convention structurée (`type(scope): verb entity`), volume suffisant, et projet open source activement maintenu. Référence sur les pratiques de commits du projet : [Better collab flows w/ git conventional commits](https://dev.to/optnc/better-collab-flows-w-git-conventional-commits-49j8).

## Attendus

1. Vérifier et classer les commits par ML / DL / NLP — techniques laissées au choix du stagiaire selon la suite de son parcours
2. Évaluer si les commits sont réellement bien classables et si le **verbe est prédictible** — notamment à l'aide d'**embeddings**
3. **Benchmarker** les différentes méthodes et déterminer l'approche optimale en termes de qualité
4. Généraliser : appliquer l'approche retenue à des repos open source **n'implémentant pas** les commits sémantiques — quitte à produire un dataset dédié, manuel ou synthétique

## Cadre

- **Stack** : Kaggle, Hugging Face
- **Travail strictement public**, sous la même licence que geol — open source et open data de bout en bout
- **Livrables** : rapport de stage LaTeX/Quarto (rendu scientifique) + vidéo
- **Sujet volontairement très ouvert** — dépendant de ce qui sera découvert et des aspirations du stagiaire
- Réserve : ne pas publier d'annonce de faille de sécurité exploitable de geol au moment de la publication du rapport
- Portfolio-ready par construction : la nature open source rend le travail directement partageable par le stagiaire

## Antériorité

- Travail d'amorce d'Adrien sur l'analyse de commits d'un autre projet open source, présenté au PMI Horizons Nouméa 2026 : https://youtu.be/hcXYVpWKjqA?t=2240
- Document et vidéo dédiés à produire par Adrien avant le démarrage, pour inspirer le travail à venir
- Lignée directe avec le stage de Thomas Quillet (2022) — dataviz & ML sur les tickets GitHub avec BERT ([2022-12-01-thomas-quillet](2022-12-01-thomas-quillet.md))

Nom complet du stagiaire et dates précises à compléter au démarrage.
