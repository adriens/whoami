---
comments: 4
id: 1090316
is_dev_challenge: false
published_at: '2022-05-19T21:03:41Z'
reactions: 5
reading_time_minutes: 1
tags:
- java
- springboot
- programming
- podman
title: 👋 Good bye Spring Boot 2.5.x, hello 2.7.0
url: https://dev.to/optnc/good-bye-spring-boot-25x-hello-270-40n
---

## 📢 Announce

Yesterday Spring team announced the `2.5.14` release... and also...

> 2.5.x has now reached the end of its OSS support 

{% twitter 1527217911730929664 %}

... and as promised, the long awaited `2.7` release announce !

{% twitter 1527284897240428545 %}

Below the full releaseNote : 

{% embed https://spring.io/blog/2022/05/19/spring-boot-2-7-0-available-now %}

## 📝 Details

Two of the most remarkable news are : 

- New `@DataCoubaseTest` and `@DataElasticsearchTest` support
- Podman can now be used when building images using Cloud Native Buildpacks

as we started to use Podman ro tun containers and always pushing further on testing.

Also in the [detailed releaseNote](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.7-Release-Notes#dependency-upgrades ), we can notice among others : 

- [Numerous dependency upgrades](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.7-Release-Notes#dependency-upgrades), including `Kafka 3.1`
- `Elasticsearch 7.17` (still no Elastic 8.x native support, awaited for Spring 3.x)

Also taking a glance at [miscellanous](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.7-Release-Notes#miscellaneous) details is worth reading for Kafka users, JDBC and ElasticSearch 

## 🏁 Upgrade time

If you are using Dependabot like we do, just wait for [PullRequests comme to your repo](https://github.com/opt-nc/opt-temps-attente-agences-api/pull/78) to discover how to upgrade : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zrj8xt5wlvkhpuy997ih.png)
 