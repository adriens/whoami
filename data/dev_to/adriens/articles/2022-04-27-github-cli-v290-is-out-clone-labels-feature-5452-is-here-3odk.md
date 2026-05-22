---
comments: 1
id: 1068519
is_dev_challenge: false
published_at: '2022-04-27T19:58:11Z'
reactions: 10
reading_time_minutes: 2
tags:
- github
- productivity
- terminal
- codenewbie
title: '🏷️ Github CLI v2.9.0 is out : clone labels feature #5452 is here'
url: https://dev.to/optnc/github-cli-v290-is-out-clone-labels-feature-5452-is-here-3odk
---

## 🙋 Intro

[GitHub CLI `v2.9.0`](https://github.com/cli/cli/releases/tag/v2.9.0) is out and brings some nice new features around [labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5nzx7sgiemdi5159sd3a.png)

{% embed https://github.com/cli/cli/pull/5452 %}

As recently I felt the need (for organizational level reporting) to synchronize labels on distinct repos (see [dedicated feedback](https://github.com/github/feedback/discussions/15300)) :
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rjl5nr77zparqnbpjcje.png)
 
, this latest release was the perfect match ❣️


## 🎞️ The demo

A short video worths a thousand words so here go 👇
{% youtube XhaqCqv1vWA %}


## 📜 Movie script


⚠️ **Replace with your account**⚠️


```shell
clear

# 🤔 So a new release is avilable for Gtihub Cli ❔
# 👉 What's new on v2.9.0... let's find out 👇  
gh release view v2.9.0 --repo cli/cli

# 🎁 ... and what is cli/cli #5452 "label clone" feature ❔
gh issue view 5452 --repo cli/cli

# 🆗 Let's give it a try ❣️

# 1️⃣ Create a master repo 
gh repo create gh-cli-demo-labels-master --public 

# 🏷️ See labels on the newly created repo 👇
gh label list --repo adriens/gh-cli-demo-labels-master

# ➕ Create a custom label 🦩
gh label create SOMETHING_PINK --description "I love pink things" --color FFC0CB --repo adriens/gh-cli-demo-labels-master

# ✅ And check it has been created  👇
gh label list --repo adriens/gh-cli-demo-labels-master

# 🔍 Look for the newly created label 👇
gh label list --repo adriens/gh-cli-demo-labels-master | grep PINK

# ➕  Now, create a new repo...
gh repo create gh-cli-demo-labels-synced --public 

# ... List existing labels on te newly created repo
gh label list --repo adriens/gh-cli-demo-labels-synced

# ✅ Check that the PINK label does not exists
gh label list --repo adriens/gh-cli-demo-labels-synced | grep PINK

# 🪄 Sync labels ✨
gh label clone adriens/gh-cli-demo-labels-master --repo adriens/gh-cli-demo-labels-synced

# 🕵️ See if the clone command did work 🤞
gh label list --repo adriens/gh-cli-demo-labels-synced | grep PINK

# 🎆 Job done 🤸

# 🧽 Cleanup the mess 🧼
gh repo delete adriens/gh-cli-demo-labels-master --confirm
gh repo delete adriens/gh-cli-demo-labels-synced --confirm

# 🎬 That's all folks
gh repo view cli/cli

# 🌟 Go like it 🌟
gh repo view cli/cli --web
```

## 🔖 Resources

- 🎞️ [Github CLI playlist](https://youtube.com/playlist?list=PL7GdrgVAWcDgnslVa345j1xpjFJx9IvrE) on [`DevOPS LABS`](https://www.youtube.com/channel/UCcbQ_euR84DKOf_-ksI5_GQ)
- [Github CLI homepage](https://cli.github.com/)
- [`cli/cli` Manual](https://cli.github.com/manual/)
- [`cli/cli` on Github](https://github.com/cli/cli)
