---
comments: 13
id: 1635646
is_dev_challenge: false
published_at: '2023-10-19T20:25:36Z'
reactions: 4
reading_time_minutes: 2
tags:
- ai
- opensource
- python
- beginners
title: '🦙 Mistral 7B & Ollama: LLMs 💏 Apache 2.0 Open Source on small hardwares'
url: https://dev.to/adriens/mistral-7b-ollama-llms-apache-20-open-source-on-small-hardwares-3ln3
---

## 💭 About

I recently felt on this news:

{% embed https://techcrunch.com/2023/09/27/mistral-ai-makes-its-first-large-language-model-free-for-everyone/ %}

The two key points that kept my attention were:

> _the model was released under the `Apache 2.0 license`,..._

and

> _`Mistral 7B` is a further refinement of other “small” large language models like `Llama 2`, offering similar capabilities (according to some standard benchmarks) at a considerably smaller compute cost_

Then a few weeks later the release of the ["GenAI Stack"](https://neo4j.com/press-releases/neo4j-docker-ollama-langchain-genai-launch/):

{% twitter 1711407364459413547%}

👉 So I started to look around... and **find the benefits I could take out of these tools.**

## 💭 Then & now

Actually my only two options were:

- **Use my OpenAI account** and use [`gpt-3.5-turbo`](https://platform.openai.com/docs/models/gpt-3-5) flavours or [`gpt-4`](https://platform.openai.com/docs/models/gpt-4) to achieve custom projects (and share my data with OpenAI)
- **Use Kaggle GPUs** resources & play with resources for free... still with the need to share (at least temporarly my resources) with Kaggle

## 🎯 What we'll achieve

With these two announcements, **I wondered what I could achieve locally on my own hardware**:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kmbyl5gksmc8dm8rxpjt.png)

👉 This blog post is dedicated to the **unboxing of this stack and the amazing  perspectives it unleashes... and why Open Source matters.**

## 🍿 Demo

{% youtube uq2Myz4uYkU %}

## 💡 Load any custom model into `ollama`

Below a short an easy trick on how to install a finetuned custom model into `ollama` : [`jackalope-7b`](https://huggingface.co/openaccess-ai-collective/jackalope-7b) (a fine tuned version of [`Mistral-7B`](https://huggingface.co/mistralai/Mistral-7B-v0.1)).

{% youtube 3BnnsQCmgLo %}

## 🔖 Bookmarks

- [🦙 `ollama.ai`](https://ollama.ai/)
- [🌬️ `mistral.ai`](https://mistral.ai/)
- [📢 `Mistral 7B` announcement](https://mistral.ai/news/announcing-mistral-7b)

More about GenAI stack

{% twitter 1713983398396526657 %}