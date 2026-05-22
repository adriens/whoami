---
comments: 2
id: 1784850
is_dev_challenge: false
published_at: '2024-04-02T20:30:36Z'
reactions: 0
reading_time_minutes: 2
tags:
- ai
- datascience
- data
- dataviz
title: 📈 Data-driven strategy automation w/ LIDA
url: https://dev.to/adriens/data-driven-strategy-automation-w-lida-d2j
---

## 🤯 Teaser

Ever wanted to get a **complete analysis of a situation so you can take data-driven decisions** for any domain and **achieve data-analysis...within a few seconds ?**

🫵 Well...I have good news for you, this short post is all about that.

## 🍿 For the inpatients

{% youtube SVIIc0W-8hg %}

## ❔ Inception

Everything started with the following tweet:

{% twitter 1692187646351798485 %}

... talking about a

> _"Systems that support users in the automatic creation of visualizations, [...] understand the semantics of data, enumerate relevant visualization goals and generate visualization specifications."_

I was just wondering how far and how good this could be so I wanted to give it a try on:

- **A very concrete real life** use case,
- **A public Notebook** on a on a public Kaggle Dataset ([🥷 Neo4J Ninjas duckdb dataset 🦆](https://www.kaggle.com/datasets/adriensales/neo4j-ninjas-duckdb-dataset))

## 📜 The analysis workflow 

The analysis workflow is pretty straightforward and can be splitted into two main phasis: preparation then get insights:

1. **🗂️ Pick a dataset** on which your business depends
2. **🧍 Design** a persona (ie. to modelize the business case)
3. **🎯 Ask** for a number of goals
4. **🎯 Get goals** ideas (and detailed explanations) from AI
5. **📊 Get dataviz** from AI
6. **🧠 Analyze** : interact with `LIDA` in a continuous improvement loop (aka. use your own brain to tune persona, dataset,... 😏)

## 🦥 Enjoy goals... as data

It's as simple as setting a number of goals and the target persona:

```python
goals = lida.goals(summary,
                   n=5,# Let's get 5 goals
                   persona="Neo4J community manager who
needs to manage its worldwide community to get the best
community engagement.")
```

Then within less than a second **you get the goals (eventually as a `pandas` dataframe so you can also share goals as a spreadsheet)**:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vvgbinijecdzotleajbs.png)

**🥳 Finally you just have to ask for some dataviz** for any goal:


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lg9gxm5j27r3v9ad9up9.png)


## 📑 Resources

- [🤖😘🥷 Neo4J community manager automation by `LIDA`](https://www.kaggle.com/code/adriensales/neo4j-community-manager-automation-by-lida)
- https://aclanthology.org/2023.acl-demo.11/
- https://github.com/microsoft/lida
- https://microsoft.github.io/lida/
- [LIDA | Automatically Generate Visualization with LLMs | The Future of Data Visualization](https://medium.com/@c17hawke/lida-automatically-generate-visualization-and-with-llms-the-future-of-data-visualization-6bc556876b46)
- [An Overview of LIDA: Generate Visualizations and Infographics of Tabular Data using LLMs!](https://techcommunity.microsoft.com/t5/educator-developer-blog/an-overview-of-lida-generate-visualizations-and-infographics-of/ba-p/4047474)