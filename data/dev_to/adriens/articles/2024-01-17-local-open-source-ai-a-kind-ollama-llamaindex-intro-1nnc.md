---
comments: 10
id: 1727471
is_dev_challenge: false
published_at: '2024-01-17T21:08:11Z'
reactions: 2
reading_time_minutes: 1
tags:
- opensource
- ai
- tutorial
- beginners
title: '🆓 Local & Open Source AI: a kind ollama & LlamaIndex intro'
url: https://dev.to/adriens/local-open-source-ai-a-kind-ollama-llamaindex-intro-1nnc
---

## ❔ About

Sometimes, you may need a **convenient yet powerful way** to run many `LLMs` locally with:

- **Only `CPU`** ( `i5` like)
- **Little `RAM`** (eg `<= 8Go`)
- Being able to plug **third party frameworks** ([`Langchain`](https://github.com/langchain-ai/langchain), [`LlamaIndex`](https://github.com/run-llama/llama_index)) so you can build complex projects
- **Ease of use** (few lines of code, powerful results)

👉 This is all what this post is about.

## 🎯 What you'll learn

In this short demo, you'll see how to:

- Run on Kaggle (CPU)
- Use [`ollama`](https://ollama.ai/) to run open source models
- Play with a first `LlamaIndex` example

## 💡 Benefits & opportunities

Get rid of [weekly GPU ](https://www.kaggle.com/discussions/general/108481) usage limits on free plan:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z0vasq83hpwhctyvrx3w.png)

With this `CPU` approach, you are then **able to schedule AI based workflow for free** (as long as it does not exceed the 12h window limit).

- [Scheduling notebook execution with `cron` and Kaggle API](https://www.kaggle.com/discussions/product-feedback/371090)

## 🍿 Demo

Enough teasing, let's jump in the demo:

{% youtube MroeN4aTjF4 %}

## 📜 Notebook


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kkjhg1scmd81wtm0ajx5.png)](https://www.kaggle.com/code/adriensales/ollama-running-local-models-w-llamaindex-cpu/notebook)


## 🔭 Further, stronger

To go further (48GB of RAM required, as well as GPU ), a full example around [`mixtral`](https://ollama.ai/library/mixtral), see [Running Mixtral 8x7 locally with LlamaIndex](https://blog.llamaindex.ai/running-mixtral-8x7-locally-with-llamaindex-e6cebeabe0ab).