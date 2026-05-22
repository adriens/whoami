---
comments: 12
id: 2385057
is_dev_challenge: false
published_at: '2025-04-14T21:48:18Z'
reactions: 1
reading_time_minutes: 2
tags:
- showdev
- go
- cli
- learning
title: 🥳 We built the cli of our dreams to send sms ❣️
url: https://dev.to/optnc/we-built-the-cli-of-our-dreams-to-send-sms-3c7m
---

## 🤔 About the benefits of `cli`

Since a few years now, we started to design various `cli` for internal batch usage, on our Java Stack on top of [`picocli`](https://picocli.info/) and [`quarkus`](https://quarkus.io/), delivered as images, and run on [`podman`](https://podman.io/).

Our goal was to : 

1. **Avoid as much as possible to write** unnecessary documentations : each tool should describe himself according to a common pattern
2. **Rely on the best possible practices**
3. And overall : **deliver a consistent first-class UX to OPS**

Therefore I started to read and follow the following site to follow the best possible guidelines : 

{% embed https://github.com/cli-guidelines/cli-guidelines %}

## 🎯 Our `Go`(al)

On my very own side I gave a try during a hackathon to Go and [`goreleaser`](https://goreleaser.com/) : 

{% embed https://dev.to/adriens/github-copilot-1-day-build-challenge-eol-a-tiny-go-client-to-manage-eols-j %}

Then, I wanted to bring my team to the Go experience at the office  as sometimes we need to deliver apps to **systems on which we don't want or can't install new softwares** : so delivering a static binary thanks to Go and [`goreleaser`](https://goreleaser.com/) seemed a good option for effortless cross-compilation... and of course build the best possible `UX` thanks to [Cobra](https://cobra.dev/).

So I used this opportunity to sharpen our skill with my team : 

{% twitter 1909597554590855170 %}

And...

> Build the best possible `cli` of our dreams to send `sms` from a terminal and see what we can deliver and learn from that.


## 🍿 `v1.0.0` `brew` unboxing

{% youtube jHg7Ydlo55E %}

## 📜 The story behind the product development

As I always say to my team & student, always ["Start with why"](https://www.goodreads.com/book/show/7108725-start-with-why?ref=nav_sb_ss_1_12) : 

{% twitter 1910458188945867005 %}

After having drafted my ideas : 

{% twitter 1908757267941666914 %}

Here are the motivations that kept us on track : 

Do things extremely : 

- 🧩 Interoperable
- **🫴 Easy to integrate for anyone** (even on legacy systems)
- ⚡ Efficient
- **🦥 Useful : make people save time**, ie. make more with less effort
- **📦 Easy to deliver** and install
- 🤩 Beautiful
- **📉 Fast to build** : for an improved Time to market
- **🟢 Fast** to (learn to) use
- **💡 Inspiring** for us and others, eg. create new business opportunities ideas
- **😍 Desirable** : people should feel the desire to use the product and feel joy while using it
- **🧑‍🤝‍🧑 Create new relationships with people** and discover new practices


## 🔭 What's next

Next, we'll focus on **showing and sharing** the benefits : 

- **♾️ Continuous delivery tools** and automation
- **📼 New ways of documentation** with next-gen tools
- **🛡️ Security** (beacause it always matters)
- **🦸 One liners** (because they're both a cool and efficient way to get things done)
- **🐧 Classical linux** tools
- **📚 General IT Culture**
- **🧑‍🎨 Creative product design** and development

Hopefully you'll like it as much as we do...and will engage yourself on the same kind of way : the [`#learnbydoing`](https://dev.to/t/learning) journey 🤗