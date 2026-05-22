---
comments: 3
id: 1508079
is_dev_challenge: false
published_at: '2023-06-20T23:07:42Z'
reactions: 0
reading_time_minutes: 4
tags:
- ai
- openai
- opendata
- showdev
title: 🏖️ Smart city social content automation w/ custom AI reporter 📸
url: https://dev.to/adriens/smart-city-social-content-automation-w-custom-ai-reporter-3pj
---

## 💭 Food for thought

As a water-sport (open water swimming, Windsurf, monofin, Stand Up Paddle, prone paddleboard,...) aficionado, my outdoors activities are strongly driven by various environmental KPIs like:

- 🌬️ **Wind** (speed, direction)
- 🛰️ **Weather** (temperature, sunny, rainy, cloud coverage,...)
- 🌡️ **Water** temperature
- 🌞 **How clear** is the sky
- 🧫 **Water Quality** (safe for swim)
- 🌇 Time for **sunrise/sunset**
- ☀️ **UV index**
- 🐠 Water **Turbidity**
- 🌊 **Tidal** index

Then I started to dream about a brand new **Smart Citizen Experience**, and challenged my self with the following question :

> "How could I put all these KPIs within a single highly interoperable yet shareable smart content ?"

## 💡 Find the right media

When looking around me and trying to **find the easiest way to streamline information accross social networks**, I finally came to the evidence that **the right media was the image**, and even better:

- 🤗 **Highly optimized image** for social networks (for easy sharing)
- 📊 **Smart** (ie. embed data)

## 🗣️ Elevator pitch

> _"I create an autonomous AI driven BOT that goes to the beach, get the water status, weather related KPIs and posts smart contextual photos on social medias so community can reuse them very easily."_

## 🦜🔗 Disclaimer (about `LLM`, agents & more)

This creation **will NOT** (at least for now 😅) rely on:

- [🦜🔗 LangChain](https://github.com/hwchase17/langchain), but could have taken benefit from [Chained Prompt Template](https://langchain-contrib.readthedocs.io/en/stable/prompts/chained.html) nor [Custom Agents](https://blog.langchain.dev/custom-agents/)
- [🤖 OpenAI Function calling](https://openai.com/blog/function-calling-and-other-api-updates)
- [🤗 Huggingface Transformers Agent](https://huggingface.co/docs/transformers/transformers_agents)


## 🧬 The workflow

The highly flexible pipeline I imagined is as follows : 

1. 📥 **Web scrap (no `API` available)** water quality metrics (safe for swim or not)
2. 🔮 **Get contextual weather (aka. nowcast) data with API** call to [OpenWeather API](https://openweathermap.org/city/2139521)
3. 📜 **Create** a contextual `PROMPT` that describes the current status
4. 🎨 **Call** [OPENAI's beta Image generation API](https://platform.openai.com/docs/guides/images/image-generation-beta) to create an image
5. 📤 **Upload** image to [imagekit.io](https://imagekit.io/) (and add tags on it)
6. 🗄️ **Archive** photos [**collection as an album**](https://imagekit.io/use-cases/media-upload-management/)
7. 📢 **Streamline optimized contents** on social medias (for [**web performance and SEO**](https://imagekit.io/image-seo/)) and rely on [`cdn`](https://docs.imagekit.io/testing-and-infrastructure-setup/integrate-with-your-cdn)

## 🍿 Demo

Let's jump'in the [Notebook](https://www.kaggle.com/code/adriensales/baignade-noum-a-w-openai-apis-imagen ):

{% youtube DfdngsK-JaM %}


## 🧰 Stack

Below a little focus on the services & tools I used to create this **Smart Citizen experience**.

### 🛰️ OpenWeather (_"Weather forecasts, nowcasts and history in a fast and elegant way"_)

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i480sj2xtmcc7c8b4qqc.png)](https://openweathermap.org/city/2139521)

### 📸 _Imagekit.io_ (_"Streamline how you work with images and videos"_ )

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uhahgi02itprnp3w7mpn.png)](https://imagekit.io/use-cases/improve-web-performance-seo/)

More about [Imagekit.io](https://imagekit.io/features/automatic-image-optimization) experience and optimization:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ytruqcn68fttfkjrxqvi.png)](https://imagekit.io/features/automatic-image-optimization)

{% youtube sWcSYG1eifo %}

### 🤖 Open AI (beta) Image generation API

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eabq8p0nkjsp4aonrdhn.png)](https://platform.openai.com/docs/guides/images/image-generation-beta)

## 📢 Ask ChatGPT to tease about my BOT

### Teaser 1

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/eoa0xgo2pnwwafw7i8a8.png)

> 🎉🤖✨ Et voilà ! Notre BOT est prêt à faire des vagues sur les réseaux sociaux ! 🌊📸💥 Prêt à partager les plus belles images de la plage, avec les infos météo en prime ! 🌞🏖️🌈 C'est parti pour un été inoubliable ! 🎉🙌😎 #PlageIntelligente #BOTBaignade #CélébrationEnImages

### Teaser 2


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ib7vzil8eqmdwx7gb1fj.png)

> "🌊🤖 Notre nouveau compagnon de plage est prêt à vous surprendre ! 🏖️📲 Découvrez bientôt notre BOT autonome qui vous donnera toutes les infos sur la qualité de l'eau, le temps et bien plus encore ! 🌞🌊 Restez connectés pour profiter de la plage en toute sécurité et partager ces moments mémorables avec vos amis ! 😎📸 #TechForGood #PlageIntelligente #StayTuned"

### Tweet


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wzc28pf1qxpmbo2wsyek.png)

> "🏙️ Bienvenue dans la #SmartCity du futur! 🌟 Les 🌍 technologies modernes 💡 améliorent notre vie quotidienne! 📱💚 Des capteurs intelligents 🎯 optimisent les transports 🚗, économisent l'énergie ⚡️ et rendent la ville plus durable 🌿🏢. Une ville connectée pour un avenir meilleur! 🌐😃 #Technologie #QualitéDeVie"


### Def. Smart City


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6s4nmd4vavmq48mseup4.png)

> Une smart city, ou ville intelligente, est une ville qui utilise les technologies de l'information et de la communication (TIC) pour améliorer la qualité de vie de ses habitants, optimiser ses opérations et gérer efficacement ses ressources. L'objectif d'une smart city est de créer un environnement urbain durable, résilient, inclusif et efficace grâce à l'utilisation de diverses solutions technologiques.



