---
comments: 1
id: 1161649
is_dev_challenge: false
published_at: '2022-08-18T10:33:00Z'
reactions: 0
reading_time_minutes: 1
tags:
- showdev
- news
- java
- ux
title: 💪 Bypass SMS 160 chars limits and send Star Wars intro as a single concatenated
  📜
url: https://dev.to/optnc/bypass-sms-160-chars-limits-and-send-star-wars-intro-as-a-single-concatenated-11ok
---

## ❔ About

Many `SMS` services and gateways support **_"concatenated SMS"_ ** (messages or messages over 160 characters).

This time, we'll show how our Java (`picocli` & Spring Boot) based `cli`, thanks to a nicely designed API make the sending of (very) long SMS look like a piece of 🍰.

## 📑 Existing services and gateways

In the wild, we can find two famous SMS API services : 

[Jasmin SMS](https://www.jasminsms.com/) is one of them... and it supports "Long Messages" :

> "Supports concatenated (multipart) SMS contents (long SMS)"

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vmxybar0vj1dxy8996zm.png)](https://docs.jasminsms.com/en/latest/)
 
So does [Twilio](https://www.twilio.com/messaging/sms), still providing [some best practices guidelines](https://support.twilio.com/hc/en-us/articles/223181508-Does-Twilio-support-concatenated-SMS-messages-or-messages-over-160-characters-) : 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mxq1lzhx3f1wctm94n8v.png)
](https://support.twilio.com/hc/en-us/articles/223181508-Does-Twilio-support-concatenated-SMS-messages-or-messages-over-160-characters-) 

## 🍿 `cli` Showtime ✨

`OPT-SMS` is a `cli` which aims is to simplify integrations & sms batch sending easier for any user who has an access to the API.

Our `cli` does not required any technical skill to perform usually not that easy tasks, for any kind of user on any kind of platform as it is a (Spring boot) Java based project.

{% youtube WjQgS7aNgGc %}