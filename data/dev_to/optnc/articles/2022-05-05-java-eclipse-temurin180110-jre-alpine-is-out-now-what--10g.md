---
comments: 1
id: 1075764
is_dev_challenge: false
published_at: '2022-05-05T01:57:41Z'
reactions: 3
reading_time_minutes: 1
tags:
- docker
- java
- infosec
- devops
title: 🗞️ Java eclipse temurin:18.0.1_10-jre-alpine is out ! Now what ?
url: https://dev.to/optnc/java-eclipse-temurin180110-jre-alpine-is-out-now-what--10g
---

## 🛡️ About

Java 18 is out since a few weeks. 

> Let's see how we can handle its integration in Docker images the Dev(Sec)Ops way 👇

## 🍿 Demo

[Eclipse Temurin](https://hub.docker.com/_/eclipse-temurin) is maintaining a rich collection of Java images.

See below how we are aware of required maintenant on our own images... and how we double check it is well secured with [`grype`](https://github.com/anchore/grype) : 

{% youtube https://youtu.be/dhhRxWpDWE0 %}


## 🔖 Related posts

{% embed https://dev.to/optnc/bench-and-choose-java-8-docker-images-with-anchoregrype-4fg8 %}

{% embed https://dev.to/optnc/grype-0350-new-feature-indicate-location-of-vulnerability-1pam %}

{% embed https://dev.to/optnc/about-java-bytecode-native-binaries-security-short-grype-benchmark-4ng9 %}

{% embed https://dev.to/optnc/dependency-management-automation-with-dependabot-3l62 %}
