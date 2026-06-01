---
comments: 3
id: 1216113
is_dev_challenge: false
published_at: '2022-10-24T20:29:06Z'
reactions: 5
reading_time_minutes: 1
tags:
- github
- quarkus
- java
- api
title: 🔁 Build & deliver static docs w. Quarkus/Reodcly on GitHub Pages 📘
url: https://dev.to/optnc/build-deliver-static-documentation-w-quarkusreodcly-on-github-pages-4224
---

## ❔ About

Today, **`CD` (Continuous Delivery)** of up-to-date documentation is a crucial step if you want to achieve things at scale.

APIs do not make exception : we deliver embedded swagger, but...

> _**more and more outside collaborators ask for offline documentation, or on API marketplaces.**_


And (hopefully) : 

> _**your outside contributors or clients are more numerous than you.**_

☝️ So you have to deliver them an optimal **`DX`** (Developer-Experience) that costs no work to your organization.

👉 We'll show you how we **deliver documentation** for : 

- 🤓 Human people
- 🤖 Third party CI services for integration purposes


## 💡 What we'll cover

What we'll show here is how we **deliver a static** [OpenAPI specification](https://swagger.io/specification/) (`html` and `yaml`), **as part of the release process**.

👉 With that, it makes it very easy to import your API into any API marketplace, see below on Google [`apigee`](https://cloud.google.com/apigee) :

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/47gqrwcw43x4v4oey08o.png)
](https://cloud.google.com/apigee/docs/api-platform/tutorials/create-api-proxy-openapi-spec)

## 🧰 Stack

- [GitHub Actions](https://github.com/features/actions)
- [GitHub Pages](https://github.blog/2022-08-10-github-pages-now-uses-actions-by-default/)
- [Quarkus](https://quarkus.io/about/)
- [Redocly](https://redocly.com/)

## 🍿 Demo

Enough talks, let's watch this very cool step by step and short (<`10'`) demo from @mbarre :

{% youtube VCphsrYfzak %}

## 🔖 Resources

- [Quarkiverse documentation](https://quarkiverse.github.io/quarkiverse-docs/index/index/index.html)
- [Quarkiverse Hub on GitHub](https://github.com/quarkiverse)

## 📆 Date to save

{% twitter 1583442985647329287 %}