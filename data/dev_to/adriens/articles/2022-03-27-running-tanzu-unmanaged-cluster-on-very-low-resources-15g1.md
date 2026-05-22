---
comments: 0
id: 1036279
is_dev_challenge: false
published_at: '2022-03-27T23:25:14Z'
reactions: 5
reading_time_minutes: 1
tags:
- kubernetes
- opensource
- devops
- docker
title: Running Tanzu unmanaged cluster on (very) low resources
url: https://dev.to/optnc/running-tanzu-unmanaged-cluster-on-very-low-resources-15g1
---

## 👉 Intro

We currently are evaluating [VM Ware Tanzu Kubernetes cluster](https://twitter.com/vmwaretanzu ) solution.

Fortunately [VM Ware](https://tanzu.vmware.com/) made the choice to get community driven by :

- Making its cluster available for many flavors through its Community Edition called TCE ([Tanzu Community Edition](https://tanzucommunityedition.io/))
- Creating [Carvel Community](https://carvel.dev/) which : 

> _"[...] provides a set of reliable, single-purpose, composable tools that aid in your application building, configuration, and deployment to Kubernetes."_

## ❔ The `unmanaged` cluster

In TCE, VM Ware introduces [TCE Unmanaged Cluster](https://tanzucommunityedition.io/docs/v0.10/ref-unmanaged-cluster/) which makes possible to run Tanzu on low resources envs or on develop environments great to be destroyed/rebuilt for experimental/learning purposes.

So I wanted to challenge TCE on Katacoda to see **how could use it on our workstations**.

> If you manage to make it run on Katacoda (with default low resources) then you can run it on your system.


## 🎞️ Discover TCE

So you can discover how we achieved to get a live TCE running cluster on Katacoda and on which stack it does rely :

{% embed https://youtu.be/GRipRGxR4QY %}

## 🔖 Resources

Play yourself on the [dedicated Katacoda scenario](https://www.katacoda.com/opt-labs/courses/tanzu-community/tce-playground) and stay tuned for more news on that topic :

{% twitter 1505904668584685569 %}