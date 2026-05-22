---
comments: 1
id: 1377746
is_dev_challenge: false
published_at: '2023-03-01T22:58:36Z'
reactions: 1
reading_time_minutes: 2
tags:
- devops
- security
- docker
- productivity
title: 🔬 Gitlab 15.8 analysis w. endoflife.date, grype, (x)eol 🐋
url: https://dev.to/optnc/gitlab-158-analysis-w-endoflifedate-grype-xeol-24b0
---

## ❔ About

Gitlab recently [released `15.9`](https://github.com/endoflife-date/endoflife.date/pull/2566) version:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z0wq2jo7yj614alxxuxy.png)](https://endoflife.date/gitlab)

This opens a opportunity to take a closer look at upgrade opportunities, security and End of Life concerns **as part of maintenance process.**

> **so we can compare `15.8` w. `15.9` (ie. why we should invest time in upgrading).**

## 🎯 What you'll learn

With this live demo, you will:

- Discover with me (live) [`xeol`](https://github.com/noqcks/xeol)
- See the whole "behind the scene" process of maintenance and documentation process.
- Learn how to produce charts from cli with [`grype-contribs`](https://github.com/opt-nc/grype-contribs) : 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/64t7euzz2cmf0ijmaasj.png)](https://github.com/opt-nc/grype-contribs/blob/main/JQ_TRICKS.md)

... and also deal with very efficient `DEVOPS`/ `DEVSECOPS` tools.

## 🧰 Tools

- [`eol`](https://github.com/hugovk/norwegianblue)
- [`grype`](https://github.com/anchore/grype)
- [`syft`](https://github.com/anchore/syft)
- [`xeol`](https://github.com/noqcks/xeol)
- [`opt-nc/grype-contribs`](https://github.com/opt-nc/grype-contribs)
- [`jq`](https://stedolan.github.io/jq/)

## 👆 (Noobs) Notice about `xeol`

Wthin `xeol`, getting the message:

> "No eol found"

means **everything is fine** for you around end of life cycle management 😅

{% embed https://github.com/noqcks/xeol/issues/38 %}

## 🎞️ (Live) Demo

{% youtube 2tTqo1TZCyA %}

## 💡 `xeol` trick : `--fail-on-eol-found`

We can trigger a fail on `xeol` when an `EOL` is found:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qneknrw3qylb8ea7ew0n.png)](https://github.com/noqcks/xeol/pull/12)

## ♾️ `xeol` GitHub Action

If you want to check `EoLs` as part of the CI, just check this:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vaqj7b0737amol5cxabg.png)](https://github.com/marketplace/actions/xeol-end-of-life-eol-scan)

## 📑 Related stuff

- https://github.com/noqcks/xeol/issues/38
- https://github.com/endoflife-date/endoflife.date/pull/2568
- https://github.com/endoflife-date/endoflife.date/pull/2569