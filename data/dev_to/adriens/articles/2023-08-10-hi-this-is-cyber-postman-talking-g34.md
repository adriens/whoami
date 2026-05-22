---
comments: 3
id: 1546196
is_dev_challenge: false
published_at: '2023-08-10T22:00:43Z'
reactions: 2
reading_time_minutes: 2
tags:
- api
- ai
- showdev
- python
title: 📯 Hi, this is Cyber postman talking 🎙️
url: https://dev.to/adriens/hi-this-is-cyber-postman-talking-g34
---

## 🎯 About

At [`opt-nc`](https://www.opt.nc/), we have APIs to track package delivery as well as a web portal for end users called ["OPT-NC Mon espace"](https://monespace.opt.nc/):

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/52rejkuat1dr0ss5j9dj.png)

The purpose of this story telling is to show how we could imagine a performance that consists in :

> **creating a customized AI-driven digital assistant thanks to public APIs, on free tiers.**

## 👨‍🍳 The recipe

Find the recipe below:

1. 📦 A **package `id`** (as input)
2. 🔑 Get `API` **credentials** (as inputs)
3. 🎙️ **Generate a whole speech** in a high quality `mp3` (and listen some bugs too 😅)
4. 🤓 Do **something fun** with `mp3`

## 🧰 `APis` as ingredients

We will rely on:

- [`📦 opt-nc/suivi-colis`](https://rapidapi.com/opt-nc-opt-nc-default/api/suivi-colis) to track package
- [`🤖 llElevenLabs`](https://elevenlabs.io/) for **Text-to-Speech**
- [`😭 SadTalker`](https://sadtalker.github.io/) to build a **movie clip**

ℹ️ Notice that **as all have free plans**, you can run (and change this code) for free at you own convenience, **as long as it's not for commercial purpose.**

## 🍿 Build the soundtrack

That said, let's take a look at demo and have some fun, first, build the soundtrack (see [🏤 Suivi colis 🤖 🎙️ Notebook for more](https://www.kaggle.com/code/adriensales/suivi-colis/notebook)):

{% youtube gCTfPxjrJ9U %}


## 🎞️ Bring "Cyber Postman to life" ⚡

To build the movie clip, we need two ingredients:

- **🎙️ A soundtrack**: the one we have just built (`mp3`)
- **🎭 An avatar**: the one I've built myself on [`bluewillow.ai`](https://www.bluewillow.ai/)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/874z04qitxn6s9au7a7v.png)

Next, with some parameter tweaks on `Sad Talker`, we can bring our cyber postman to life:

{% youtube nIq-Vwexk4I %}

## 🔭 The "Customer Experience" screenwriter

Beyond the fun, it makes appear the **need to work on the delivery scenario speech** which may be achieved in different ways:

- 📜 **Hard code the scenario with placeholders** (current version) : you can get help from chatBOTs, **yet the final version is static**
- 🦾 Use **variables (location, status,...) and inject into AGI** ... and get an original script with a **`PROMPT` template**, play with temperature and get original content **while keeping control**
- 🤯 **Hybrid** of previous ones : create a template, **get an output then ask to AGI to build a brand new one** on top of it and carefully design a system context

From my very own point of view, **the emergence of the _screenwriter_ role is the most exciting one.**

## 🔖 Resources

Take a look at [🏤 Suivi colis 🤖 🎙️ Notebook for more](https://www.kaggle.com/code/adriensales/suivi-colis/notebook) and discover more hacks around this API below (ask to add yours):

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jmdee6o2r96rajsn6txo.png)](https://rapidapi.com/opt-nc-opt-nc-default/api/suivi-colis/details)