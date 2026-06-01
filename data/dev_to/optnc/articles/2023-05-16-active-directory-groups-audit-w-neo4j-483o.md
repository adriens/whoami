---
comments: 1
id: 1451829
is_dev_challenge: false
published_at: '2023-05-16T00:18:33Z'
reactions: 1
reading_time_minutes: 2
tags:
- neo4j
- datascience
- security
- devops
title: 🕵️ Active Directory Groups audit w. Neo4J
url: https://dev.to/optnc/active-directory-groups-audit-w-neo4j-483o
---

## 🧐 About

Active Directory is a crucial part of many Information Systems as it manages both **authentication and access management.**

In this article, we'll **focus on Active Directory group management** analysis.

## 🍿 Demo

{% youtube 4LCZbkkCyfQ %}

## 💰 Return On Investment

With this data, we are now able to :

- 📏 Produce **classification**
- 🔮 Make **predictions**
- 🕸️ Cross checking with **third party identity management services**

## 🔭 Further with groups 

We will **link these datas** (ie. relationships) on top of our our digital identity  management, see below:

{% embed https://dev.to/optnc/digital-identities-journey-w-neo4j-5gep %}

## 💡 Group tuning & _Minimum spanning tree_

Having large set of groups **has impacts on performances**. Getting this data as a graph makes it possible to **use graph algorithms** to see if we can improve group assignment design thanks to [Minimum spanning tree](https://neo4j.com/docs/graph-data-science/current/algorithms/minimum-weight-spanning-tree/).

## 📷 Screenshots gallery

We often ask ourselves the same questions
Below some still screenshots of our experience:

### 🔬 Drilling down into someone's groups

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/agv38o8f2c9sq95alfx0.png)

### ⚖️ Member & Guest accounts

> Guest users have default restricted directory permissions. They can manage their own profile, change their own password, and retrieve some information about other users, groups, and apps. However, they can't read all directory information. B2B guest users are not supported in Microsoft Teams shared channels.

Let's see how they are implemented:

```cypher
// Groupes dont les 2 agents et les 2 guests du GLIA sont membres
MATCH (a:AD_agent {name:"3004XXX"})-[ia:IS_MEMBER_OF]->(g:AD_group)
<-[ig:IS_MEMBER_OF]-(b:AD_agent {name:"2999XXX"})
OPTIONAL MATCH (gu:AD_guest {name:"pXXX"})-[ip:IS_MEMBER_OF]->(g)
OPTIONAL MATCH (gue:AD_guest {name:"dXXX"})-[id:IS_MEMBER_OF]->(g)
RETURN a,g,b,gu,gue,ia,ig,ip,id
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8s6llx1y9ecnf11q303x.png)

### 🐘 Biggest groups

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h1zagri685wfwq5qdqry.png)

### 🏋️‍♂️ Account having the largest amount of groups

Getting a large amount of groups can mean many things, so being able to analyze this is worth taking a glance:
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9cl3hks8fn726xdlhb4a.png)