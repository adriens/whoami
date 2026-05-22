---
comments: 1
id: 1076839
is_dev_challenge: false
published_at: '2022-05-30T21:53:40Z'
reactions: 5
reading_time_minutes: 1
tags:
- github
- productivity
- tutorial
- api
title: 📅 Manage GitHub milestones from cli
url: https://dev.to/optnc/manage-github-milestones-from-cli-2hkh
---

## ❔ Intro

Recently we needed to load a lot of issues on a given milestone so they could be properly managed and reported.

Issues were coming from a given list. Manual process was very time consuming... so we wondered how we could achieve this in a much more efficient way, from shell and cli commands.

This short post is about that and shows what kind of things can be achieved with [GitHub Cli](https://cli.github.com/)... and especially how [`cli/cli`](https://github.com/cli/cli) can be used with [`gh api`](https://cli.github.com/manual/gh_api) calls.

## 🎬 Démo

{% youtube wWyUDkghFZI %}

## 🔖 More about GH API

Delopers make feedbacks... and as you can see it below Github is

> _"committed to making it trustworthy, easy to find, and easy to use."_

{% twitter 1529140169185665026 %}

## 🔖 Gist


{% embed https://gist.github.com/adriens/5a66c2aad305b6da7f3a8f7271e6f42d %}