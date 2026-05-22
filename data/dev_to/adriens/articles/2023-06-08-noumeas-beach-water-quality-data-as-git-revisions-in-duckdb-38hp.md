---
comments: 5
id: 1492961
is_dev_challenge: false
published_at: '2023-06-08T01:30:32Z'
reactions: 0
reading_time_minutes: 1
tags:
- python
- datascience
- opendata
- tutorial
title: 🏖️ Noumea's beach water quality data as git revisions, in DuckDb 🦆
url: https://dev.to/adriens/noumeas-beach-water-quality-data-as-git-revisions-in-duckdb-38hp
---

## 🏝️ About

Ever wanted to get your favorite beach's water quality like this : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cwnxe4clkmfz3xqww2jx.png)

With this article you'll learn how I could:

1. **Get** (scrap) the data
2. **Load** data into a database
3. **Backup & export** (`csv` & [`Apache parquet`](https://parquet.apache.org/))
4. **Commit** data to GitHub
5. **Query from any terminal** from `duckdb`

## 🧫 About water quality

{% embed https://la1ere.francetvinfo.fr/nouvellecaledonie/province-sud/noumea/comment-sont-surveillees-les-eaux-de-baignade-a-noumea-1359918.html %}

## 🍿 Demo

{% youtube M9JAPYhNCVs %}

## 🔖 Source code

{% embed https://github.com/adriens/odata-eaux-baignade-noumea %} 
