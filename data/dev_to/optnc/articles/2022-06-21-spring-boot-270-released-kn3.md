---
comments: 8
id: 1120720
is_dev_challenge: false
published_at: '2022-06-21T20:52:00Z'
reactions: 12
reading_time_minutes: 2
tags:
- java
- springboot
- news
- opensource
title: 🎀 Spring Boot 2.7.0 Released
url: https://dev.to/optnc/spring-boot-270-released-kn3
---

## 📢 About

Spring Boot `2.7.0` has [just been released](https://spring.io/blog/2022/05/19/spring-boot-2-7-0-available-now) :

{% embed https://www.infoq.com/news/2022/06/spring-boot-2-7 %}

👉 Let's summarize what it brings and what's the next step.

## 🛍️ What it brings

- Support for [GraphQL 1.0](https://www.infoq.com/news/2022/06/spring-graphql/)
- Support for the [`Podman` container engine](https://podman.io/) as an alternative to Docker Engine 
- Dependency management and auto-configuration for [`Cache2k`](https://cache2k.org/)

## 🧰 Testing related features

Hot news around testing as new test annotations are coming for :

- [`ElasticSearch`](https://www.elastic.co/) 
- [`Couchbase`](https://www.couchbase.com/)

## 📖 `/actuator/info` related features

[`JavaInfoContributor`](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/actuate/info/JavaInfoContributor.html) and [`OsInfoContributor` ](https://docs.spring.io/spring-boot/docs/current/api/org/springframework/boot/actuate/info/OsInfoContributor.html )classes have been improved and can now expose more information about :

- Java version & vendor
- Underlying OS

## ⬆️ Dependencies updates

- [Spring Data 2021.2](https://github.com/spring-projects/spring-data-commons/wiki/Release-Train-2021.2-%28Raj%29-Release-Notes)
- [Spring Security 5.7](https://github.com/spring-projects/spring-security/releases/tag/5.7.0)
- [Infinispan 13](https://infinispan.org/blog/2021/10/12/infinispan-13-final)
- [Micrometer 1.9](https://github.com/micrometer-metrics/micrometer/releases/tag/v1.9.0)
- [Elasticsearch 7.17](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/release-highlights.html)
- [H2 2.1](https://github.com/h2database/h2database/releases)
- [Flyway 8.5](https://github.com/flyway/flyway/releases)


## 🛤️ Head to `Spring Boot 3.0`

Based on Spring Framework 6.0, Spring Boot 3.0 will be the next major revision **and will require Java 17 or above**. 


☝️ Spring Boot 3.0, **planned for November 2022**, will be the next version.

Spring Boot 3.0 will also support AOT (ahead-of-time) compilation and native executables thanks to [Spring Native](https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/).