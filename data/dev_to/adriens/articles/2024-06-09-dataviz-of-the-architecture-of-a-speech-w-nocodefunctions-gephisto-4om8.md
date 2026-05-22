---
comments: 1
id: 1881592
is_dev_challenge: false
published_at: '2024-06-09T02:24:17Z'
reactions: 1
reading_time_minutes: 1
tags:
- datascience
- dataviz
- nocode
- ai
title: 🌌 Dataviz of the architecture of a speech w/ Nocodefunctions & Gephi(sto)
url: https://dev.to/adriens/dataviz-of-the-architecture-of-a-speech-w-nocodefunctions-gephisto-4om8
---

## ❔ About

Yesterday, June 8, 2024, [Louis Mapou](https://en.wikipedia.org/wiki/Louis_Mapou), the President of the Government of New Caledonia, delivered a [solemn televised address](https://la1ere.francetvinfo.fr/nouvellecaledonie/crise-en-nouvelle-caledonie-suivez-en-direct-la-declaration-solennelle-de-louis-mapou-president-du-gouvernement-1494992.html):

{% youtube hBSo1Nq5aqQ %}

## 🎯 What we'll do

In this blog post, you'll see an **-almost- `nocode` (and open source)** way to : 

1. **Extract the `mp3`** from a given youtube video with `yt-dlp/yt-dlp`
2. **Extract the text from `mp3`** with `openai/whisper`
3. **Transform the text into a Knowledge graph** with [🔎 Nocode functions](https://nocodefunctions.com/), and get the `gexf` file
4. **Produce datavisualisations** with [Gephisto](https://jacomyma.github.io/gephisto/)
5. **Load `gexf`** file into [Gephi](https://gephi.org/) and produce some dataviz by ourselves

## 🍿 Demo

{% youtube m24Kzk-kat4 %}

## 🔖 Resources

- [Jupyter Notebook](https://www.kaggle.com/code/adriensales/declaration-solennelle-du-2024-06-08-louis-mapou)

{% embed https://github.com/adriens/declaration-solennelle-louis-mapou-2024-06-08-data %}

## 🖼️ Dataviz

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jjgl6biu5n4ilavwcc07.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m7l083ql3w3rw8hmvohn.png)

