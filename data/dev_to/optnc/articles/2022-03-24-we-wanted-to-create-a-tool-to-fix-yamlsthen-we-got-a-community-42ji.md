---
comments: 0
id: 1029336
is_dev_challenge: false
published_at: '2022-03-24T20:24:28Z'
reactions: 9
reading_time_minutes: 2
tags:
- yaml
- devops
- python
- kubernetes
title: We wanted to create a tool to fix yamls...then we got a community
url: https://dev.to/optnc/we-wanted-to-create-a-tool-to-fix-yamlsthen-we-got-a-community-42ji
---

## 👉 Intro

Recently we built a library that would lint & fix `yamls`, that we also did embed as a Github Action so we could use this tool as part of our CI pipeline : 

{% embed https://dev.to/adriens/let-ci-check-fix-your-yamls-kfa %}

What we did not know at that time is that...

> _that was just the beginning of a journey._

## 📦 Release the `cli`

Progressively we started to focus on `yamlfixer` `cli` user experience, features, packaging and delivery.

So the context slowly started to shift from a background  hidden tool to a full tool, with more features and more integrations.

We started to automate [package delivery on `pypi`](https://pypi.org/project/yamlfixer-opt-nc/), make install process much easier, [create demo scenarios](https://www.katacoda.com/opt-labs/courses/devops-tools/yamlfixer), create [one liners](https://github.com/opt-nc/yamlfixer/blob/main/README.md#-one-liners), [plug into `jq`](https://github.com/opt-nc/yamlfixer/blob/main/README.md#piping-json--summary-through-jq) , plug it into [gomplate template engine](https://github.com/opt-nc/yamlfixer/issues/31), ...integration scenarios and many other exciting things, very efficiently around our Dev & OPS pipeline, all that very naturally.

> While the collaboration through GH issues was fully remote, we even did an internal (30' minutes long) meetup to share about vision and issues.

At the end of the first week I was mesmerized : 

{% embed https://asciinema.org/a/478928 %}

> _we wanted a `cli` tool to fix `yamls` but finally we built a community !_

## 🎞️ Video demo

Find below first live demo video (in French) with a lot of more details about what we did :

{% youtube https://youtu.be/_FiVaMFITkI %}

## 🎬 asciinema demos

Below some dedicated [`asciinema`](https://asciinema.org/) demos :

- [First Kickstart](https://asciinema.org/a/478928)
- [Backup suffix](https://github.com/opt-nc/yamlfixer/issues/70) feature [demo](https://asciinema.org/a/479510)

Feel free to contribute yours on the GH project 👇

## 🧑‍🤝‍🧑 Contributors

Many thanks to the core team I really enjoy working with on a daily basis on many other DevOPS challenges, helping pushing disruptive new ideas :

- 👱‍♀️ [Michèle](https://dev.to/mbarre)
- 🧔‍♂️ [Jérôme](https://github.com/tamere-allo-peter)

## 🔖 Project repo

For more about the project just : 

{% github opt-nc/yamlfixer %}