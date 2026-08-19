---
duration_seconds: 841
id: yeuByq3sgdM
lang: fr
likes: null
published_at: '2026-08-19'
tags: [opt-nc, nouvelle-caledonie, pacifique, open-data, interoperability, mentorat, pedagogy, duckdb, schemacrawler, civic-tech]
title: '🧑‍💼 Découvrir les métiers et compétences en data'
url: https://youtu.be/yeuByq3sgdM
views: 4
---

Démo de fin de stage d'Olivier Dinan (07/07 → 11/08/2026, section GLIA, DSI OPT-NC) : structuration interopérable du référentiel des métiers et compétences de l'OPT-NC, en open data.

- Site : https://opt-nc.github.io/odata-referentiel-metiers/
- Code source : https://github.com/opt-nc/odata-referentiel-metiers/

Point de départ : trois fichiers CSV bruts (métiers, compétences, relations) fournis par Adrien Sales, maître de stage. Le stage transforme cette donnée brute en un référentiel structuré et republié sous plusieurs formes cohérentes, toutes régénérées depuis la même source :

- Base relationnelle DuckDB (transformation, calculs) puis réplique SQLite (consultation, portabilité, mode serverless)
- Détection d'anomalies dans les données sources (niveaux de compétence à zéro non renseignés, libellés dupliqués sous des codes différents) via des vues SQL
- Documentation de schéma générée avec SchemaCrawler
- Export PDF du référentiel
- Site statique Hugo (thème relearn) publié sur GitHub Pages : navigation par famille/métier, recherche par code
- Task file pour orchestrer les commandes de génération
- CI/CD GitHub Actions : semantic-release sur main/develop, vérification sur pull request, déploiement automatique du site
- Analyse exploratoire des ressemblances entre compétences (formulation, sens), proposée par le maître de stage
