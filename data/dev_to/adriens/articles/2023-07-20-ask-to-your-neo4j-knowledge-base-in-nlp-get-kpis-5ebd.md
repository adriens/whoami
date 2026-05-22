---
comments: 5
id: 1536423
is_dev_challenge: false
published_at: '2023-07-20T03:32:29Z'
reactions: 2
reading_time_minutes: 4
tags:
- neo4j
- datascience
- openai
- nocode
title: 🗣️🤖 Ask to your Neo4J knowledge base in NLP & get KPIs
url: https://dev.to/optnc/ask-to-your-neo4j-knowledge-base-in-nlp-get-kpis-5ebd
---

## 🤔 Food for thought

With this content we'll start to uncover a fascinating subject, which is:

> The **cost/value balance of a question/answer**... and "the illusion of gratuitousness"

As you will see, `AI` (and especially `AGI`) throws a lot of worries about [task encroachment](https://www.oecd-ilibrary.org/sites/e39255bb-en/index.html?itemId=/content/component/e39255bb-en)... but also helps challenging **deep questions about what is the ratio between cost & intelligence**, the impact it does already have on our collaborations... and most important :

> _"How we join our intelligence and creativity **into a hybrid Humain/AI taskforce**?"_

## 🗞️ `Neo4j`, `LLMs` and data

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/14elqw7s1o53t98su5zm.png)
](https://neo4j.com/generativeai/)

In this context no-code integration has landed on [NeoDash](https://neo4j.com/labs/neodash/):

{% twitter 1678866394480525314 %}

This post will show up:

- 🧐 **Why** it matters
- 🎯 **What** can be achieved with this new feature (and its potential impact on our organizations & workflows)


## 🚼 How it works

Before going further, we need to understand that all that we are going to do is: 

1. **Ask a question** in [`NLP`](https://en.wikipedia.org/wiki/Natural_language_processing) (in english for now)
2. **Call openai's LLM API to query meta graph** [`APOC`](https://neo4j.com/labs/apoc/) and build the `cypher` query
3. **Get** the `cypher` (the query)
4. **Locally run** the cypher against the data
5. Customize **reports**

## 🤔 Questions

On your **daily activities**, you may be challenged by the following kind of questions that _look like (ie. follow the same pattern)_ : 

- **How many** GitHub users do we have ? (as it **involves costs**)
- **Who are the people** managed by `Mr X`  ?
- **How many** GitHub repositories does `Team X` maintain ? (involves **capacity to maintain a set of services**)
- **How many** virtual machine do we have ? (**involves size of infrastructures and then costs,...**)
- **How much** do we spend on...
- etc...

👉 Therefore we built an **omniscient knowledge graph that is able to answer a very wide amount of questions about our organization.**

Below some zoom-in into graph topology, so you (as well as the `LLM` we will use later) can **understand how to deal with data**:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a46ydaavata3qr48kalj.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nq5h47fzi9xl5j9qo200.png)

Now we are able to **transform a question into a dashboard widget:**

{% twitter 1679730751934464000 %}

## 🍿 Demo

{% youtube hq_ZvUTCRWQ %}

## ⚖️ Further on strategies

With that first experimentation started to appear new kind of concerns, in particular the following one:

> "A big omniscient giant vs. a myriad of little agents equipped of custom tools."

This section is dedicated to **very briefly summarize these questions** so we can talk about them and optimize the design of our solutions, the way we could manage & answer incoming questions... and **most of our own learning path** so we can delegate automated tasks to AI and...

> **focus on the ones that can't or are not yet automated.**

## 💰 Benefits

As a matter of fact, pretty shortly you're willing to automate questions answering tasks and re-invest that time.

In short:

- 🔗‍💥 People don't wait answers from your part : **they go faster with more freedom**, they don't make issues, etc...
- 🧑‍🚀 You can focus on higher value added activities : **you go further and faster & gain in expertise**


### 📊 NO-Code `Neodash`

- No **skill** required
- **Plug & play** strategy
- Could be quite **expensive during query prototyping** phasis (but keep in mnd that [`OpenAI` is regularly reducing the price of its APIs](https://venturebeat.com/ai/openai-is-reducing-the-price-of-the-gpt-3-api-heres-why-it-matters/) while improving them)
- Put in evidence that **"_Time is money_"**
- **Remove the data guys from a potential bottleneck** situations where people expect them to produce more knowledge at a faster pace
- Very convenient to **prototype**
- Great for high level questions and **technically affordable by non-tech people** (which sets them free)
- **No need to know the knowledge** graph design
- **`100%` AI driven** and meta-schema driven
- Prone to make misunderstandings and `cypher` error generation **(beware of large contexts, see below)** and adequate `LLM` model setup

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3hdd3rqq5p9g8gh4wxgq.png)

### 🦜🔗 `Langchain` & custom tools

[Langchain](https://github.com/hwchase17/langchain) and the implementation of [Custom Tools](https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools) also is a great (and very efficient) way to **setup a dedicated Q&A (for example for chat purpose) agent**.

Here are some few points to consider:

- **Skills required** for implementation
- Requires to **know a preset of questions**
- Could fall back to the global approach when the chain is not able to find the answser...  simply throw _"I'm sorry, but with my current toolset, I was not able to find a suitable answer."_

That's all for now, hopefully you'll have found this content useful and made you consider new use cases around AI adoption.

## 📘 Book

Last but not least, reading this book also highly helped considerate new way of thinking the work itself and prepare the ~~future~~ present:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/htndir8yr347kt4wqqo6.png)](https://www.goodreads.com/book/show/51300408-a-world-without-work)