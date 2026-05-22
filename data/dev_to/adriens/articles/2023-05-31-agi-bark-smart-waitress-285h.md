---
comments: 9
id: 1467511
is_dev_challenge: false
published_at: '2023-05-31T20:37:50Z'
reactions: 1
reading_time_minutes: 2
tags:
- ai
- python
- showdev
- opensource
title: 😋 AGI (bark 🐶) Smart waitress 🎙️
url: https://dev.to/adriens/agi-bark-smart-waitress-285h
---

## ❔ About

With this post you'll see how I started my first full artwork creating a bridge between:

- 📜 **Data**
- 🎙️ Sound **design**
- 🤖 **Generative** Text To Speech
- 🖌️ Video **artwork**
- 📢 Digital contents **streamline**
- 📈 **Social** networks and content embedding

## 💡 Inception

What triggered this creation is the following tweet:

{% twitter 1649118838431322113 %}

... I immediately started to think:

> "... and if I could **create a fully digital, multimodal Customer Experience** that would be ready to be shared on social platforms ?"

☝️ Also, people are talking a lot about about AGI like `Midjourney`, `DALL-E `... but very much less about **Generative AI for TTS (Text to Speech).**

## ♾️ " Voice prompts," aka. "History prompts"

As all others AGI, [`suno-ai/bark`](https://github.com/suno-ai/bark) makes no exception : it relies on "PROMPTs".

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ddey32fwt96gc1cxvst0.png)

Luckily, the bark's community is very active and share their voices prompt (and tags) discoveries :

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/060xaygwgg0iro02zzh8.png)](https://rsxdalv.github.io/bark-speaker-directory/)

## 🔁 Creative workflow

Here is the current workflow I could experiment:

1. **Create & release a SDK** to get the data
2. **Imagine a customer experience** at restaurant
3. **Develop & tune the data driven script** and build soundtrack
4. Create an **avatar** and scene for the waitress
5. **Put together soundtrack & avatar** into video
 
## 🧰 Tools

Here are the open source tools I used for now:

- [📦 `auptitcafe`](https://pypi.org/project/auptitcafe/) package to get the data
- [🎨 `bluewillow.ai`](https://www.bluewillow.ai/) : _"AI Artwork Generator"_ for avatar creation
- [🐕 `suno-ai/bark`](https://github.com/suno-ai/bark) to build effective soundtrack
- [🤏 `pydub`](https://pypi.org/project/pydub/) to compress `wav` (~ 20 Mo) to `mp3` (825.65 kB) & `webm` (1.68 MB)
- [🎥 `OpenTalker/SadTalker`](https://github.com/OpenTalker/SadTalker)
- 🦾 `T4x2 GPU` from Kaggle

## 🍿 Demos

Below are the demos:

### 🤓 How it's built (author's words)

{% youtube t6tDH8qaVSA %}

### 🎙️ Soundtrack

Output soundtrack with [`bark`](https://github.com/suno-ai/bark):

{% embed https://soundcloud.com/rastadidi/auptitcafe-take-23 %}

### 🎞️ Movie

Then put the sound into an avatar with [`SadTalker`](https://sadtalker.github.io/):

{% youtube J-j3R7fKac0 %}

## 🤔 Ideas for "later"

Automate:

1. Video creation
2. Video upload on dedicated cloud services for further optimal collaboration, digital marketing,...
3. Avatar creation so video is totally code driven... and makes content more original (and funny) on each release thanks to one time generative prompt (prompt design required)

## ↩️ Conclusion

The more I think about designing - and **achieving** - such experiences, the more I find evident the core of this kind of project is:

- 🎯 **Get a clear idea and be strongly focused** on what you want to achieve (ie. you **don't get lost in your creative journey**)
- 🔗 **Design a clean linear workflow** that focus on tasks (not tools) so you can adapt it easily as AI projects are evolving at an amazing pace (I mean **every week there are new tools**)

## 🔖 Resources

- [Kaggle Notebook](https://www.kaggle.com/code/adriensales/au-p-tit-caf-bark-generative-ai-experience/notebook)
- [🐦 `Suno AI` aka. `Onus Radio`](https://twitter.com/OnusFM)
- [🐦 `BlueWillow`](https://twitter.com/bluewillow_ai?lang=en)
- [🎙️ `rsxdalv/bark-speaker-directory`](https://github.com/rsxdalv/bark-speaker-directory)

## 🔭 Tools to prototype

{% twitter 1662292608490561540 %}