---
comments: 2
id: 1921783
is_dev_challenge: false
published_at: '2024-07-14T22:26:39Z'
reactions: 4
reading_time_minutes: 1
tags:
- devops
- productivity
- automaton
- operations
title: '📦 "OaaS" : A short intro to "Operations as a Service" & its tremendous benefits'
url: https://dev.to/adriens/oaas-a-short-intro-to-operations-as-a-service-its-tremendous-benefits-3h99
---

## 💭 About `OaaS`

How many times did you:

- **🧑‍🎨 As a `DEV`** : to explain a third party how to use a job/task you have developed and delivered in your favorite language on a specific server...**happily & proudly delivered with a wiki page** that explains step by step how to run the task
- **🤔 As an `OPS`** : to discover a long documentation or issue that explains you the 100 steps to achieve to successfully run the task, schedule, monitor and integrate it with the crowd of other jobs you already have to RUN... and what to do and who to call if it fails
- **☎️ As a `hotliner`** : being frustrated to wait for the `OPS` to give you the **`root` access to this damn server so you can reboot a specific service or run `shell` script... and then complaining about their lack of trust.**

**👉 Well, `OaaS` is a way to achieve this : build an end-to-end pipeline so people, within a shared pipeline, can build, share, run, delegate and monitor job executions within an interoperable way.**

Interoperability & uniformity are the key point here, for example to : 

- **Deliver** a clickable button on a web console
- **Configure** a ticket generation in some cases
- **Trigger** a third-party SaaS or non-SaaS webhook
- **Plug-it** into Pagerduty like services in case of failure
- **Let AI agents** call jobs to overcome some incident
- ...

[Rundeck](https://www.rundeck.com/) is a way to achieve this, ie. **to prioritize development/configuration/uniformity** over endless heterogeneous documentations.

## 🎯 Why of this post

The aim of this post is to introduce these aspects with simple & pragmatic concepts.

## 🍿 Demo

{% youtube 3F7njD6ehqM %}