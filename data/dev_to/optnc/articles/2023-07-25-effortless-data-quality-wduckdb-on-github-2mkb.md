---
comments: 10
id: 1531531
is_dev_challenge: false
published_at: '2023-07-25T06:33:44Z'
reactions: 3
reading_time_minutes: 1
tags:
- duckdb
- githubactions
- data
- automation
title: 🦆 Effortless Data Quality w/duckdb on GitHub ♾️
url: https://dev.to/optnc/effortless-data-quality-wduckdb-on-github-2mkb
---

## 🪝 Teaser (for the impatients)

Do you have a repository that relies on `csv` files... and want to operate:

- 🛡️ **Protect your data** with quality intergrity checks before to _corrupt your data_
- 🔬 **Check data quality** as part of your project lifecycle
- 📊 Get operational **KPIs reporting**
- ♾️ **Automate release process to explain** your contributors what has been achieved
- 📦 **Deliver** data
- 🤯 **Endless** usages

🫵 Don't look further, this sort post will cover all these aspects with a practical and highly understandable workflow.

## 🍿 Demo

Enough talks, let's jump'in:

{% youtube 90RhOdxWNqo %}

## 🦆💻🔁🔧♾️🦆 `opt-nc/setup-duckdb-action`

{% github opt-nc/setup-duckdb-action %}

## 🔭 Further 🎀

Once **CI (Continuous Integration) has been done**... you can also think (without a lot of efforts) **to Deliver that data to third party services, as part of your DEVOPS pipeline.**

A this point I see two easy options:

- Upload to _minio_ [`S3 API` w/ `HTTPS`](https://duckdb.org/docs/extensions/httpfs.html)
- Use [MotherDuck](https://motherduck.com/)

... which make your data available for new usecases, at no additional effort:

{% youtube NQgHrszyQWY %}