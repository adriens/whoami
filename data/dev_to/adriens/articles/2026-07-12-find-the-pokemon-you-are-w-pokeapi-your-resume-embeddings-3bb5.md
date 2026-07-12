---
comments: 1
id: 4124120
is_dev_challenge: true
published_at: '2026-07-12T08:00:47Z'
reactions: 0
reading_time_minutes: 3
tags:
- devchallenge
- weekendchallenge
- machinelearning
- api
title: 🤗 Find the Pokemon you are w. PokéAPI, your resume & embeddings
url: https://dev.to/adriens/find-the-pokemon-you-are-w-pokeapi-your-resume-embeddings-3bb5
---

*This is a submission for [Weekend Challenge: Passion Edition](https://dev.to/challenges/weekend-2026-07-09)*

## ❔ What I Built

These two last weeks, my team mates started to to use Claude Code together with they yearly review : 

{% embed https://dev.to/adriens/versionner-et-builder-lebook-de-son-entretien-annuel-devaluation-sur-github-242k %}

**to discover which Pokemon they are... and why**.

I found that really really fun... and started to wonder

> if I could automate that with only onPrem resources, with embeddings, ML... only with a simple laptop without GPU, a simple core i5 and 8 Gib.

And of course, only with pure Open Source software ❣️

What you'll discover below is how I started to prototype it and make it happen.

## 🍿 Demo

{% youtube P1IEkb5g07I %}

## 🤗 Code

The whole code source is available as a HF Space, see [`rastadidi/resume-to-pokemon`](https://huggingface.co/spaces/rastadidi/resume-to-pokemon) for more... or to play wth it 🤓

## 🧰 How I Built It

To achieve this first prototype I : 

0. **Used the data** I already prepared with my 
[`registry.jsonresume.org/adriens`](https://registry.jsonresume.org/adriens)
1. **Bundled dataset (built once).** `build_dataset.py` fetches every
   species from the [PokeAPI](https://pokeapi.co/docs/v2) — name, types,
   base stats, sprite, genus and English Pokedex flavor text. For each
   Pokemon it also derives a **professional-archetype profile** from its
   types and stat spread (e.g. a Steel type → *"a disciplined, precise,
   robust engineer of structured systems"*), so career resumes and
   monster biology meet in the same trait vocabulary. Description +
   profile are embedded with
   [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3) and committed as
   `data/pokemon.json` + `data/embeddings.npy` — so the app makes **no
   PokeAPI calls at runtime**.
2. **Resume → phrases.** Sections that carry semantic signal —
   `basics.summary`, `skills`, `work`/`volunteer`, `projects`,
   `interests` — are each turned into a short phrase and embedded with
   the same model. (Administrative sections like education, certificates
   and languages are skipped.)
3. **Retrieve → rerank.** Cosine similarity over the embeddings
   retrieves a shortlist of the closest Pokemon; a cross-encoder
   ([`BAAI/bge-reranker-v2-m3`](https://huggingface.co/BAAI/bge-reranker-v2-m3))
   then re-scores the (resume, Pokemon) pairs jointly for much sharper
   precision than cosine alone. The tool explains *why* by quoting the
   matched resume phrase and the Pokemon's own profile + Pokedex text.
4. **Ranking + relative fit.** Pokemon are ranked by a blend of the
   rerank match and their base stats (adjustable). Because a broad
   resume matches many Pokemon similarly, raw scores cluster tightly and
   are unreadable — so the reported score is a **relative fit**: rerank
   scores are standardized across the shortlist and spread through a
   sigmoid, so the top clearly stands out (~100%) and the tail drops
   off. It's a fit *relative to the candidate pool*, not an absolute
   probability. The two best-fitting **types** are derived from the same
   shortlist, so they always agree with the ranked Pokemon.
5. **Calibrated confidence.** Instead of a raw similarity number, a
   read-out reports how far the top match *stands out from the field*
   (a z-score over the shortlist), flagging decisive vs. diffuse,
   multi-type profiles. Type scores and the ranked Pokemon are derived
   from the *same* reranked shortlist, so the "best-fit typing" always
   agrees with the cards.


<!-- Walk us through your technical approach and any interesting decisions you made along the way. If you used any of the prize category technologies, be sure to highlight how you incorporated them here! -->

