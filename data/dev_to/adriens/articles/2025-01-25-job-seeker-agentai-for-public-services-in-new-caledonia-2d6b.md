---
comments: 9
id: 2223706
is_dev_challenge: true
published_at: '2025-01-25T22:35:01Z'
reactions: 11
reading_time_minutes: 3
tags:
- devchallenge
- agentaichallenge
- ai
- machinelearning
title: 🤖 Job seeker agent.ai for Public Services in New-Caledonia
url: https://dev.to/adriens/job-seeker-agentai-for-public-services-in-new-caledonia-2d6b
---

*This is a submission for the [Agent.ai](https://srv.buysellads.com/ads/long/x/T6EK3TDFTTTTTT6WWB6C5TTTTTTGBRAPKATTTTTTWTFVT7YTTTTTTKPPKJFH4LJNPYYNNSZL2QLCE2DPPQVCEI45GHBT) Challenge: Productivity-Pro Agent ([See Details](https://dev.to/challenges/agentai))*

## ❔ What I Built

Currently, the way to find a job in Public Services in New-Caledonia is a classical form:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9ape205lnswzl580v6eg.png)](https://drhfpnc.gouv.nc/avis-vacances-postes-AVP)

But when I come to look for a job this way:

> _"I'm a full stack developer but also passionate about data-engineering, AI & DEVOPS"_

... things get complicated **- time consuming 😵 -** to find the best possible matches.

## 🎯 Why I built this agent

I built [`New-Caledonia Public Services (DRHFPNC) Job Seeker` Agent](https://agent.ai/agent/jobs-avps-drhfpnc-new-caledonia) to **provide a ready to-use as a service agent that points anyone the best job opportunities according to its skills** or aspirations so they find them & apply to them efficiently without having to crawl pdfs and run many _"legacy searches"_.

## 🔭 Envision and perspectives

- **🗞️ Build a `Job trends` Blog Poster** that makes weekly notes on specific skills and related job opportunities
- **📑 Custom job recommendation team** : a Team that takes in input curriculum/skills from a specific set of sources (curriculum, online linkedIn activity,...) to make dedicated recommendations
- **🌐 Plug it into a team** next to [LinkedIn Profile Analyzer](https://agent.ai/profile/1putsxwtwuuv3p2p)
- **📜  Create an agent that make is possible to put together** all the assesments of a given user

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qbshxrtmxamt9ctf6c90.png)](https://agent.ai/agent/jobs-avps-drhfpnc-new-caledonia)

Then it became public : 

{% twitter 1881560530122572227 %}

## 🍿 End User UX on mobile

Below a demo of the UX from a mobile device:

{% youtube EGiq_P3mD1M %}

## 🔬 How it's built demo

{% youtube jiuVHmZp_Ls %}

## 💬  `Agent.ai` Experience

At first, I watched the video tutorial which took me a very few minutes, then I was ready to go to build the firs version of the agent.

## 🔬 How does it work ?

I have developped and scheduled a Kaggle Notebook : [⚙ Loader Avis de vacances de poste AVPs DRHFPNC](https://www.kaggle.com/code/adriensales/loader-avis-de-vacances-de-poste-avps-drhfpnc) that takes in input an OpenData dataset, performs transformations and as well pushed data into a Github Repo [`adriens/odata-avps-drhfpnc`](https://github.com/adriens/odata-avps-drhfpnc):

{% twitter 1880130238849630557 %}

It pushed [`csv`](https://github.com/adriens/odata-avps-drhfpnc/blob/main/data/avps-drhfpnc-with-headers.csv) files and the [`markdown` version from initial pdf ones](https://github.com/adriens/odata-avps-drhfpnc/tree/main/avps).

For this agent I used the scraping feature of the [raw `csv` file](https://raw.githubusercontent.com/adriens/odata-avps-drhfpnc/refs/heads/main/data/avps-drhfpnc-with-headers.csv) : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/m7wgz55fn4hrbm72s8kb.png)

Then i's just about prompting...


## 🤩 Best agent RUNs

Below some agent analysis that retained my attention:

- [_"I'm a full stack developer but also passionated about dataengineering, ai & DEVOPS"_](https://agent.ai/agent/jobs-avps-drhfpnc-new-caledonia?rid=60a0b658e77d4d808a0f4e520e7cbdcf)
- [_"je suis dans le domaine médical"_](https://agent.ai/agent/jobs-avps-drhfpnc-new-caledonia?rid=995964352d2b4beebc37cfb9a844d3e7)
- [_"Je cherche un emploi dans la comptabilité"_](https://agent.ai/builder/agent/edit?id=axdh4u78tu2kmw7u)
- [_"je suis dans le domaine médical"_](https://agent.ai/agent/jobs-avps-drhfpnc-new-caledonia?rid=800b61af6473428b9af86d1ae073cae5)

## 💡 Making the product better : API automation, datasources,...

{% twitter 1880836261986107488 %}

{% twitter 1881759951095525454 %}

## 📢 Social interactions

{% twitter 1883259568282915046 %}

