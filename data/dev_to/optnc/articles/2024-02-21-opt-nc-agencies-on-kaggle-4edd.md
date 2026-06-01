---
comments: 1
id: 1766021
is_dev_challenge: false
published_at: '2024-02-21T20:00:48Z'
reactions: 0
reading_time_minutes: 2
tags:
- datascience
- opendata
- python
- showdev
title: 📍 OPT-NC agencies on Kaggle
url: https://dev.to/optnc/opt-nc-agencies-on-kaggle-4edd
---

## ❔ About

OPT-NC has [many agencies in New-Caledonia](https://www.opt.nc/service/l-opt-pres-de-chez-moi-trouver-une-agence), but getting `csv` files was not as easy as that, and if you wanted to use data to build datascience, **you had to achieve manual tasks.**

**👉 The purpose of this post is to show how we recently upgraded the [Developer experience](https://github.blog/2023-06-08-developer-experience-what-is-it-and-why-should-you-care/)... and the opportunities it does open.**

## 🎯 What you'll learn

You'll learn:

- **🛍️ The various datasources** we used to build a consistent & up-to-date dataset
- **🎁 Available dataformats** (`csv`, `duckdb`)
- **🎀 How to use** the dataset with a dedicated Notebook

## 🍿 Demo

{% youtube Y5PWxaxz1_E %}

## 📑 Related resources

1. [⚙️ Notebook builder](https://www.kaggle.com/code/optnouvellecaldonie/open-data-agences-opt-nc) (where the data is prepared and aggregated)
2. [🏤 Agences 📍 Dataset](https://www.kaggle.com/datasets/optnouvellecaldonie/agences-new)
3. [👨‍🎓 Agences OPT-NC for dummies](https://www.kaggle.com/code/optnouvellecaldonie/agences-opt-nc-for-dummies)

## 🤯 Opened perspectives

Delivering data on Kagglle make it possible to play with them with free GPU and...

Amazing Open Source AI models like `Mixtral` (see [Kaggle model card](https://www.kaggle.com/models/mistral-ai/mixtral))...

and more recently `google/gemma` (see [Kaggle model card](https://www.kaggle.com/models/google/gemma)):

{% twitter 1760289388204900633 %}

... or many other open source LLM models, see :

{% embed https://dev.to/adriens/local-open-source-ai-a-kind-ollama-llamaindex-intro-1nnc %}

or simply use OpenAI from your notebook and the AI do the job for you so yo can focus on your storytelling:

{% embed https://dev.to/adriens/put-magic-in-your-notebook-w-jupyter-ai-3co4 %}