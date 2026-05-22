---
comments: 3
id: 3658489
is_dev_challenge: true
published_at: '2026-05-17T22:47:08Z'
reactions: 9
reading_time_minutes: 4
tags:
- devchallenge
- gemmachallenge
- gemma
- dataengineering
title: 🧞‍♂️Transform unstructured PDFs Job Offers into a dataset w. gemma4:2b
url: https://dev.to/adriens/transform-unstructured-pdfs-job-offers-into-a-dataset-w-gemma42b-4ggb
---

*This is a submission for the [Gemma 4 Challenge: Build with Gemma 4](https://dev.to/challenges/google-gemma-2026-05-06)*

## 🤔 About the power of collections and our ability to compare things

First a bit of philosophy.

Did you notice how we tend to align things, tend to shape things so they can be aligned, compared (based on a common attributes like color, weight,...).

> Comparing objects is much easier when they share common structure, **then we can use attributes to get more knowledge, produce KPIs, make clever choices and put things in evidence.**

**👉 Well the same happens with machines : it's much much easier to compare and manage documents when they share a same structure.**

This is the very core idea that motivated this work to explore how Open Source AI could help in a very pragmatic way... and feel the opportunities it opens with concrete prototypes.

## 🙋 What I Built

I've built a whole real life and live data pipeline that takes as input Open Data Public Sector Job offers ([`dataset/avis-de-vacances-de-poste-avp-drhfpnc`](https://data.gouv.nc/explore/dataset/avis-de-vacances-de-poste-avp-drhfpnc)) :

- `csv`
- Raw `PDFs`

Then, 

1. From a dedicated GH repo [`adriens/avps`](https://github.com/adriens/avps) I've prepared a whole structured mix of `md` thanks to `csv`
2. Then from the GH Action I did transform brut raw PDFs with [`pypi.org/marker-pdf`](https://pypi.org/project/marker-pdf/) into `markdown`
3. I ended to publish a dedicated Zensical `gh-pages` website : [`adriens.github.io/avps`](https://adriens.github.io/avps/)

Next, this is where things go really interesting : I wanted to be able to compare job offers the one against the others... **but markdown were far too much different the one from others** : 

- Not the same number of sections
- Not the same section titles : hard skills, soft skills, missions,...
- Not the same levels of sections
- Not necessarly itemized the one 
- Not the same style at all (section levels, CAPITALs, email, cities...)

... which made it very hard... or even impossible to compare them amongs the others... or even crazier : put them in a traditional SQL structured database.

**👉 This is where `gemma4:2b` comes in to create a very well and consistent set of markdowns** that can then be used for various use cases : 

- **Create very well structured `ePub`** to read job offers on the go (and docx)
- **Create a very clean and well organized PDF** : very easy to load in assistants, print or to drop in any assistant
- **Deliver structured data** with clean `json` files
- **Make a `duckdb` database and perform `SQL`** on the data by using the now well structured markdowns, which made it possible to open unprecedented and exciting reporting opportunities (here in `duckdb`)
- **Share all this** as a dataset on Kaggle

```sql
SELECT '--- RÉPARTITION DES COMPÉTENCES PAR DOMAINE ---'
as titre_report;
SELECT domaine, count(*) as nb_competences 
FROM savoir_faire 
GROUP BY 1 ORDER BY 2 DESC;
```
{% twitter 2055533578021396775 %}

# 🎯 Problems it solves

In input we really had very various kind of PDF documents, and no structured tabular data, now, they both are delivered as : 

- Well formated and structured markdown
- A real database that embeds data as tables and views for advanced SQL reporting and charting
- Ready to use and perfectly well structred ePub and PDF documents, very easy for LLMs to understand

# 🤗 Experience it creates

The experience is rather an data experience as thanks to data normalisation and standardization we can load and compare job offers, which make job search and indexing much much more efficient, whatever the input.

Last but not least, using `gemma4:2b-it` proves that great things can be achieved even with small resources and that well prepared data opens so many intelligence opportunities, without having to deal with frontier models as _"the output I got is good enough"_.

## 🍿 Demo

{% youtube Rui7jSKNJNk %}

## 💰 The benefits : then and now

Below the benchmark of markdown before and after

### ⚖️ Benchmark : **`marker-pdf` vs. `marker-pdf` ➕ `gemma4:e2b`**

Below some results:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/djebvux6akthvn2tn4bb.png)

Structure consistency:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5qu87m44rlsez1bvz0vt.png)

### 📊 Analytics on top of database

One the well-structured `json` could be produced from the markdown I could efficiently load them into a `duckdb` database and do some reporting see [AVPS DRHFPNC - Les pdf en `SQL` avec `duckdb`](https://www.kaggle.com/code/adriensales/avps-drhfpnc-les-pdf-en-sql-avec-duckdb) Kaggle notebook : 

{% twitter 2055751934301380738 %}
 

## 📜 Code

- Kaggle Notebook : [IA AVPs DRHFPNC Structurés](https://www.kaggle.com/code/adriensales/ia-avps-drhfpnc-structur-s)
- Kaggle dataset : [`avps-nouvelle-caldonie-structurs/data`](https://www.kaggle.com/datasets/adriensales/avps-nouvelle-caldonie-structurs/data)
- GitHub repo [`adriens/avps`](https://github.com/adriens/avps)
- Zensical website : [`adriens.github.io/avps`](https://adriens.github.io/avps/)
- Kaggle notebook that shows how to load structured `json` into a `duckdb` database : [AVPS DRHFPNC - Les pdf en `SQL` avec `duckdb`](https://www.kaggle.com/code/adriensales/avps-drhfpnc-les-pdf-en-sql-avec-duckdb)

## 🎁 Goodies

- [Notebook LM](https://notebooklm.google.com/notebook/fa2d947b-4d60-4381-974c-5ea37f07f602)


## 💡 How I Used Gemma 4

I chose `google/gemma-4/transformers/gemma-4-e2b-it` from [`kagglehub`](https://github.com/Kaggle/kagglehub) as I had a huge amounf of data to load (all New-Caledonia ones) and a restricted amount of time on Kaggle as well as small GPUs.

> Also my intent was to be able to **run this code one day onPrem on my very own hardware so I decided to stay as little as possible.**

## 🤔 What remains to do...

Try to: 

- **Add an evaluation phasis** to check output consistency
- **Try to switch to CPU mode** so the Notebook can be scheduled without exceeding the maximum Kaggle window
- Use [`gemma-4-E4B`](https://huggingface.co/google/gemma-4-E4B) and benchmark output quality
- **Produce native `adoc`** with proper annotations
- **First produce `json`** (and more standardized values, enums,...) then re-generate `md`/`adoc` from it
