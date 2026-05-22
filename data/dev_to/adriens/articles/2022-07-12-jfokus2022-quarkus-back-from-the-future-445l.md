---
comments: 6
id: 1137962
is_dev_challenge: false
published_at: '2022-07-12T21:31:18Z'
reactions: 7
reading_time_minutes: 3
tags:
- quarkus
- java
- kubernetes
- showdev
title: '📑 #jfokus2022 : Quarkus [...] back from the Future'
url: https://dev.to/optnc/jfokus2022-quarkus-back-from-the-future-445l
---

## ❔ About

We recenlty started to investigate around native Java services and serverless with Spring Native as we are actually relying on Spring Boot :

{% embed https://dev.to/optnc/devops-labs-20222-premiers-pas-et-demo-spring-native-3e62 %}

{% embed https://dev.to/optnc/going-native-with-spring-boot-on-mac-m1-3nnh %}

In the mean time, we also started to perform some experimentations on Quarkus, the _"Supersonic Subatomic Java"_.

👉 This post is dedicated to an amazing session that occurred at  [`#jfokus2022`](https://www.jfokus.se/) by [Sébastien Blanc](https://www.linkedin.com/in/s%C3%A9bastien-blanc-08a73b1/) (aka. [`@sebi2706`](https://twitter.com/sebi2706)) :

> For me, this video is **THE** place to start if you want to learn more about Quarkus and all the underlying aspects

As the original video is not indexed by chapters, I decided to :

- Index the chapters
- Promote this awesome content around me

## ☝️ Intro

First, the two main aspects of Quarkus are :

- **Deployment density** (will be explained)
- Native is **Not a must have** but nice to have in serverless

## 📑 Chapters

1. [`00:00`](https://youtu.be/H7X7rQHK4qE) : Intro
2. [`01:40`](https://youtu.be/H7X7rQHK4qE?t=100) : About [Quarkus](https://quarkus.io/about/) : performance & developer experience
3. [`02:43`](https://youtu.be/H7X7rQHK4qE?t=163) : Create a Quarkus project from scratch
4. [`03:05`](https://youtu.be/H7X7rQHK4qE?t=185) : Create with [`code.quarkus.io`](https://code.quarkus.io/)
5. [`03:46`](https://youtu.be/H7X7rQHK4qE?t=226) : Create with [IDE plugin (VSCode)](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-quarkus) and [`maven`](https://maven.apache.org/)
6. [`06:20`](https://youtu.be/H7X7rQHK4qE?t=380) : Start application in [`Dev-mode`](https://quarkus.io/guides/dev-mode-differences)
7. [`07:50`](https://youtu.be/H7X7rQHK4qE?t=470) : Deal with configuration
8. [`09:00`](https://youtu.be/H7X7rQHK4qE?t=540) : Live reload and state management
9. [`11:11`](https://youtu.be/H7X7rQHK4qE?t=671) : [Continuous testing](https://quarkus.io/guides/continuous-testing)
10. [`13:08`](https://youtu.be/H7X7rQHK4qE?t=788) : [Quarkus Dev UI](https://quarkus.io/guides/dev-ui)
11. [`14:24`](https://youtu.be/H7X7rQHK4qE?t=864) : Container packaging
12. [`14:55`](https://youtu.be/H7X7rQHK4qE?t=895) : Container packaging with [`mutable-jar`](https://quarkus.io/guides/maven-tooling#remote-development-mode) (full OpenShift lifecycle demo)
13. [`21:26`](https://youtu.be/H7X7rQHK4qE?t=1286) : Cluster remote live reload with [`mvn quarkus:remote-dev`](https://developers.redhat.com/blog/2021/02/11/enhancing-the-development-loop-with-quarkus-remote-development)
14. [`23:25`](https://youtu.be/H7X7rQHK4qE?t=1405) : Create [native binary & GraalVM](https://quarkus.io/guides/building-native-image) (native profile)
15. [`28:20`](https://youtu.be/H7X7rQHK4qE?t=1700) : Persistence layer with [`Panache`](https://quarkus.io/guides/hibernate-orm-panache) layer, jdbc, Swagger, psql testcontainer,...
16. [`31:46`](https://youtu.be/H7X7rQHK4qE?t=1906) : Deal with JPA entity annotations with `Panache`
17. [`34:10`](https://youtu.be/H7X7rQHK4qE?t=2050) : [Create Resources](https://quarkus.io/guides/rest-data-panache) (`GET`, `POST`,...  )
18. [`38:58`](https://youtu.be/H7X7rQHK4qE?t=2338) : Dev Services (Databases, [Kafka](https://quarkus.io/guides/kafka), [Keycloak](https://quarkus.io/guides/security-keycloak-authorization), ... )
19. [`39:44`](https://youtu.be/H7X7rQHK4qE?t=2384) : Compatibiliy layer extensions (Doing [Spring Boot stuff in Quarkus](https://quarkus.io/blog/quarkus-for-spring-developers/))
20. [`42:15`](https://youtu.be/H7X7rQHK4qE?t=2535) : [Security with `OIDC`](https://quarkus.io/guides/security-openid-connect) : Keycloak, Okta,...
21. [`48:45`](https://youtu.be/H7X7rQHK4qE?t=2925) : Conclusion

## 🔖 Bookmarks

- [Quarkus Master Course](https://dn.dev/quarkusmaster)

## 🍿 Showtime

{% youtube H7X7rQHK4qE %}
