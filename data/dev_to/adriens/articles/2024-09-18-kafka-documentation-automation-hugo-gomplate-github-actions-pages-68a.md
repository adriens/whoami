---
comments: 2
id: 1998753
is_dev_challenge: false
published_at: '2024-09-18T20:30:38Z'
reactions: 2
reading_time_minutes: 3
tags:
- productivity
- devops
- kafka
- showdev
title: '🔁➡️📘 Kafka documentation automation : HUGO, gomplate, Github Actions & pages'
url: https://dev.to/optnc/kafka-documentation-automation-hugo-gomplate-github-actions-pages-68a
---

## 💭 _"what's wrong with writing (and maintaining) docs ?"_

> Very often **a single team has a privileged access to a set of data, services, middlewares** and you cannot grant access because of technical limitations (sometimes due to limited licences plans), costs, access control strategies
 or so many other reasons : there may me plenty of them.

👉 Still, it is not rare that **third parties need to have at least a partial access to these resources**, for example to develop new services on top of yours.

## 💸 The cost of manual legacy documentation

The consequence is that you may be asked to implement a Wiki (eg. on Confluence) that your **team will be charged to maintain in addition to its core activities.**

Then you grant access to this wiki and **everyone is happy..or so you think**... as 

> you have just increased the `RUN` load of your team... and then impacted your own _"Time to Market"_ to deliver new bankable services.

To make simple, the problem with this strategy is that : 

- 😫 It will cost you a **lot of time**
- **🏋️ You have to stay up-to-date** with sometime - and hopefully for you - very fast changing systems
- **📉 You waste your team skills** & workforce on writing most of the time outdated documentations

## ♾️ Embracing continuous change

> What we want is a [SchemaCrawler](https://www.schemacrawler.com/) like portable and static report of our onPrem Kafka so we can embrace the change comfortably and continuously.

## 🎯 The _"What"_ & the _"How"_

This post is about this common pattern and **how we delivered a scalable data-driven documentation pipeline around Kafka**, based on data & CI:

1. **💰 We already have the automatically data prepared & delivered** as `csv` and `json` by scheduled GH Actions on a third party repository
2. **🦥 On a dedicated Wiki-like repository** we `clone` the part of the data we need
3. **🔁 Thanks to templates & [`gomplate`](https://docs.gomplate.ca/)** we transform `csv` and `json` into nice `markdown`
4. **🎁 We build & deliver the resulting static site** with [HUGO Github Action](https://gohugo.io/hosting-and-deployment/hosting-on-github/) on GH Pages
5. **🤩 We enjoy** the [`HUGO shadocs`](https://themes.gohugo.io/themes/shadocs/) theme

## 💰 Benefits

Below some benefits we immediately got

- **🔄  Up-to-date** documentation
- **🛡️ Data security** thanks to custom obfuscation so the doc can be shared with confidence to third parties
- **⚡`DevEx` impact** : third parties get informations _"as a Service"_, whenever they need it 24/7 : no need to make an issue...
- **🤩 Responsive wiki and amazing UI** (PC, tablet and even phone)
- **🌟 Continuously improving documentations**, howtos and resources
- **_"🎀 as a Service"_** delivery
- **🔗 Linked to classical/legacy static documentations**... in both directions
- **🔐 GitHub driven Access management** (Teams, SSO,...)

## 🍿 Demo

{% youtube JBlSaaiiS2w %}

## 💪 The magic of `gomplate` : `csv` to `markdown`s

The core magic that transforms **a single input `csv` file into more than 100 separate `markdown`**  (in less than 1' ) is below : 

```yaml
in: |
  {{ $topics := (datasource "topics") | data.ToCSV | data.CSVByRow }}
  
  {{ range $i, $e := $topics }}
    {{ $file := $e.name | strings.Slug }}
    {{ tmpl.Exec "topicT" . | file.Write (print "outputs/topics/" $file ".md") }}
  {{ end }}

templates:
  - topicT=template/topic.tmpl
datasources:
  topics:
    url: source/import/auto/kafka/node_kafka_topic.csv
outputFiles: ["csv"]

suppressEmpty: true
```

🤩 Then `HUGO` does the rest within GitHub to **deliver a whole functional website  : the overall process takes less than a minute.**