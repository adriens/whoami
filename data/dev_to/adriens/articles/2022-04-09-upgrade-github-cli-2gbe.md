---
comments: 0
id: 1049553
is_dev_challenge: false
published_at: '2022-04-09T00:10:16Z'
reactions: 10
reading_time_minutes: 1
tags:
- github
- git
- productivity
- cli
title: ⬆️ Upgrade GitHub cli
url: https://dev.to/optnc/upgrade-github-cli-2gbe
---

## ❔ About `cli/cli`

GitHub focuses more and more its users productivity and [`UX`](https://en.wikipedia.org/wiki/User_experience).

Target audience are : 

- Programmers/people making code (DEV, OPS, SECOPS, Network, DevSecOPS,..),
- Team Managers,
- SCRUM Masters,
- Product Owners,
- Security managers (see [organization-level security manager role](https://github.blog/changelog/2021-10-21-introducing-the-organization-level-security-manager-role/)),
- DEVOPS engineers,

, ... and more generally **every person how is engaged on the software creation, delivery and deployment pipeline.**

To make `userexperience` always better they have released a dedicated cli : `cli/cli/` :

{% github cli/cli %}


In addition to traditional `git` operations, you can smoothely interact on an - everyday - [growing set of GitHub features](https://cli.github.com/manual/).

## 🆙 Stay up-to-date

As any other software and as it is also maintained by an ever growing [programmers community](https://github.com/cli/cli/graphs/contributors), `cli/cli` is often [released](https://github.com/cli/cli/releases).

Hence you often have to upgrade (the cli warns you about new release availability).

Fortunately it is distributed through [`brew`](https://brew.sh/) wich makes uprgade process a real piece of cake

> ... making it possible to enjoy new features very easily.

## 🎬 Upgrade demo

To upgrade things are a easy as :

```shell
brew upgrade gh  
```

See below how to upgrade (`v2.6.0` to [`v2.7.0`](https://github.com/cli/cli/releases/tag/v2.7.0) in my case):

{% youtube 3c7vj5cuYoY %}


## 🔖 `cli/cli` Homepage

For more about that tool, just visit its homepage :

{% embed https://cli.github.com/ %}