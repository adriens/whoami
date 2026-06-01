---
comments: 2
id: 1528628
is_dev_challenge: false
published_at: '2023-07-10T20:32:56Z'
reactions: 2
reading_time_minutes: 2
tags:
- api
- docker
- opendata
- showdev
title: '🤯 ridet-nc-api : service mesh API on top of heterogeneous Open Data'
url: https://dev.to/optnc/ridet-nc-api-service-mesh-api-on-top-of-heterogeneous-open-data-4c3b
---

## 🙋 About

New-Caledonia has an [Open Data platform](https://data.gouv.nc) on which public organizations (aka. [partners](https://data.gouv.nc/pages/Partenaires/)) come and share data, on various topics like:

- 🧑‍⚕️ Health
- 🌳 Ecology, climate & environment
- 🧾 Taxes incomes
- 📍 Geographic Information System (streets,...)
- 🥬 Agriculture
- 🎭 Culture & art
- 📈 Economy & employment
- 🧑‍🎓 Education
- ⚡ Energy
- 🏟️ Youth, sports, 
- 💻 Technology
- 🚌 Mobility
- ...

☝️ Unfortunately, for now, **as these datasets are provided by various [data providers](https://data.gouv.nc/pages/Partenaires/)**:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/snjw0aaxvs7gulljseup.png)](https://data.gouv.nc/pages/Partenaires/)

, there is no real common **governance on top of all these datasets.**

👉 The consequence of this is that, as a developer, you want to work on a specific transversal subject,...

> you'll have to deal many datasets to bring some real value, ... then achieve higher business values.


🐌 In a word, **before to be able to answser specific business driven questions**, you'll have to:

1. 🔬 **Learn** about the dataset dictionary
2. 💪 **Deal** with each dataset
3. 🕸️ **Link datasets** between each others with universal keys (or maintain a referential set of keys)
4. 🛍️ Make (**create, release, deploy & maintain**) this as a **nice & ready-to-use API**
5. 🎯 (At last) do your stuff : **work on your primary business goal**

## 🦥 The `DX` word

The Developer Experience (`DX`) word is quite straightforward:

> **Everyone would rather jump-start straight to step 5... and not care about the boilerplate data side.**

## 🪝 Pitch

This post is all about _"How to make it possible to **jump start to Step 5**... , and most of all, how to prepare & deliver it at scale."_

## 🍿 Demo

To discover how we handled the challenge, just enjoy the following dedicated content that will **explain the whole process within a dedicated live data story telling.**

{% youtube RawJXW_Lwag %}

## 🔖 Resources

- 📘 [Learn it](https://opt-nc.github.io/ridet-nc-api/)
- 🐋 Pull it : [`optnc/ridet-nc-api`](https://hub.docker.com/r/optnc/ridet-nc-api)
- 🛒 Use it : [on our marketplace](https://rapidapi.com/opt-nc-opt-nc-default/api/ridet-nc)