---
comments: 5
id: 1744220
is_dev_challenge: false
published_at: '2024-01-31T22:15:41Z'
reactions: 3
reading_time_minutes: 3
tags:
- ai
- opensource
- automation
- dataengineering
title: 🦿🛴Smarcity garbage reporting automation w/ ollama
url: https://dev.to/adriens/smarcity-garbage-reporting-automation-w-ollama-3eg9
---

## 💡 About

Recently I saw a pile of garbage on the sidewalk next to a street I'm living in:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ff8j7vmqjlorsvmia5f7.jpg)

Generally (it was not the first time), I apply the following process:

1. **📸 Take a photo**
2. **📝** Send a mail in which I **explain** what's wrong


... but this time **I wondered if one could automate a kind of  "sidewalk cleanup status reporting", I mean like a batch process.**

This is what triggered this reflection and pitch with the following stack:

- [`ollama`](https://ollama.ai/) : from cli, on my personal workstation (core i5/8 Go RAM)
- [`bakllava`](https://ollama.ai/library/bakllava), a _"multimodal model consisting of the [`Mistral 7B`](https://ollama.ai/library/mistral) base model augmented with the LLaVA architecture."_

I initially got two main ideas (but they have a wide range of customizations.

ℹ️ Notice that I have designed the thing so the terminal that shoots photos does not require a lot of power, but rather **rely on a remote asynchronous analysis system... to keep it as affordable as possible.**


### 🚶🛴 Streets cleaning status reporting w/ "drone like cleaning reporter agent"

- **Walk** (or bike or 🛴) along a street
- **Take photo each `n` meters** in "batch mode" (or photo-shoot only when I see anything abnormal)

### 📍 Specific spot monitoring

Sometimes, people tend to put garbage on **very specific public places that you really want to stay clean** (for health, commercial or any other reason)...

For this case, we just have to

- **Schedule a photo-shot** so you can be aware of the status of this specific spot

## 🍿 Pitch

Enough talk, let's see what it looks like:

{% youtube smtsyhVE2Lk %}

## 🔭 Real life implementation

To implement this at scale, we could:

1. **Take photoshot** with GPS enabled device
2. **Consider image compression** before to send it into the pipeline
3. **Upload the photo** on a remote place (so any low tech  device can do the job from almost anywhere)
4. **Poll the raw incoming photo**, then process each photo:
    1. **Extract metadatas** (GPS coordinates, timestamp,..) by using [`exif`](https://pypi.org/project/exif/)
    2. **Automate photo shot caption** with [`ollama-python`](https://github.com/ollama/ollama-python) 
    3. **Push data **(original source image, GPS, timestamp) in a common place ([Apache Kafka](https://kafka.apache.org/),...)
    4. Consume data into third party software (then let [Open Search](https://opensearch.org/) or [Apache Spark](https://spark.apache.org/) or [Apache Pinot](https://pinot.apache.org/)) for analysis/datascience, GIS systems (so you can put reports on a map) or any ticket management system
5. Use analytics **so human can take the final decision for intervention**
6. ☝️ Last but not least: **re-inject the decision data** in the system so we can create a maintain a dedicated decision making system (**AI photo caption and the final decision**).

## 🤗 Further, faster, stronger

Putting altogether:

- 🗸 **AI** initial scene analysis
- 🗸 **Human explanations** (why he chose the action)
- 🗸 **Human intervention (_"should we send someone to fix it?"_) [`MoSCoW`](https://en.wikipedia.org/wiki/MoSCoW_method) score**:
    - 0️⃣ : **Won't**
    - 1️⃣ : **Could**
    - 2️⃣ : **Should**
    - 3️⃣ : **Must**
- 🗸 **Human cleaner feedback loop**: how long did it take to clean it up (can be seen as a complexity score)

Then save & [share it as a proper & public HuggingFace dataset](https://huggingface.co/docs/datasets/index) may also benefit to:

1. **Create** dataset
2. **Train** a model
3. **Share** the [model](https://huggingface.co/docs/hub/models)... 

⚡ Even further, once the dataset released, we could **produce & share some synthetic data** to build models **sooner, and with higher quality.**

It may also be interesting to create an **team of AI agents** (the reporter, the analyst & decision provider) to **help in decision making**, for example by using [`crewAI`](https://github.com/joaomdmoura/crewAI).