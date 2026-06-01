---
comments: 1
id: 1087429
is_dev_challenge: false
published_at: '2022-06-08T20:54:07Z'
reactions: 5
reading_time_minutes: 1
tags:
- java
- maven
- programming
- productivity
title: Java runtime management automation with SDKMAN! .sdkmanrc
url: https://dev.to/optnc/java-runtime-management-automation-with-sdkman-sdkmanrc-3eoi
---

## 👉 Intro

Recently I had to onboard a new programmer in our Team. His first programming experience is to add a feature to an existing Java based SDK Project.

Our culture in the team is to use Open JDK flavors of Java,...

> still that was not mentionned in any `README.md`.

And once I asked him if he had installed his java runtime he answered me : 

> _"Yes, take a look, I've just installed the AWS's one."_

At this moment I told my self and to the team that we should enhance this part of the onboarding process...

> **so people would know on which distribution and version of our Java runtime we should work, as part of project's source code itself.**

The same week, I saw the following tweet : 

{% tweet 1525439674939998209 %}

That was showing how to achieve this without having to write any documentation and by **providing the desired target runtime... next to source code** ❣️

👉 The purpose of this post is to show how to achieve this within a live demo.

## 🍿 Demo

{% youtube nPg5d1YOKjk %}

## 🔖 Killercoda

You can play by yourself with the demo with the dedicated Killercoda scenario : 

{% embed https://killercoda.com/opt-labs/course/sdkman/sdkmanrc %}