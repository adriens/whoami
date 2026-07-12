---
duration_seconds: 440
id: P1IEkb5g07I
lang: en
likes: null
published_at: '2026-07-12'
tags: [data, interoperability, huggingface, api-fication, ai-agents, open-source, frugal, devrel, pacifique, nouvelle-caledonie]
title: 'Discover the Pokemon you are thanks to your resume and PokéAPI & embeddings'
url: https://youtu.be/P1IEkb5g07I
views: 7
---

Démo réalisée pour le DEV.to Weekend Challenge (Passion edition), dimanche soir.
Adrien met en interopérabilité son CV en données (JSON Resume, publié en continu sur le registry https://registry.jsonresume.org/adriens) avec la PokéAPI v2 pour découvrir « quel Pokémon il est ».

- Article Dev.to : https://dev.to/adriens/find-the-pokemon-you-are-w-pokeapi-your-resume-embeddings-3bb5
- HuggingFace Space : https://huggingface.co/spaces/rastadidi/resume-to-pokemon

Principe : construction d'un dataset depuis la PokéAPI → calcul d'embeddings du `resume.json` (BAAI/bge-m3) → reranking cross-encoder (BAAI/bge-reranker-v2-m3) → cartes de matching partageables, avec explication du score et lien vers la page Pokémon officielle. Tourne on-premise, sans GPU (frugal). Résultat pour Adrien : Inteleon (type psychic/water) — cohérent avec l'architecture logicielle (Spring Boot, Quarkus, Java, Go, Maven), l'interopérabilité et le temps passé dans l'eau (triathlon).
