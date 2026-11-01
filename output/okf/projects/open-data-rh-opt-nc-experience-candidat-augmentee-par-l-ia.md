---
type: Project
title: Open Data RH OPT-NC — Expérience candidat augmentée par l'IA
description: 'Programme open data autour des données RH de l''OPT-NC : référentiel
  des métiers, offres d''emploi, AVPS (avis de vacances de poste) et organigramme
  publiés en o…'
resource: https://huggingface.co/opt-nc
tags:
- data
- ai-agents
- civic-tech
- huggingface
- mcp
- open-data
- api-fication
- team-lead
- pacifique
- nouvelle-caledonie
- duckdb
- schemacrawler
- interoperability
- mentorat
- devrel
- saga
- hackathon
- product
- pedagogy
- embeddings
- speaker
timestamp: 2024-01
---

Programme open data autour des données RH de l'OPT-NC : référentiel des métiers, offres d'emploi, AVPS (avis de vacances de poste) et organigramme publiés en open data pour créer une expérience candidat unique. Datasets Hugging Face, agents IA et MCPs pour rendre ces données exploitables par Claude et d'autres LLMs.
- Référentiel des métiers OPT-NC : dataset HuggingFace + application Gradio
- Référentiel des métiers OPT-NC restructuré en interopérable (stage Olivier Dinan, 07/07→11/08/2026) : DuckDB/SQLite, documentation SchemaCrawler, export PDF, site Hugo publié sur GitHub Pages, CI/CD semantic-release — https://opt-nc.github.io/odata-referentiel-metiers/
- AVPS (avis de vacances de poste) : dataset HuggingFace + agent IA de matching compétences/poste, désormais normalisées schema.org/JobPosting et exposées par API + serveur MCP
- Objectif : expérience candidat d'excellence — trouver, comprendre et candidater à un poste en quelques minutes via IA
- #HackAVP : premier hackathon calédonien dédié à l'emploi dans la fonction publique, co-organisé avec la Station N et la commission Data & IA du cluster OPEN NC — lancement 09/09/2026, finale et remise des prix au salon Tech&Co 2026 (4-5/11/2026, Domaine de Nouméa — coorganisé par la French Tech NC et OPEN NC) — https://dev.to/adriens/hackavp-premier-hackathon-dedie-a-lemploi-dans-la-fonction-publique-en-ncl-3oj0
- Jury #HackAVP constitué (29/08/2026) — pilotage du recrutement et de la composition du jury du hackathon
- Vidéo teaser #HackAVP (31/08/2026) : démonstration des ressources open data mises à disposition des candidats — API et MCP des AVPs, dataset HuggingFace, site web, flux RSS, API et open data des métiers — https://youtu.be/jHE-4l2Gwbk
- Vidéo « Who am I pipeline - Recevoir une recommendation » (01/09/2026) : ressource candidat #HackAVP illustrant l'industrialisation du CV — transformation en direct d'une recommandation LinkedIn reçue en données versionnées du resume.json via Claude — https://youtu.be/pi3kmAfxIGw
- Vidéo « HackAVP - Le slideshow des AVPs et la candidate experience sur TV et mobile » (07/09/2026, J-2 du lancement) : site des AVPs généré avec Hugo exploité en diaporama plein écran pour la valorisation des offres d'emploi sur écran de télévision/projection, avec transfert de l'expérience candidat vers mobile via QR code — https://youtu.be/dZHvKJ1OTRs
- Article + démo #HackAVP « Trouver un poste sans rien coder avec le feed RSS » (11/09/2026) : soumission personnelle sur la track SaaS, en conditions réelles — veille automatisée sur le flux RSS des AVPs via Claude CoWork (filtrage hebdomadaire par compétences/appétences), ayant permis de détecter une offre de CDO alignée avec son propre profil, avec génération assistée du CV, de la lettre de motivation et du document de préparation à l'entretien — https://dev.to/adriens/pendant-un-hackathon-data-je-trouve-une-opportunite-de-cdo-dans-ma-propre-entreprise-4bp9
- Vidéo tutoriel #HackAVP « Je soumets ma réalisation » (22/09/2026) : pédagogie candidat — parcours de soumission filmé de bout en bout (prérequis article Dev.to public, remplissage du formulaire), en s'appuyant sur sa propre soumission CDO comme exemple concret — https://youtu.be/3QG_BndMt6o
- Article #HackAVP « Linking ROME French and European ESCO job referentials with Gemma and TabPFN » (04/10/2026, Hacktoberfest Weekend Challenge « Build for a Friend ») : ressource préparée pour les étudiants MIAGE UNC concourant au hackathon — rapprochement des référentiels métiers ROME v4 (France Travail) et ESCO v1.2.1 (UE) avec des modèles ouverts sur Kaggle (EmbeddingGemma, Gemma 4, TabPFN), publiés en datasets interopérables (ROME v4, ROME-ESCO mapping) à partir de la base DuckDB ESCO odata-esco — https://dev.to/adriens/linking-rome-french-and-european-esco-job-referentials-with-gemma-and-tabpfn-f66
- Article + démo #HackAVP « J'ai mappé les offres d'emploi public de l'OPT-NC avec le référentiel ESCO » (18/10/2026) : 2ème soumission personnelle sur la track SaaS, 100 % Kaggle — rappel par embeddings (multilingual-e5-large, ~12 métiers et ~12 compétences ESCO candidats par AVP) puis validation LLM-as-a-judge (Qwen3-32B-AWQ via vLLM, mode raisonnement, traces conservées pour expliquer chaque lien), sur un dataset ESCO v1.2.1 préparé en amont ; analyses : compétences ESCO les plus demandées, profil par direction (postal transversal vs SI compétences dures), drill-down ISCO, exigences sans équivalent ESCO — https://dev.to/adriens/jai-mappe-les-offres-demploi-public-de-lopt-nc-avec-le-referentiel-esco-a-laide-dembeddings-5765 — démo https://youtu.be/cKV_tJ6qdSo — notebook https://www.kaggle.com/code/adriensales/avp-opt-nc-esco-qwen/notebook
- Évaluation des 11 soumissions #HackAVP outillée en données (23→26/10/2026) : jury de 6 membres humains constitué et animé + 4 modèles Claude (Opus, Sonnet, Haiku, Fable) notant sur la même grille /100 à 22 critères, conflit d'intérêt déclaré (l'organisateur ne note pas ses propres soumissions), classement par piste via Borda et accord inter-évaluateurs sous DuckDB, mesure de la part de texte généré par IA (Pangram, ZeroGPT, textes témoins), vote du prix du jury à la majorité absolue, rapport Quarto (R/ggplot2) — guide d'évaluation remis aux jurés en amont (21/10/2026 : 11 soumissions, grille /100, calendrier du jury) — https://dev.to/adriens/hackavp-guide-devaluation-pour-les-membres-du-jury-12i0 — https://github.com/adriens/eval-hackavp
- Cérémonie de remise des prix « Concours OPT & #HackAVP » au salon Tech&Co (05/11/2026, salle James Cook, en présence de la présidence et de la direction générale de l'OPT) : présentation du #HackAVP sur scène, discours de représentation de l'IAE-UNC par une étudiante du Master MIAGE, puis annonce des lauréats — https://technco.nc/programme/

*Type : professional*

**Tags :** [ai-agents](../tags/ai-agents.md), [api-fication](../tags/api-fication.md), [civic-tech](../tags/civic-tech.md), [data](../tags/data.md), [devrel](../tags/devrel.md), [duckdb](../tags/duckdb.md), [embeddings](../tags/embeddings.md), [hackathon](../tags/hackathon.md), [huggingface](../tags/huggingface.md), [interoperability](../tags/interoperability.md), [mcp](../tags/mcp.md), [mentorat](../tags/mentorat.md), [nouvelle-caledonie](../tags/nouvelle-caledonie.md), [open-data](../tags/open-data.md), [pacifique](../tags/pacifique.md), [pedagogy](../tags/pedagogy.md), [product](../tags/product.md), [saga](../tags/saga.md), [schemacrawler](../tags/schemacrawler.md), [speaker](../tags/speaker.md), [team-lead](../tags/team-lead.md)
