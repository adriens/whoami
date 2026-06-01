---
comments: 1
id: 1063330
is_dev_challenge: false
published_at: '2022-05-03T07:29:41Z'
reactions: 4
reading_time_minutes: 2
tags:
- api
- githubaction
- cloud
- rapidapi
title: 🦾 Avoid domain name expiration with GH Actions , issues & RapidAPI 🎫
url: https://dev.to/optnc/avoid-domain-name-expiration-with-gh-actions-issues-rapidapi-24
---

## ❔ About

We are managing a website dedicated to domain names management (see [`DOMAINE.NC`](https://www.domaine.nc/)).

Some months ago we faced a incident due to domain name expiration.
The impact on the business is pretty simple 👇

> your domain is simply disappearing from the web (no more ads nor transaction revenue, no more service, SLA impacts, potential penalties,...) 😱

At that time I said myself... then to my team that we absolutely had to

> _create something that would help anyone avoid that incident so **noone should see anymore that kind of service outage**_

## 💡 The Pitch

> **_"We need to get a solution that warns us before domain name expiration by sending a pluggable event/notification."_**

## 🧰 Our toolbox

Previously we had created an API to interact with _domain names in New-Caledonia_.

It is available under various flavours : 

- As a public docker image : [`optnc/domaine-nc-api`](https://hub.docker.com/r/optnc/domaine-nc-api)
- On our [marketplace on RapidAPI](https://rapidapi.com/opt-nc-opt-nc-default/api/domaine-nc/)

So thanks to this, we wanted to apply  [“dogfooding”](https://deviq.com/practices/dogfooding) practice.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7sortd28o7fg049rie0w.png)
 
We will 

> create a ready to use cloud based solution so we could monitor our own domains.

## 🛎️ Deliver a ready to use solution

I was still remembering of "2021 GitHub Actions Hackathon on DEV" :

{% embed https://dev.to/devteam/join-us-for-the-2021-github-actions-hackathon-on-dev-4hn4 %}

Github actions are **an efficient way to get the Job done** and take advantage of all GH (ready to use) integrations around issues.

So...

> we would create a **public GH Action** that would do the monitoring for us... making it possible to **automate backoffice tasks** (Power Automate, Zapier or IFTTT) : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5r0p7o29y0leoaa1g2jq.png)

☝️ **The GH action is relying on the API delivered through RapidAPI, so the only thing you have to do is bring your own [RapidAPI key](https://docs.rapidapi.com/v2.0/docs/keys) so you can store it as a secret on your GH repo**

## 🎬 Live demo

Enjoy the demo of the solution and how to customize it :

{% youtube x4GhCnyJ_DY %}

## 📜 Source code

Find below GH Action source code :

{% embed https://github.com/opt-nc/domaine-nc-action %}

... and finally the [Action on the Marketplace](https://github.com/marketplace/actions/get-your-nc-domain-validity-metadata).



## 🔖 Related contents

Previous related POST : 

{% embed https://dev.to/optnc/domainenc-the-fun-docker-way-and-screenshots-contest-17o8 %}

API on [RapidAPI marketplace](https://rapidapi.com/opt-nc-opt-nc-default/api/domaine-nc/) :

[
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hbndfi3zvwqr3j3hm6f1.png)](https://rapidapi.com/opt-nc-opt-nc-default/api/domaine-nc/)