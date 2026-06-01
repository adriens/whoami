---
comments: 1
id: 1123829
is_dev_challenge: false
published_at: '2022-06-29T23:21:02Z'
reactions: 7
reading_time_minutes: 1
tags:
- docker
- kafka
- security
- devops
title: '⚖️ Kafka image : wurstmeister vs. bitnami'
url: https://dev.to/optnc/kafka-image-wurstmeister-vs-bitnami-efg
---

## ❔ Context

We recenlty did operate maintenance on our interal (yet public repo) that helps us internally promote Kafka practices : 

{% github opt-nc/atelier-spring-kafka %}

☝️ We also do apply a maintenance strategy on this content like : 

- [Spring Boot upgrades](https://github.com/opt-nc/atelier-spring-kafka/pull/21)
- [Kafka upgrades](https://github.com/opt-nc/atelier-spring-kafka/pull/19)

We created a [dedicated issue to upgrade to Kafka `3.2`](https://github.com/opt-nc/atelier-spring-kafka/issues/18), we switched from [`wurstmeister/kafka`](https://hub.docker.com/r/wurstmeister/kafka/) to [`bitnami/kafka`](https://hub.docker.com/r/bitnami/kafka/) (by [vmWare](https://hub.docker.com/u/bitnami)) cf [our configuration change](https://github.com/opt-nc/atelier-spring-kafka/commit/7255813352133f76d205e7cec0cf3d25ee6a8dee).

## 🛡️ Security concerns

☝️ Each time we use a new Docker image, we also focus on the security part.

👉 **This post is about the comparison of these two images security levels.**

```shell
grype --add-cpes-if-none wurstmeister/kafka:latest \
    | grep Critical \
    | wc -l
# 14
grype bitnami/kafka:latest \
    | grep Critical \
    | wc -l
# 5
```

|Criticity|`wurstmeister/kafka:latest`|`bitnami/kafka:latest` |
|       ---     |          ---       |          ---         |
| ☣️`Critical`  | 14                 | 5                    |  
| ❗`High`      | 34                 | 17                   | 
| ❕`Medium`    | 16                 | 9                    | 
| ⚠️`Low`       | 9                  | 9                    | 
| 🪶`Negligible`| 68                 | 66                   |
| ❔`Unknown`   | 15                 | 13                   |


## 📊 Charts

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uolz7iqqat8ye0fww7ki.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1zfkuqvqb12dziuemxur.png)

## 🤔 The `Unknown` Criticity
 
Wondering what means `Unknown` Criticity ? Check the answer below :


{% embed https://github.com/anchore/grype/issues/807 %}

## 📦 Apache Kafka packaged by `Bitnami`

{% github bitnami/bitnami-docker-kafka %}

## 🔖 Resources

- 🐦 [`@bitnami`](https://twitter.com/Bitnami)
- 🐳 [Bitnami containers](https://bitnami.com/stacks/containers)