---
comments: 11
id: 1910871
is_dev_challenge: false
published_at: '2024-07-10T23:27:11Z'
reactions: 3
reading_time_minutes: 2
tags:
- opensource
- ai
- showdev
- python
title: '🔀 Semantic Router w. ollama/gemma2 : real life 10ms hotline challenge 🤯'
url: https://dev.to/adriens/semantic-router-w-ollamagemma2-real-life-10ms-hotline-challenge-1i3f
---

## ❔ About `CCaaS` (aka. Contact Center as a Service)

Cf [Gartner](https://www.gartner.com/reviews/market/contact-center-as-a-service) : 

> "Gartner defines contact center as a service (`CCaaS`) as solutions offering SaaS-based applications that enable customer service departments to manage multichannel customer interactions holistically from both a customer-experience and employee-experience perspective. CCaaS solutions offer an adaptive, flexible delivery model with native capabilities across the four functional components of the technology reference model for customer service and support. CCaaS providers also offer productized integrations with partner solutions through application marketplaces."

👉 Today, we'll cover some of these aspects by **focusing on how to efficiently route a huge number and variety of questions into a ridiculuous little amount of topics** so they can be efficiently managed by the proper adequate services.

To achieve that, we'll use 100% Open Source software, on **locally running LLMs**, thanks to the following stack : 

- **📘 A custom hand-made** dataset
- [`🦙 ollama`](https://ollama.com/)
- [`🤖 gemma2`](https://huggingface.co/docs/transformers/main/en/model_doc/gemma2)
- [🔀 Semantic Router | Aurelio AI](https://www.aurelio.ai/semantic-router)

## 💰 Expected benefits

- Save a lot of **human time**
- Save a lot of **money** (less LLM/GPU calls)
- **Dispatch tasks** according to their kind or complexity on different channels
- Keep (Kanban-like) swimlanes clean to **get an optimal throughput**

## 🍿 Demo for impatients

{% youtube QHqti5NprX8 %}


## 📚 Data sources

- **Public Facebook** human moderations
- **Corporate** websites


Below some real life datasources I used:

- [Je déménage et je souhaite que mon fixe et mon Internet me suivent](https://www.opt.nc/particuliers/telephonie-fixe/je-demenage-et-je-souhaite-que-mon-fixe-et-mon-internet-me-suivent)
- [Je déménage et je suis client CCP](https://www.opt.nc/particuliers/services-financiers/je-demenage-et-je-suis-client-ccp)
- [Pour toutes assistance concernant une coupure ou une perturbation de ma ligne Fixe ou Internet](https://www.opt.nc/assistance/assistance-coupure-et-perturbation-internet-fixe)
- [Bien entretenir ma ligne de téléphonie fixe ](https://www.opt.nc/particuliers/telephonie-fixe/bien-entretenir-ma-ligne-de-telephonie-fixe) 

## 🗣️ Real life Q&A interactions examples

Below some real life customer Q&As:

> "Je déménage et je souhaite que mon fixe et mon Internet me suivent"

**💡 Answer** : Go to https://www.opt.nc/particuliers/telephonie-fixe/je-demenage-et-je-souhaite-que-mon-fixe-et-mon-internet-me-suivent

> "Je déménage et je suis client CCP"

**💡 Answer** : Go to https://www.opt.nc/particuliers/services-financiers/je-demenage-et-je-suis-client-ccp

## 🔖 Resources

Source code is available below : 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o3wce9vis025t0oe2xb5.png)](https://www.kaggle.com/code/adriensales/semantic-router-ollama-gemma2-hotline)