---
comments: 2
id: 1922890
is_dev_challenge: false
published_at: '2024-07-22T20:58:14Z'
reactions: 0
reading_time_minutes: 2
tags:
- database
- dataengineering
- devops
- eventdriven
title: '🪄 Debezium: the magic behind data capture & async replication (for free)'
url: https://dev.to/adriens/debezium-the-magic-behind-data-capture-async-replication-for-free-355m
---

## 🪝 Teaser

Did you ever find yourself in a situation where : 

- **Team 🇦 pushes data** in a given database (let's say MySQL,...) with its very own custom software
- **Team 🇧 needs to get these data changes** (`INSERT`, `UPDATE`, `DELETE`) as events so they can put them in  let's say... an another database (MariaDB, PostgreSQL,...)
- **Base software** cannot be changed : you have to _"deal with it"_

Eg, team B's motivation maybe to achieve datascience, RealTime Analytics, store in a datalake,...

**👉 This blog post is dedicated to this case... and surprisingly : open source solutions do exist to achieve this magic!**


## 🤔 About the "why"

[`Debezium` Project](https://x.com/debezium)'s "why" is pretty straightforward : 

> "Turn your databases into change event streams"

... even for "legacy" like systems:

{% twitter 1808144012127171020 %}

## 👂 How it does NOT work (why it's awesome)

The key thing here to remind is that **Debezium does NOT act as a proxy in front of the database**, and that's the most elegant part.

The key point is that **Debezium is literally listening to database changes**, whatever you call them : 

- [MySql](https://debezium.io/documentation/reference/2.7/connectors/mysql.html) `binlog`
- [MariaDB](https://debezium.io/documentation/reference/2.7/connectors/mariadb.html )
- [PostgreSQL](https://debezium.io/documentation/reference/2.7/connectors/postgresql.html) `WAL`s for 
- [Oracle](https://debezium.io/documentation/reference/2.7/connectors/oracle.html) `archivelog`
- ...

, then send these events in a common standard format into Kafka messages... waiting to be used later by one or many consumers.

## 🪄 How it works

The magic resides in the following workflow : 

1. **Capture data changes** at the database level (`WAL` for postgres, archivelogs, whatever you call them...)
2. **Send/Stream events** to Kafka
3. **Consume Kafka events** so they they can be pushed to any third party data service
3'. [JDBC](https://debezium.io/documentation/reference/2.7/connectors/jdbc.html) : for example _"consume events from multiple source topics, and then rite those events to a relational database by using a JDBC driver."_

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v0e3bzqsagfviayyjgmi.gif)

## 🍿 Demo from scratch

Below the live demo I was able to do, from scratch, but by following default instructions for a MySQL instance : 

{% youtube vxP2EBGwpv0 %}

## 🔭 Going further

- [Hands-On Guide: Implementing Debezium for PostgreSQL to Kafka Integration](https://dev.to/gouthamsayee/debezium-implementation-in-postgres-2fjd)
