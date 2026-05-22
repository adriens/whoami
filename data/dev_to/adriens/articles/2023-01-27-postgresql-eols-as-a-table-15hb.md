---
comments: 1
id: 1332962
is_dev_challenge: false
published_at: '2023-01-27T02:30:22Z'
reactions: 0
reading_time_minutes: 1
tags:
- cryptocurrency
- blockchain
- discuss
- bitcoin
title: 🐘 PostgreSQL EoLs as a table ⏳
url: https://dev.to/adriens/postgresql-eols-as-a-table-15hb
---

## 🐘 About

When you want to know about [PostgreSQL](https://www.postgresql.org/) [End of Life (EoLs)](https://en.wikipedia.org/wiki/End-of-life_product), you usually start with a [Google Search](https://www.google.com/search?client=firefox-b-lm&q=postgresql+end+of+life) : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/t9azk7mjjcvkzwd1vc54.png)

## 📅 PostgreSQL Versioning Policy 

So you get to the [PostgreSQL Versioning Policy ](https://www.postgresql.org/support/versioning/):

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y9igj22t046o23npf4h8.png)](https://www.postgresql.org/support/versioning/)

☝️ ... but you can't really **interact/play with the underlying data** 😓

## ⏳ `endoflife.date` 

If you go to the dedicated [`endoflife.date`](https://endoflife.date/postgresql) page

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/31seqzr3jzhy8lj6yb0e.png)
](https://endoflife.date/postgresql)

💡... things are getting much much more interesting... especially when you notice the [`api`](https://endoflife.date/docs/api) option 🤔

## 🎯 What ya gonna do

In this post, you'll see how to **load PostgresSQL EoLs data into a regular table**, (almost) only from `psql` commands.

## 🧰 Tools

All you need here is:

- 🐘 A PostgreSQL instance 
- ⛏️ [`httpie`](https://httpie.io/) (or `curl`, ... or `wget`)
- 🪛 [`jq`](https://stedolan.github.io/jq/)
- ⌨️ Any (decent) terminal

## 🌈 Teaser 🐱

At the end of this post, you'll be able to get PostgreSQL EoLs this way:

{% youtube V1wb5dkdAPs %}

## 🎬 Demo

{% youtube LIYfZXC97C8 %}

## 🔖 Resources

{% github https://github.com/adriens/endoflife.date-nested %}

{% twitter 1618371468630560776 %}

# 🎫 Related contents

{% github https://github.com/endoflife-date/endoflife.date/issues/2380 %}