---
comments: 14
id: 1564199
is_dev_challenge: false
published_at: '2023-08-24T19:53:48Z'
reactions: 0
reading_time_minutes: 2
tags:
- ai
- openai
- api
- showdev
title: 🦜🔗 Track Package Delivery w. Langchain Agent Custom Tools
url: https://dev.to/adriens/track-package-delivery-w-langchain-agent-custom-tools-18jf
---

## ☝️ About

Big enteprises build Strategic Plans to project themselves into the future.

[OPT-NC](https://www.opt.nc/) makes no exception and has recently designed its own called _"Construire demain"_:

{% embed https://office.opt.nc/fr/strategie/construire-demain-OPT-2025 %}

A strategic plan may have a lot (maybe plenty) of points... and in the mean time should be resumable into a very few keypoints -let's say 3 -,

> **_so anyone can understand and talk about the big picture with ease._**

👉 With this post, we'll **dive into a journey** where, with the help of various AI driven tools, we will:

1. **📚 Chat** with the plan itself
2. **🤔 Imagine** a near future
3. **💡 Pitch** an idea
4. **🗣️ Explain & Implement** the idea
5. **🕹️ Play** with the prototype
6. 🎯 Loop back on strategic plan to **how it fits**
7. 🔭 Think about other **opportunities**

## 💭 About Chatbots & Primary Customer Service

Below some context about ChatBot based service, good to knonw before delivering such services in production:
[
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/csielgyveszrsp54a9n7.png)](https://www.gartner.com/en/newsroom/press-releases/2022-07-27-gartner-predicts-chatbots-will-become-a-primary-customer-service-channel-within-five-years)

## 🧰 Tools

We will use many tools here:

- [🧠 `Quivr`](https://www.quivr.app/) as "the brain" of the Strategic Plan, which holds the knowledge of what the plan we have stored in
- [🦾 `OpenAI`](https://openai.com/) : the API that will give us the `LLM`, the engine that will _"do the job"_
- [🤖 `ChatGPT`](https://chat.openai.com/) : for casual question or little explanations (eg. _"What's a `LLM` ?"_)
- [🦜🔗 `Langchain`](https://python.langchain.com/) : the framework, the "glue" we will use to interact with the `LLM`
- [😽 `Kor`](https://github.com/eyurtsev/kor) : A tool to extract structured data out raw unstructured text

## 🎯 What we'll do

In this demo, we'll see how to build very custom tools (add our very own ones) to achieve specific customer-centric  tasks... but operated by autonomous AI-driven agent.

At the end, we'll get a kind of connected chatGPT.

## 📽️ Demo

{% youtube BN5Fdtvu21Q %}

## 🤯 What Ive learned and reflexions

- **Trust** LLM capabilities (experiment early with tools)
- **Screenwriter** role
- Customer **Experience Designer**
- Designing **Custom Tools**
- About **static content** : fallback
- Agent **Contextualizaiotn**
- Agent **design**
- Agent & tools unit testing
- Chatbot KPIs

## 📚 Must-reads

- [Digital Humanism: For a Humane Transformation of Democracy, Economy and Culture in the Digital Age](https://www.goodreads.com/book/show/122035634-digital-humanism)
- [A World Without Work: Technology, Automation, and How We Should Respond](https://www.goodreads.com/book/show/51300408-a-world-without-work)
- [🎯 Data strategy for (not so) dummies](https://dev.to/optnc/data-strategy-for-not-so-dummies-1b23)