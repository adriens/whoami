---
comments: 7
id: 1080390
is_dev_challenge: false
published_at: '2022-05-16T21:01:06Z'
reactions: 0
reading_time_minutes: 2
tags:
- github
- documentation
- redocly
- devops
title: 📜 API Documentation release automation with Github, redocly and Open API 🦾
url: https://dev.to/optnc/api-documentation-release-automation-with-github-redocly-and-open-api-f6h
---

## 💡 Inception

I truly ❤️ the way [Forem](https://forem.dev/) manages its community by providing ready to use resources to help make things possible.

Their [way of achieving documentation](https://developers.forem.com/api) really impressed me, see by yourself :

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yf2hccq37lzylkfqth6g.png)](https://developers.forem.com/api#tag/articles)
 
> So I wanted to offer the same comfort to the users of the APIs we create & maintain

👉 **This post is about how we achieved that as part of our maintenance & release process.**

## ❔ Intro

Pretty often, people ask you for API documentation. Most of the time you have a live and running Swagger interface (aka. [`Swagger UI`](https://swagger.io/tools/swagger-ui/)), but..

> when you have onPrem APIs, some people may not have access to an up-to-date documentation.

This post will show how we did achieve this on one of our APIs : domaine-nc-api.


## 📝 Ways of releasing documentation

Below are some ways to achieve and access documentation :

- Live & running [Swagger](https://swagger.io/) instance
- Swagger from running Docker (public images) instance, see [`optnc/domaine-nc-api`](https://hub.docker.com/r/optnc/domaine-nc-api)
- API Marketplace like [our API Marketplace on RapidAPI](https://rapidapi.com/opt-nc-opt-nc-default/api/domaine-nc/)
- Static [openAPI](https://spec.openapis.org/oas/v3.1.0) `yaml` exports
- Static web documentation (achieved thanks to [redocly](https://redocly.com/))

☝️ To achieve all this work, we are using Continuous Integrations, with [GitHub Action](https://github.com/features/actions) **so the job is done as part of the release process.**


## 🍿 Démo

With the following demo you'll discover live how we achieve the whole maintenance & release process to achieve all these tasks 👇

{% youtube 4eNz5qHGnEY %}

## 🔖 Related contents

{% embed https://dev.to/optnc/avoid-domain-name-expiration-with-gh-actions-issues-rapidapi-24 %}

{% embed https://dev.to/optnc/dependency-management-automation-with-dependabot-3l62 %}

{% embed https://dev.to/optnc/domainenc-the-fun-docker-way-and-screenshots-contest-17o8 %}
