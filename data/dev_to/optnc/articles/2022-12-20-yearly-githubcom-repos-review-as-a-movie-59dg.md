---
comments: 1
id: 1298835
is_dev_challenge: false
published_at: '2022-12-20T06:22:42Z'
reactions: 1
reading_time_minutes: 2
tags:
- github
- datascience
- showdev
- management
title: 🏎️ Yearly GitHub.com repos review (as a movie) 📽️
url: https://dev.to/optnc/yearly-githubcom-repos-review-as-a-movie-59dg
---

## 🎯 About this series

What you'll discover in this series is **the knowledge we got by working on the data** our activity did generate on GitHub.com, only by using its [(always richer) set of APIs](https://docs.github.com/en/rest/issues?apiVersion=2022-11-28).

## ❔ Intro

GitHub.com is a complete platform on which people :

- 🧑‍🤝‍🧑 Build & **socialize** around code
- 🎁 **Contribute**
- 📅 Manage **projects**
- 📦 **Deliver** software
- 🚀 Trigger **deployments**

**Each of these activities generate structured data** that describe what you did, when, with who... and (hopefully 😅) why.

Some reporting is already delivered through charts by GitHub:


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r7lfsnts4ro6eaunlsaf.png)

... but sometimes you can be challenged by many questions, including (but not only) one of the most crucial one : 

> _"How much time (and where) do you spend on `BUILD` vs. `RUN`"_

or this one:

> _"You talk about BOTs and third party services... but how can you tell me more about the ROI ... and how it helps achieve more things ?")_

👉 **In this episode**, we'll only **focus on reporting which repositories have been the most active** during the past year... through a **format anyone can immediately understand.**

## 🍿 Demo

The **chart race of the most active repositories**, based on issues activity :

{% youtube aFtJx-dEqug %}

## 🧰 Stack

Here is the flow we used to produce the content :

1️⃣ Dump GitHub issues to `csv` with Python [`invoke`](https://www.pyinvoke.org/) tasks
2️⃣ Use [`Jupyter Notebook`](https://jupyter.org/)
3️⃣ Generate Race Chart with [`Bar Chart Race`](https://www.dexplo.org/bar_chart_race/)

## 💰 Benefits

By a **single movie** we could show how our most trendy activity evolved over the months since our migration from onPrem GitLab to GitHub.com... without having ever asked anyone to fill a single timesheet. 😅