---
comments: 14
id: 1244289
is_dev_challenge: false
published_at: '2022-12-14T06:24:50Z'
reactions: 16
reading_time_minutes: 3
tags:
- showdev
- security
- api
- opensource
title: ⌛ Manage EoLs like a boss with endoflife.date 🛑
url: https://dev.to/adriens/manage-eols-like-a-boss-with-endoflifedate-2ikf
---

## ❔ About

Product lifecycle, `EoL` (End of Life) and more generally obsolescence is a very hot topic for both :

- 🛡️ **Security**
- 🤗 Customer & Developer **Experience**
- ⌛ Durable **time to market** performances

Still,... managing these can be a tedious activity... and it's not always as easy to at least manage that, have metrics.

## 👉 What you'll learn

This post will introduce you a **very concrete _API driven_ approach that makes these data interoperable** (through `APIs`) **so you can build effective dashboard with pretty very few efforts.**

## ❔ `endoflife.date`

[Why `endoflife.date` exists](Why this exists ) :

- EOL and Support information is [often hard to track, or very badly presented](https://twitter.com/captn3m0/status/1110504412064239617)
-All the data is made available using an [easily accessible API](https://endoflife.date/docs/api)
- There are a few tools that use this API: [`norwegianblue`](https://github.com/hugovk/norwegianblue), [`cicada`](https://github.com/mcandre/cicada).
 
## 🍿 Demos

Below are some integrations we cloud do thanks to [`endoflife.date`'s API](https://endoflife.date/docs/api)


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s8xizh7luqhz16ggg2x1.png)](https://endoflife.date/docs/api)


### 😎 Get EOL from your terminal with `eol`

{% youtube ZOoawjzVa0g %}

### 📊 EoL in Neo4J dashboards

After API-driven integrations We could start to implement these kind of dashboards ([Neodash](https://neo4j.com/labs/neodash/))

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/31kxt1tppzmjbvbkobrg.png)

... or visualizations ([Bloom](https://neo4j.com/product/bloom/)): 


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/b1kch97a9m1w8jkfqki6.png)

### 🕹️ "Playing" with dependencies and EoLs

Below, a [demo on neo4J Neodash](https://neo4j.com/labs/neodash/):

{% youtube w9zAWPxMcPk %}

### ♨️ Interact Java EoLs roadmap

Once imported into Neo4J, you can run `cypher` queries:

```cypher
MATCH (m:JavaEOL)
WITH m,
     CASE 
     WHEN date(m.support)> date() THEN 'True'
     ELSE 'False'
     END AS supported 
RETURN supported, 
       count(supported) as total,
       m.cycle as version
ORDER BY supported 
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/shmxh86eiohqn7gwpkmc.png)

### 🕸️ Report apps that rely on deprecated Java

```cypher
MATCH
  (a:Application)-[ra:HAS_GITLAB_REPOSITORY]->(g:GitlabRepository)-[rg:HAS_JAVA_VERSION]->(j:JavaEOL)
WITH a,g,j,

CASE
   WHEN date(j.support) > date()
   THEN 'True'
   ELSE 'False'
END as supported
RETURN supported,
       count(supported) as total,
       a.name as name
ORDER BY supported
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nupxujq2a6jbossjkzhg.png)

## 🧑‍🤝‍🧑 Our contributions (so far)

I have started to contributed to get the best coverage as possible for our current stack so anyone can take benit of it (including ourselves 😅) :

- [Quarkus](https://github.com/endoflife-date/endoflife.date/pull/1800) : see [detailed and dedicated discussion with Quarkus maintainers](https://github.com/quarkusio/quarkus/discussions/29161
)
- [Spring-Boot 3](https://github.com/endoflife-date/endoflife.date/pull/1904)
- [Apache Maven](https://github.com/endoflife-date/endoflife.date/pull/1914)
- [Apache Kafka](https://github.com/endoflife-date/endoflife.date/issues/1930)
- [`JReleaser`](https://github.com/endoflife-date/endoflife.date/pull/1962)
- [OpenSearch](https://github.com/endoflife-date/endoflife.date/pull/1935)
- [`JHipster`](https://github.com/endoflife-date/endoflife.date/pull/1984)
- [`Neo4J`](https://github.com/endoflife-date/endoflife.date/issues/2005)
- [API enhancement](https://github.com/endoflife-date/endoflife.date/issues/1985)
- [`endoflife.date` badges on `Shields.io`](https://github.com/endoflife-date/endoflife.date/issues/2003)
- [Make `endoflife.date` urls nicer to share](https://github.com/endoflife-date/endoflife.date/issues/2007)
- [Data quality enhancement](https://github.com/endoflife-date/endoflife.date/issues/2016)

## 🧰  `cli` Tooling

`eol` CLI to show end-of-life dates for a number of products. : 

You can export EoLs in very various ways (`csv`, `tsv`, `markdown`,...) : 

{% embed https://github.com/hugovk/norwegianblue/issues/110
 %}

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q9xmp0xu5okhlzru2hvf.png)

## 📑 Related tools

- [`endoflife.date`](https://github.com/endoflife-date/endoflife.date) : _Informative site with EoL dates of everything_
- [`cicada`](https://github.com/mcandre/cicada) : _Long Term Support Analyzer_
- [`norwegianblue`](https://github.com/hugovk/norwegianblue) : _CLI to show end-of-life dates for a number of products._