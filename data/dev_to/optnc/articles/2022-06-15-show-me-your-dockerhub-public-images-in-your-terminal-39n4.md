---
comments: 2
id: 1065476
is_dev_challenge: false
published_at: '2022-06-15T20:26:54Z'
reactions: 8
reading_time_minutes: 2
tags:
- docker
- api
- beginners
- json
title: 🌈 Show me your DockerHub public images in your terminal
url: https://dev.to/optnc/show-me-your-dockerhub-public-images-in-your-terminal-39n4
---

## ❔ Intro

[Docker Registry `HTTP API V2`](https://docs.docker.com/registry/spec/api/) make is possible to query the registry in a comfortable way.

To showcase our public images, I wonder if I could :

- **Learn** more about the API
- **Play** with `jq` options
- **Showcase** some content in a fun yet interesting way, from the terminal itself
- Generate other kinds of **creative ideas** around this topic

## 💡 The idea

To put in evidence the popularity of our images to the team that builds them,

> I wanted to display a ranking they could play with on their workstations... right into their terminal

## 🧰 Tooling

Therefore I used the tool the team already uses on a daily basis to test & document our APIs : 

- [`httpie`](https://httpie.io/) : _"As easy as /aitch-tee-tee-pie/ pie Modern, user-friendly command-line HTTP client for the API era. JSON support, colors, sessions, downloads, plugins & more. "_
- [`jq`](https://stedolan.github.io/jq/) : _"jq is like `sed` for JSON data"_

... and for the fun and geek culture :

- [`lolcat`](https://github.com/busyloop/lolcat) : _"Rainbows and unicorns!"_


```shell
http https://hub.docker.com/v2/repositories/optnc | \
	 jq -r '"Image\tPulls", "-----------------------\t---", ( .results | sort_by(.pull_count) | reverse | .[] | "\(.name)\t\(.pull_count)")' | \
 column -t -s $'\t' | \
 lolcat -a -d 20
```

## 🍿 Demo

Here is the final demo :

{% youtube uaiklKmxkws %}

Find the _movie source code_ just below (so you can replay or customize it) : 

```shell
# 🤓 Let's see at optnc's public images on DockerHub 🎇

http https://hub.docker.com/v2/repositories/optnc | jq -r '"Image\tStars\tPulls", "-----------------------\t-------\t------", ( .results | sort_by(.pull_count) | reverse | .[] | "\(.name)\t\(.star_count)\t\(.pull_count)")' | column -t -s $'\t'

# 🎬 Now watching the spicy way 🌈

clear && http https://hub.docker.com/v2/repositories/optnc | \
	 jq -r '"Image\tPulls", "-----------------------\t---", ( .results | sort_by(.pull_count) | reverse | .[] | "\(.name)\t\(.pull_count)")' | \
 column -t -s $'\t' | \
 lolcat -a -d 20

# 🙏🏻 Hopefully you enjoyed this short demo 🙋
```

## 🔖 Resources

- [Docker HUB API (beta)](https://docs.docker.com/docker-hub/api/latest/)
- [Docker Registry HTTP API V2](https://docs.docker.com/registry/spec/api/)
- [Great collection of DockerHub Docker Registry API call Examples](https://www.arthurkoziel.com/dockerhub-registry-api/)

## 📜 Drafts

Below drafts that helped create the final version 👇

```
http https://hub.docker.com/v2/repositories/optnc | jq -r '.results|.[] | "\(.name)\t\(.star_count)"'  | column -t -s $'\t'
```

Then the aligned version : 

```
http https://hub.docker.com/v2/repositories/optnc | jq -r '"Image\tStars", "-----------------------\t-------", ( .results|.[] | "\(.name)\t\(.star_count)" )' | column -t -s $'\t'
```

Sorting desc by stars : 

```
http https://hub.docker.com/v2/repositories/optnc | jq -r '( .results | sort_by(.star_count) | reverse | .[] | "\(.name)\t\(.star_count)")' | column -t -s $'\t'
```

Then with `lolcat` piping : 

```
http https://hub.docker.com/v2/repositories/optnc | jq -r '"Image\tStars\tPulls", "-----------------------\t-------\t------", ( .results | sort_by(.pull_count) | reverse | .[] | "\(.name)\t\(.star_count)\t\(.pull_count)")' | column -t -s $'\t' | lolcat
```

