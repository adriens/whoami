---
comments: 6
id: 1423617
is_dev_challenge: false
published_at: '2023-04-05T05:59:02Z'
reactions: 0
reading_time_minutes: 1
tags:
- docker
- datascience
- python
- jupyter
title: 🐋 Effortless Docker images trends on Kaggle 📈
url: https://dev.to/optnc/effortless-docker-images-trends-on-kaggle-5bg
---

## ❔ About

As we are going more and more digital, we rely and release an ever increasing set of artifacts : 

{% twitter 1638339730772316164 %}

... and as we go _cloud native_, docker images are a crucial part of it.

So it makes sense you want to get KPIs about their:

- 📝 **Description** & documentation quality (for better indexation and get traction)
- 📈 **Popularity**

This post is dedicated to this concern, for public images on DockerHub.com.

## 💡 Inception

I recently ran a **manual internal reporting** job on docker images, and I discovered that some of them were lacking descriptions : 


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1wzibmm47qhjd21po4ch.png)

So I wanted, on an automated and daily basis to : 

- 🛑 **Lint images description** : be sure metadatas are properly setup
- 📈 **Get & share KPis** of the images popularity (nb. of downloads/Pulls) 
- 🦥 **Effortless** : get notified as soon a requirements are not met
- 📢 **Share** popularity

👉 Fortunately, DockerHub has a public API so this can be **achieved without too much efforts.**


## 🍿 Demo

{% youtube 2tWFPIPBZM4 %}

## 🔖 Resources

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3neohoz8yds9afxqbnzd.png)
](https://www.kaggle.com/code/optnouvellecaldonie/opt-nc-public-docker-images)