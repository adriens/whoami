---
comments: 4
id: 1099319
is_dev_challenge: false
published_at: '2022-05-29T22:24:18Z'
reactions: 3
reading_time_minutes: 3
tags:
- java
- springboot
- programming
- spring
title: 🏁 Preparing for Spring Boot 3.0
url: https://dev.to/optnc/preparing-for-spring-boot-30-3bi9
---

## 👉 Context

We all are aware that... 

> **Spring Boot `3.0` is coming ❕**

Since a few months as part of our pipeline's migration from onPremise to Github.com process we have been prototyping on Spring Native and invest on maintenance by upgrading :

- Our dependencies (let Dependabot PRs ⛆ 😱 ), making us upgrade all to [`2.6.7`](https://spring.io/blog/2022/04/21/spring-boot-2-6-7-available-now), then more recently [`2.7.0`](https://spring.io/blog/2022/05/19/spring-boot-2-7-0-available-now)
- Our runtime from `Java 8` to `Java 17`... from the dev side up to the server runtime

## 🧽 Gains

That was a big work to achieve but offered us the **opportunity to improve our testing strategies** (less code for more coverage), dependencies cleanup/removal to make native easier in a near future.

> Notice that this investment made it possible to achieve `RUN` tasks in a much more comfortable on a continuous pace and less time consuming way... while making it possible to **upgrade the middlewares we rely on**.

## ☝️ Switching to Spring Data libraries

As part of dependencies cleanup, we switched to [Spring Data for Elasticsearch](https://github.com/spring-projects/spring-data-elasticsearch#spring-data-for-elasticsearch--), hence making us rely on [Spring Data](https://spring.io/projects/spring-data)  instead of Elastic's ones.

So we chose the following **straightforward strategy** : 

We did migrate our Elastic instance to Elastic 7... and [wait to Spring Boot 3, based on Spring 6 and Java 17.](https://github.com/spring-projects/spring-data-elasticsearch#elasticsearch-8-client-libraries)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/axu273wyqtgry4smorlm.png)

Find below the [compatibility matrix](https://docs.spring.io/spring-data/elasticsearch/docs/current-SNAPSHOT/reference/html/#preface.versions) (so you don't have to look for it 😓) : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/srxps2ua35vweraal1ww.png)
 

## 🐳 Docker prepare
 
In the mean time we also did prepare traditional (non native) docker images that embeds a secured Java 17 runtime, see below for more : 

{% embed  https://dev.to/optnc/java-eclipse-temurin180110-jre-alpine-is-out-now-what--10g %}

## 🌌 Be ready for Spring Boot 3

Fortunately Spring tweeted a dedicated post on this topic : 

{% twitter 1529432188038561794 %}

According to the [blog post](https://spring.io/blog/2022/05/24/preparing-for-spring-boot-3-0), here are the things you can do to get ready.

In our team, this will be used as a checklist to get ready to migrate as clean as possible : 

### 1️⃣ Upgrade to Java 17

> "Spring Boot 3.0 will require Java 17."

Hence it makes it possible to use [Records](https://dzone.com/articles/what-are-java-records).

Also here is Spring advice : 

> "We highly recommend that you upgrade your JDK today if at all possible."

### 2️⃣ Upgrade to the Latest Spring Boot `2.7.x`

Spring will provide a migration guide to Spring Boot 3...

> "but it will assume that you’re migrating from Spring Boot 2.7 and not an earlier version."

We also applied the following migration strategy, following SB upgrades on a continuous way (so we finally could drastically reduce our technical debt):

> If you’re upgrading from Spring Boot 2.5 or earlier, we don’t recommend skipping releases.** It’s often easier to upgrade in steps** (e.g. 2.5 → 2.6 → 2.7) rather than trying to upgrade directly from 2.5 → 2.7.

### 3️⃣ Check for Calls to Deprecated Code

> **Spring Boot 3.0 will remove all deprecated code**, so we recommend that you check your existing code is not relying on any deprecated methods. It’s worth considering using the `-Werror` Java compiler option to fail your build if deprecation warnings are reported.

### 4️⃣ Migrate from Legacy `application.properties` and `application.yaml` Processing

> The **legacy processing support will not be coming to Spring Boot 3.0** so you should check that your project doesn’t set `spring.config.use-legacy-processing`.

### 5️⃣ Use Spring MVC’s PathPatternParser

> we recommend using the `PathPatternParser` if at all possible since it provides better performance.

### 6️⃣ Other

Also see the [full blog post ](https://spring.io/blog/2022/05/24/preparing-for-spring-boot-3-0)for more about _Third-party Projects Have Jakarta EE 9 Compatible Releases_ and _Third-party Projects have Updated Spring Compatible Releases_

## 🔖 Resources

- [Preparing for Spring boot 3.0](https://spring.io/blog/2022/05/24/preparing-for-spring-boot-3-0)
- [VMware Overhauls Spring 6 & Spring Boot 3 for Another Decade ](https://www.infoq.com/news/2021/09/spring-6-spring-boot-3-overhaul/)