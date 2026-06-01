---
comments: 0
id: 1047181
is_dev_challenge: false
published_at: '2022-04-07T03:17:39Z'
reactions: 5
reading_time_minutes: 1
tags:
- github
- security
- maintenance
- java
title: 🦾 Dependency management automation with Dependabot
url: https://dev.to/optnc/dependency-management-automation-with-dependabot-3l62
---

## ❔ Intro

We (Java programmers) recently had to face 3 majors issues :

- Two on [Log4J](https://www.dynatrace.com/news/blog/what-is-log4shell/)
- One on [Spring](https://spring.io/blog/2022/03/31/spring-framework-rce-early-announcement).

In the mean time teams have an ever growing set of projects to manage.

⚠️ While you **often rely on public dependencies**, you also **can rely on your own private ones... which can themsleves depend on public ones and then present security flaws.**

👆 **In both cases, dependency management has to be performed at scale on your pipeline from build to deployment... as fast as possible... and on all your code.**

Sometimes, you just need to be aware that some of your dependencies are not up-to-date, for example to get new features.

In both cases : 

> _You don't have time to spend to monitor your favorite dependencies for each of your projects : you'd rather see someone else do the job._

Yet, when it's about security...

> _The job has to be done as fast as possible at scale... and without breaking existing software so the fix can be deployed as fast as possible._


This is what this post is about.

It will show how we achieve this as part of the CI with [Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) :

{% youtube NHJSdEYDqRw %}