---
comments: 1
id: 1150431
is_dev_challenge: false
published_at: '2022-07-31T20:56:26Z'
reactions: 2
reading_time_minutes: 9
tags:
- neo4j
- datascience
- algorithms
- dataviz
title: 🗺️ Delivering Information System cartography as a Graph with Neo4J
url: https://dev.to/optnc/delivering-information-system-cartography-as-a-graph-with-neo4j-5bhl
---

## 🗣️ Pitch

As Information Systems grow everyday faster and get even more decentralized and hybrid, **getting an up-to-date System Mapping becomes an always hotter and strategic topic.**

There are ready to use softwares to achieve that kind of goals, still sometimes, you need to achieve that kind of goal in a very short time... and at no cost (this is the tricky part).

This article will show you such an approach :

- highly customizable
- natively interoperable through APIs (`REST`, `graphql`) and SDKs (Java, js, Python, ...)
- deliverable through thanks to easy to classic DevOPS pipelines

## ❔ Intro

 This is the fact :

> _"few people want to maintain that kind of mapping... yet most of us need to get that knowledge"_

...a few minutes after a question has been asked. So the question maybe :

> _"how to empower people so they can answer by themselves to their own questions ?"_

## 🙀 The hot questions

Some of the most frequent questions I got in my daily experience are :

- What happens if this service or **middleware is down or broken** ?
- Does my HA (High Availability) application exclusively rely on high availability services ? (Please say yes, and if not tell me why)
- I see that these services rely on each others : why do they as they should not ?!
- Who does consume this service ? For what purpose ?!
- Who are the people maintaining this chain of services ? I need to talk to them.

👉 The first thing to notice is that all these questions are in fact **relying on data considerations, and meta-datas, not more, not less.** 

We would like to

> _"answer these questions with data, and hence : they should be formulated as queries (not tickets nor meetings, nor manually maintained wikis)."_

## 🔭 The vision

 So... What if you were

> _"considering Information System as a Social Network were people would be services or middlewares ?"_ 

Finally, one day, I got it:

> _"I wanted to get the "Facebook of our services"... and I wanted it now !"_

## 🙋 Answering the question with data structures

Once the question is properly set (sorry I have a math background), it suddenly appears quite evident that the answer to these questions is a graph where **relation between a wide variety of objects occurs.**

I previously did some data story telling on Neo4J, on a large variety of custom datasets like : 

- [books](https://www.linkedin.com/pulse/l%C3%B4%C3%B4%C3%B4ngin-cest-qui-quest-au-centre-de-la-bd-%C3%A0-nous-brousse-sales/)
- [PostgreSQL relational schema metadatas](https://www.linkedin.com/pulse/digging-mining-datas-structures-extracting-from-neo4j-adrien-sales/)
- [mathematical conjectures](https://dev.to/adriens/about-the-collatz-conjecture-neo4j-cypher-184h)
- [identity providers](https://www.linkedin.com/pulse/cloud-authentication-providers-cambridge-analytica-what-adrien-sales/)
- [cooking recipes](https://www.linkedin.com/pulse/non-le-basilic-nest-pas-au-centre-de-la-cuisine-ni%C3%A7oise-adrien-sales/)

A playground to which

> _"I wanted now to add the Information System mapping."_

## 🚀 Kick Off

The first goal I wanted to achieve was to be able to answer all the questions that were around my department (and keep track of them). **That would be my MVP** : and this is how I pitched it to my team.

The first thing to do would be able to deliver a runnable solution within 3 weeks to our CIO... Considering that we were not 100% available to that, we needed to collaborate together in an efficient way, ... the DevOPS way, then on Git. I would evangelize core Neo4J concepts and a very core yet usable version.

I could build the very first core concept and its deployment guidelines within less than 4 hours.

## 🧑‍🎓 Neo4J basics

Neo4J relies on graph theory, we have two kind of objects :

 - [Nodes](https://neo4j.com/docs/getting-started/current/graphdb-concepts/#graphdb-node)
 - [Relationships](https://neo4j.com/docs/getting-started/current/graphdb-concepts/#graphdb-relationship)

In our case :

- **Nodes** will be information system objects (services, middlewares, people or Organizational Units,....)... and they have properties
- **Relationships** will be the relationships between them (a services relies on an another one, someone maintains an application, someone manages someone, etc...)

Once that in mind, as a starter we built `csv` files, **one by kind of node, and one by kind of relationship.** That's all : [KISS](https://en.wikipedia.org/wiki/KISS_principle) (Keep It Simple Stupid).

As you can very [easily load `csv` files in Neo4J](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/), you can then feed your database in one shot with a few lines of cypher code :

Loading a collection of nodes becomes :

```
LOAD CSV WITH HEADERS
FROM 'file:///node_kafka_consumer.csv' AS lin
CREATE (:KConsumer {id_consumer: line.id_consumer,
    name:line.name,
    url_doc: line.url_doc,
    url_git: line.url_git}
    );
```

Then set nodes as `uniques` :

```
CREATE CONSTRAINT UniqueKConsumer
ON (p:KConsumer)
ASSERT p.id_consumer IS UNIQUE;
```

While loading relationship between two nodes becomes :

```
LOAD CSV WITH HEADERS FROM "file:///relationship_consumer_topic.csv" AS row
MATCH (c:KConsumer), (t:KTopic)
WHERE
  c.id_consumer = row.id_consumer AND
  t.id_topic = row.id_topic

CREATE (c)-[r:CONSUMES]->(t)
RETURN r;
```

Once all entities are loaded, just let Neo4J engine do the job, for example by [drawing you the metamodel of your map](https://neo4j-contrib.github.io/neo4j-apoc-procedures/3.5/schema/meta-graph/),

> _"putting in evidence how objects are intended to interact with each others, straight out of the data."_ 

See below [Bloom](https://neo4j.com/product/bloom/) visualization which shows applications, people, Kafka topic/consumers and producers, middlewares :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o4v3h8m33xu8so5xchrf.png)

Admit it : this is probably the first time you see your Information System like that. What is nice with that is that

> _"it's all made through data introspection."_ 

Now that you have the meta-graph, you can perform cypher queries and answer questions, for example visually discover how people and services are relying on one of your services, or discover and report Single Point Of Failure :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qjy9pdbx8kl0ityyl954.png)

The nice thing is that you can play and interact with them, get properties, links to resources (Git repo, Wiki links and so many things). In a word,

> _"you can touch your Information System cartography"_

## 🧑‍🤝‍🧑 Information System Mapping KickOff

 Once we had this first "draft", we could start to enjoy with it... and a lot of great stuff started to happen.

The most exciting thing was that

> _"people started to talk together about these datas like they never did before."_

## 📖 And now... Data story telling !

As part of the first demo, we did live exploration on the previous case. While clicking and opening new relationships and drilling down in the Information System, people started to ask new kind of questions while getting answers in the next second.

At that time I started to introduce how the data-scientist could hold that role.

Some could not hide their surprises :

> _"Is it normal that so many things rely on that node ? Is it in HA ? What if..."_

## ➰ Mapping as part of daily `RUN` tasks

As soon as we had put all that in data, on a git repo, we started to **add items on a regular basis** : each opportunity was caught and transformed in a dedicated issue that was fixed thanks to a Pull Request, a code Review, then a merge on the main branch.

> _"That activity became part of our daily routines."_ 

Very quicly we had the following exciting interaction pattern with other teams :

- _"Hey, could I submit you come code so I can get my app in your mapping ? I have a project kickoff and I'd like to introduce it with that kind of nice looking dataviz"_
- _"Sure. Take a look at the README.md, drop us a dedicated issue, then a related PR on a dedicated branch, once reviewed, it will be merged._

## 🛍️ Contributors & documentation for free

Our audience started to grow very quickly because of the visual impact : **soon non developer people wanted to get the live mapping on their own workstation.**

- _"Can we have an install party together so I can get it up and running on my laptop, I'll create a documentation with screenshots so everyone like me could get it even if we don't have programmer skills"_
- _"Sure, le'ts do this next week, I'll show you how you'll be able to contribute your documentation to the our repository"_

## 🕸️ Integration(s) 💰

Some asked if it would be possible to load that in more traditional middlewares like [PostgreSQL](https://www.postgresql.org/docs/current/sql-copy.html) or [Elasticsearch](https://www.elastic.co/guide/en/logstash/current/plugins-filters-csv.html) to achieve other custom goals.

As our `csv` are [very clean](https://datatracker.ietf.org/doc/html/rfc4180) (meeting [Github csv compliance rules](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#rendering-csv-and-tsv-data)), versionned and normalized, I could answer yes with confidence and

> _"get some more contributions around our work, which made our ROI even greater."_ 

## 🤖 AI & Applied Data Science 🧠

Today, a lot of people talk about `#datascience`. Thanks to the architecture of the solution, you can ask datascientists for help, perform audit, for example to discover well-known or hidden patterns in the topology of your information system, predict relationships, detect regressions and so many possibilities offered by data science.

> _"The more skills you'll have on data science around you, the better you'll master your information system mapping, the better you'll be."_ 

Also, Neo4J has a dedicated [Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/) that helps you detect : 

- loops,
- topological structures (ex : if two nodes are connected or not)
- perform predictions,
- ...

Learn more about these kind of features below :

{% embed https://dev.to/adriens/about-the-collatz-conjecture-neo4j-cypher-184h %}

## 🏭 Industralization

With very few efforts regarding to the benefits, still some questions were coming : how could I integrate that new kind of documentation ? Do you have an API ? How do you manage to environments : integration vs. production,...

And for each of these questions the answers were coming very naturally, here are some of them below.

## 🔌 Does your map have an API ?

That was one of the first one, along with programming languages bindings and SDKs. The anwser is very easy : yes, and take a good look a Neo4J documentation to find the approach that best fits your needs.

Still saying that REST and GraphQL are available as well as a wide variety of SDKs for a great variety of languages (Java, GO, Ruby, Python, js, .NET,...).

In a word,

> _"loading our data into Neo4J made our map highly interoperable, making it available for a wide set of usecases, but at no developement cost."_

## 🛤️ About environments and releases



- _"How do you manage environements ? Often I make draft candidate architectures : how do you handle this ?"_
- _"Well, as it's all code based in Git, we handle this by using a dedicated issue and branches. If your candidate is released, then the code has to merged in the proper branch"_

Also :

- _"How do you version the architecture map ?"_
- _"We strongly rely on git revision system"_
- _"Awesome, for the first time we have a fine grained architecture map !... and even are able compare version and environments ?"_
- _"Absolutely."_

## 🦾 Automating

 In the first version we are integrating static data, but as time goes by, we started to want to grab some other external entities, coming from other live system and create new relationships.

For example, we were highly interested in getting the following objects :

- Contracts (linked to some services or apps)
- [Git repositories](https://docs.github.com/en/rest/repos/repos#list-organization-repositories) (so we could import metadatas and browse) to grab technology, maintainers, [issues](https://docs.github.com/en/rest/issues/issues), software quality scores, [users](https://docs.github.com/en/rest/users/users),...
- Active Directory accounts,
- ...

To make the system richer, we plan to implement daily jobs through CI that produce csv so the live part stays up-to-date. In a word, create daily builds and releases.

Finally  comes the delivery part... 

## 📩 Delivering the map

As this point, people wanted to get a ready to use map on their workstation, but we did not have time to install a centralized Neo4J instance.

Still we needed to deliver a ready to use and up-to-date versions to people. This is why this is probably the next thing we will operate :

> _"deliver ready to use docker images,"_ 

with adequate tags according to what people ask us, at least : production, integration, qualification.

We'll probably deliver classic tags like latest (main branch), stable (based on latest tag) and tag-name itself, all targeting production environment/branch as most questions are for production items.

Finally to get the map you need, you should just pull and run the right image, then browse it. That's it.

## 🔚 Conclusion

Hopefully you enjoyed this approach. Just enjoy that kind of data-driven approach, customize it and start thinking about your information system as a whole thing, show relationships and nodes to collaborators, make story tellings for your teams, on your architecture and never stop making it better day after day.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7zobhx7xbr9an5icda63.png)
 