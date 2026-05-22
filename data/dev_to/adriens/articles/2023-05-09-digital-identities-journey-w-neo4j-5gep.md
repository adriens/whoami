---
comments: 2
id: 1457897
is_dev_challenge: false
published_at: '2023-05-09T20:01:07Z'
reactions: 0
reading_time_minutes: 1
tags:
- datascience
- neo4j
- productivity
- beginners
title: 🌌 Digital identities journey w. Neo4J
url: https://dev.to/optnc/digital-identities-journey-w-neo4j-5gep
---

## ❔ About

More and more, as digtialization spreads in our organizations, the importance of digital identities becomes every day more crucial for many reasons.

If you add the fact that we rely on hybrid platforms (SaaS & onPrem) and services, at a point in time, you will need to know what a digital identity looks like for :

- 🛡️ **Security** (access management, Active Directory,...) governance
- 💸 **Licences** management
- 🧑‍💼 **HR knowledge** (management, roles, peoples skills balance, prevent mental health issues,...)
- ☁️ Third party **cloud platforms** (eLearning, GitHub, Kaggle, Onlineformapro,...)

👉 This post is about **showing how we implemented this as a data-driven solution with Neo4J and code to answer complex question on our digitalization journey.**

## 🗺️ Digital identity... the data way

To discover what digital entities (current state of the art), we query our Neo4J instance's data with introspection like follows with [`apoc.meta.subGraph`](https://neo4j.com/labs/apoc/4.4/overview/apoc.meta/apoc.meta.subGraph/):

```cypher
CALL apoc.meta.subGraph({
  includeLabels: ["Person",
                  "GhMember",
                  "KaggleMember",
                  "OnlineFormaProUser",
                  "DevToAccount",
                  "SumoAgent",
                  "UO",
                  "CigrefJob"],
  includeRels: []
});
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vl6l285rrtc1b9jrks4a.png)

Now, enought talk, let's see how it looks.

## 📘 The digital identity metagraph

{% youtube 2aMK7LLAv2E %}

## 🧑‍🤝‍🧑 Browse identities & people

{% youtube KWaId5i88Ks %}

## 🔖 Related resources

I hope you enjoyed this content and found inspiration.

For more about our data journey, just watch the dedicated speak at `#NODES22` : 


{% embed https://dev.to/optnc/our-speech-about-it-holism-at-nodes22-1bpl %}