---
comments: 3
id: 1389559
is_dev_challenge: false
published_at: '2023-03-06T04:20:02Z'
reactions: 1
reading_time_minutes: 1
tags:
- datascience
- kaggle
- python
- api
title: 🦆 From API to scheduled offline copies with DuckDB on Kaggle ♾️
url: https://dev.to/adriens/from-api-to-scheduled-offline-copies-with-kaggle-duckdb-an
---

## ❔ About

While I was working on [`endoflife.date`](https://endoflife.date/) integrations, the need for offline copy started to raise:

{% github https://github.com/endoflife-date/endoflife.date/issues/2530 %}

After some various attempts, I finally found a [Kaggle](https://www.kaggle.com/) based solution.

I wanted the data to:

- 👐 Be easy to share
- ✅ Rely on the official API
- 🔁 Up-to date (without any effort)
- 🔗 Easy to integrate with third party products
- 🧑‍🔬 Be deployed on a datacentric/datascience platform
- 🤓 Show source code (Open Source)
- 🚀 Be easily extensible

Therefore I created a [Notebook](https://www.kaggle.com/getting-started/270972) that does the following things once a week: 

1. **Queries** the API
2. **Load & store** data in a DuckDb database
3. **Export** resulting database in `sql` an `csv`
4. **Export** database a [`Apache Parquet`](https://parquet.apache.org/) files

## 🧰 Tools

All you need is Python and DuckDB `json` functions:

{% embed https://duckdb.org/docs/extensions/json.html %}

## 🎯 Result

As you can see, for now, the only input is the [API](https://endoflife.date/docs/api):


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jleq47jjipmcfb7pt08m.png)](https://www.kaggle.com/code/adriensales/endoflife-date-offline-copy/input)

... while we have fresh output files:
[
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vh9ytr3667o3b9yirdk2.png)](https://www.kaggle.com/code/adriensales/endoflife-date-offline-copy/output)

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gr31atneecbvhqxpv9da.png)](https://www.kaggle.com/code/adriensales/endoflife-date-offline-copy/)


## 🗣️ Conclusion

Finally I delivered the following solution to the community:

{% github https://github.com/endoflife-date/endoflife.date/issues/2633 %}