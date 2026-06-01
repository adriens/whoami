---
comments: 0
id: 1068315
is_dev_challenge: false
published_at: '2022-05-09T22:23:54Z'
reactions: 4
reading_time_minutes: 2
tags:
- github
- java
- security
- devops
title: 🎞️ This is how we maintain & release Secured Software on Github 🤖
url: https://dev.to/optnc/this-is-how-we-maintain-release-secured-software-on-github-2pn3
---

## ❔ About

As many organizations, we have to develop & maintain (aka. **`BUILD & RUN`**) common software.

☝️ This process involves **a lot of things that have to be achieved**... (if you want to get a robust and secured software release pipeline).

I'll showcase here how we achieved all theses challenges on a common Java library dedicated to logging :

{% github opt-nc/opt-logging %}

## 🏎️ Time to Market

Software release pipeline gains everyday a shorter Time To Market.

In fact there is no real option : 

> _**maintenance & release tasks have to be drastically automated... and should embed security concerns on the left side of the pipeline.**_

## 🛡️ Security

We have three complementary ways of achieving security tasks on our pipeline : 

1. [Dependabot](https://github.com/dependabot) alerts : so we get Pull Requests to notify us what are the risks
2. [`CodeQL`](https://codeql.github.com/) Scan as part of [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) (aka. GHAS)
3. Docker Image scan (see [previous dedicated post](https://dev.to/optnc/bench-and-choose-java-8-docker-images-with-anchoregrype-4fg8))


Then to release software we rely on [`semantic-release`](https://github.com/semantic-release/semantic-release) to implement a solid [Semantic Versioning scheme](https://semver.org/) and get a

> _**fully automated version management and package publishing pipeline.**_

## 🍿 Démo

Here is the full secured & automated release process 👇

{% youtube jfvRUCo89Iw %}

## 🧰 Stack

- [`semantic-release`](https://github.com/semantic-release/semantic-release)
- [`codeql`](https://codeql.github.com/)
- [`codeql-action`](https://github.com/github/codeql-action)
- [GitHub Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)


## 🔖 Related contents

### ⛯ Scan Docker images 🛡️

{% embed https://dev.to/optnc/bench-and-choose-java-8-docker-images-with-anchoregrype-4fg8 %}

### 🔂 Semantic release demo 🎞️

Semantic release intro demo :

{% youtube Er-W5J5ky7Q %}