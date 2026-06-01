---
comments: 2
id: 1115785
is_dev_challenge: false
published_at: '2022-07-28T07:06:04Z'
reactions: 1
reading_time_minutes: 3
tags:
- api
- java
- programming
- showdev
title: 📲 Inspired by Twilio we started to build our own (pico)cli to send sms
url: https://dev.to/optnc/inspired-by-twilio-we-started-to-build-our-own-picocli-to-send-sms-3f80
---

## ❔ About

Back in 2019, while trying to send notifications for a personal ([Arduino `MKR WiFi 1010`](https://docs.arduino.cc/hardware/mkr-wifi-1010)) IoT project :

{% embed https://www.linkedin.com/pulse/making-legacy-mailboxes-smarter-arduino-iot-cloud-platform-sales/ %}

Well... I felt the need to send `sms`... and used [IFTTT](https://ifttt.com/sms) to achieve this... but also discovered [Twilio](https://www.twilio.com/)... and started to follow them on social medias.

## 😮 The post that teased me

Then... one day.. I discovered that blog post :

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8lqlh0p6yre4v7tkh722.png)](https://www.twilio.com/blog/cli-app-java-jbang-picocli)

Explaining **step by step how to build from scratch** a Java Client to send `sms` based on : 

- [Twilio `SMS` API](https://www.twilio.com/docs/sms/api) : _"API that helps you add robust messaging capabilities to your applications."_
- [`SDKMAN!`](https://sdkman.io/) : _"a tool for managing parallel versions of multiple Software Development Kits"_
- [`JBang!`](https://www.jbang.dev/) : _"edit and run self-contained source-only Java programs with unprecedented ease."_
- [`picocli`](https://picocli.info/) : _"a mighty tiny command line interface"_

Finally I saw the conclusion :


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pusw3kv0e7ke7d5o1ntk.png)

Even better I saw the following tweet : 

{% twitter 1287845230197211137 %}
 
I was mesmerized by the simplicity and started to think...

> 🤔 _"One day, we will implement this at the office"_

## 🔭 Start dreaming

> **Since that day, I neved stopped dreaming about the opportunity to create such a `cli`** ❣️

I mean... like....

{% embed https://giphy.com/gifs/Collider-yes-do-it-PLIxrcm4rPZfVh6k8j %}

## 🍀 The opportunity

Then one day the opportunity came : my Team was in charge of creating a new batch that should : 

✅ Use our internal `sms` API
✅ Send `sms` in a batch mode while taking `csv` as input

That was it, we had the **opportunity to create something clean and cool** around the `sms` experience : 

> We would create a nicely, efficient and well designed `cli` 🤗

## 🚀 Straight to the MVP

### 📜 `cli` guidelines

First, we wanted to build a userexperience around the `cli` to make it also as much user-friendly as possible.

Therefore we started to learn more about `cli` design best practices :

- [10 design principles for delightful CLIs](https://blog.developer.atlassian.com/10-design-principles-for-delightful-clis/)

Then this site which is an amazing set of dedicated resources: 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/skf24i7yb2ircdex28ui.png)](https://clig.dev/)

👉 You can folllow the underlying repo :

{% github cli-guidelines/cli-guidelines %}

### ✨ Finally... the first `sms` 

Finally, our first MVP was up... from the terminal :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/52mrfsvzqt41i7h07f62.png)

to the mobile phone :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ziqwt3y81wvreazl2v13.png)

## 🛤️ Roadmap

Next steps are : 

- Refactoring for better performances
- Reporting features
- Implement `csv` send mode in batch
- `cli` packaging using [`JReleaser` to ease its distribution](https://jreleaser.org/guide/latest/distributions/binary.html#_packager_support) (`Docker`, `Homebrew`, `Macports`, native,...)

## 🍿 Demo

Finally we could manage go get a new experience.

Discover below **the software in its very early stages** : 

{% youtube 4Rn_T_q207Y %}
 

## 🔖 Resources

- [Twilio on RapidAPI](https://rapidapi.com/user/twilio)
- [Twilio Blog](https://www.twilio.com/blog)
- [`#twilio`](https://dev.to/t/twilio) on DEV.to

## 📑 SMS APIs

- [Free SMS APIs](https://rapidapi.com/collection/free-sms-apis)
- [Twilio SMS](https://rapidapi.com/twilio/api/twilio-sms/)


## 🐦 Twitter accounts worth following 🥇

- **Matthew (he/him)** : [`@MaximumGilliard`](https://twitter.com/MaximumGilliard)
- **Ben Firshman** : [`@bfirsh`](https://twitter.com/bfirsh)
- **Carl Tashian** : [`@tashian`](https://twitter.com/tashian)
- **Eva Parish** : [`@evpari`](https://twitter.com/evpari)
- [`@twilio`](https://twitter.com/twilio)
- [`@picocli`](https://twitter.com/picocli)
- [`@jbangdev`](https://twitter.com/jbangdev)
- [`@jreleaser`](https://twitter.com/jreleaser)

Stay tuned for more 😊.