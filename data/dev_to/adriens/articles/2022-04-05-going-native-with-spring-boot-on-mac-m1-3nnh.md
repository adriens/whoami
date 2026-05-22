---
comments: 2
id: 1045907
is_dev_challenge: false
published_at: '2022-04-05T22:12:00Z'
reactions: 3
reading_time_minutes: 2
tags:
- graalvm
- knative
- springboot
title: ⏩ Going native with Spring Boot on Mac M1
url: https://dev.to/optnc/going-native-with-spring-boot-on-mac-m1-3nnh
---

## 👉 Intro

I recently saw a great Spring blog post about [Building Native Images with GraalVM and Spring Native on Apple's M1 Architecture](https://spring.io/blog/2022/03/23/building-native-images-with-graalvm-and-spring-native-on-apple-s-m1-architecture).

In the same time we are investigating on porting some of our (innovation dedicated) existing Spring Boot based APIs to [Spring Native](https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/), see related content : 

{% embed https://dev.to/optnc/knative-the-easy-way-to-serverless-a-java-app-3n36 %}

As one of our developers works on an Mac M1, we wanted to give it a try to see what would happen.

This short blog post is about that short experimentation.

## 🎞️ Build & Run  : 2' speedrun

Finally we could enjoy the full and smooth cli based experience : 

1. Setup Java runtime with [GraalVM](https://www.graalvm.org/) [`22.0.0`](https://www.graalvm.org/release-notes/22_0/) with [sdkman](https://sdkman.io/)
2. Build & Install native image (and see resources used : time & memory)
3. Boot the API (`0.4`s.)
4. Perform a first REST query (`0.007` s.) with [`httpie`](https://httpie.io/)
5. Perform a second REST query (`0.003` s.)

Let the show begin :

{% embed https://youtu.be/MyNPzH7oheA %}


## 🍏 More about Apple M1

You can get a full intro/deep dive on Apple M1 Ultra architecture  thanks to this great [Computerphile](https://www.youtube.com/channel/UC9-y-6csu5WGm29I7JiwpnA) episode : 

{% embed https://youtu.be/yG1m7oGZC48 %}


## 🔖 Resources

- API [homepage on Dockerhub](https://hub.docker.com/r/optnc/api-partenaires-mobilis/)
- API on [RapidAPI marketplace](https://rapidapi.com/opt-nc-opt-nc-default/api/partenaires-mobilis/details)
- [Building Native Images with GraalVM and Spring Native on Apple's M1 Architecture](https://spring.io/blog/2022/03/23/building-native-images-with-graalvm-and-spring-native-on-apple-s-m1-architecture)

{% twitter 1511724002150162432 %}