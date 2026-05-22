---
comments: 9
id: 1411571
is_dev_challenge: false
published_at: '2023-03-30T20:19:23Z'
reactions: 2
reading_time_minutes: 2
tags:
- openai
- ai
- datascience
- python
title: 🪄 Enhance/fix data quality w. openai's API 🦾
url: https://dev.to/adriens/enhancefix-data-quality-w-openais-api-dnd
---

## ❔ About

> 🤔 Sometimes you face **lack of data or data quality** issues that prevent you from producing insights.

> 💡 Whatif you could **call AI to the rescue** to fix/enhance some data

I first started some [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering) on chatGPT:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cix0nsr5b83gyaki72ph.png)

## ☝️ Notice

Notice that guessing gender on firstnames can seem useless or a bit dumb (or nerdy). Yes,but...

- 🗺️ This work relies on openAI... which acts as a **universal language firstname parser**
- 💡 **This work is just an illustration** of how prompt engineering and **OpenAPI'API can help review/fix** any kind of data quality issues... and **makes a concrete illustration on how you may enrich your enterprise data pipeline**


## 🎯 Target

The purpose of this article is to see how [openai's API](https://openai.com/product#made-for-developers) can help on a very specific testable dataset.

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gt3kmaks6g9m04yapi8n.png)](https://openai.com/blog/openai-api)


## 📝 `Kaggle` Notebook

This short notebook I will:

1. 📥 **Download** data
2. 🐼 **Load** data in [`pandas`](https://pandas.pydata.org/)
3. 🦾 **Call** [`openai`'s API](https://openai.com/blog/openai-api) to guess firstname's gender
4. ⚖️ **Compare** guessed vs. real data


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zj1z6p6ii35lhw7est4i.png)](https://www.kaggle.com/code/adriensales/openai-gender-guess-on-firstname)

## 🍿 Demo

{% youtube vDXkRrkfqRc %}

### 🗃️ Input Dataset

I have used the [`top-10-prenoms-a-noumea-depuis-1860`](https://data.gouv.nc/explore/dataset/top-10-prenoms-a-noumea-depuis-1860/information/) open dataset from [`data.gouv.nc`](https://data.gouv.nc/pages/accueil/):

{% embed https://data.gouv.nc/explore/dataset/top-10-prenoms-a-noumea-depuis-1860/ %}

## 🤖 The `text-davinci-003` model

I have used `text-davinci-003` from [`GPT-3.5` models](https://platform.openai.com/docs/models/gpt-3-5) as they can:

> "understand and generate natural language or code." 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sxmydxzvmxf7syltbwef.png)](https://platform.openai.com/docs/models/gpt-3-5)

### 📊 Results 👏

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a6hhwrclipxbgd8xwf4p.png)

## ☝️ Notice

Notice that I have put the guessed value in a dedicated structure... so we can easily flag it as AI generated when reporting its metadatas:

{% twitter 1638981460244959232 %}

## 💰 Gains

- 📈 **Data quality**
- 💡 **Better decisions** & opportunities
- 💸 Puts **the cost of the lack of data quality** in evidence (API calls are not free)
- 🧠 Create more **intelligence**

## 👨‍🔬 Further optimizations

- Benchmark models to **spend as less money as possible while getting the best results as possible**

## 🔭 News & perpsectives

{% twitter 1630992406542970880 %}

{% twitter 1638971204458663936 %}

{% twitter 1638978499452223488 %}