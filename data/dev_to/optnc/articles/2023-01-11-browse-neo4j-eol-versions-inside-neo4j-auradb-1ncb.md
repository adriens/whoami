---
comments: 1
id: 1312604
is_dev_challenge: false
published_at: '2023-01-11T19:29:17Z'
reactions: 0
reading_time_minutes: 2
tags:
- beginners
- typescript
- javascript
title: 🔁 Browse Neo4J EoL versions inside Neo4J AuraDB 🤓
url: https://dev.to/optnc/browse-neo4j-eol-versions-inside-neo4j-auradb-1ncb
---

## ❔ About

Sometimes, you may need to know if the current Neo4J version you are running is up-to-date, **which versions are available**, supported... **or simply if you have the `latest` version of your release so you can achieve maintenance.**

In this post, you'll discover how to achieve this in pure [`Cypher`](https://neo4j.com/developer/cypher/) with the help of [`APOC`](https://neo4j.com/developer/neo4j-apoc/).

To show how easy the process is, we'll do this on [`AuraDB`](https://neo4j.com/cloud/platform/aura-graph-database/), from scratch.

## 🍿 Demo for impatients

{% youtube rpRDstHf-fk %}

## 🕹️ Script time for geeks

```cypher
// Get the current version
call dbms.components() yield name,
  versions,
  edition
unwind versions as version
return name, version, edition;
```


```cypher
// Load all products
CALL apoc.load.json("https://endoflife.date/api/all.json")
  YIELD value
  UNWIND value.result AS product
MERGE (p:EOLProduct {name: product,
  url: 'https://endoflife.date/' + product});

// create unique index
CREATE CONSTRAINT EOL_UNIQUE_PRODUCTS
FOR (p:EOLProduct)
REQUIRE p.product IS UNIQUE;

MATCH (p:EOLProduct) RETURN p;


MATCH (p:EOLProduct) 
  CALL apoc.load.json('https://endoflife.date/api/neo4j.json')
  YIELD value
MERGE (c:EOLCycle {product: p.name,
       cycle: value.cycle,
       eol: value.eol,
       //support: value.support,
       latest: value.latest,
       latestReleaseDate: value.latestReleaseDate,
       releaseDate: value.releaseDate,
       lts: value.lts//link: value.link
       }
       );

// link cycles with products
MATCH
  (c:EOLCycle),
  (p:EOLProduct)
WHERE c.product = p.name
  CREATE (c)-[r:EOL_CYCLE_OF]->(p)
RETURN type(r);
```

... then get releases of `Neo4J` :

```cypher
MATCH (c:EOLCycle)-[r:EOL_CYCLE_OF]->(p:EOLProduct)
  WHERE p.name = 'neo4j'
RETURN c,r,p;
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nc6xn1fk8rs5viclou2t.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mvtks700humzbq3wek2r.png)


## 🔖 Related content

{% embed https://github.com/endoflife-date/endoflife.date/issues/2211 %}