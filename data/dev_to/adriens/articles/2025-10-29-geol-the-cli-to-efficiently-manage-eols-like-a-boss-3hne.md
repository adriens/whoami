---
comments: 30
id: 2951766
is_dev_challenge: true
published_at: '2025-10-29T20:39:59Z'
reactions: 3
reading_time_minutes: 3
tags:
- devchallenge
- hacktoberfest
- opensource
- devops
title: ⏳geol, the cli to efficiently manage EOLs like a boss
url: https://dev.to/adriens/geol-the-cli-to-efficiently-manage-eols-like-a-boss-3hne
---

*This is a submission for the [2025 Hacktoberfest Writing Challenge](https://dev.to/challenges/hacktoberfest2025): Maintainer Spotlight*

## ⏱️ `geol` in `5'` for impatients

{% youtube ZqiXogK2fSw %}

## 🤗 Building ideas & patterns before software

First of all, I would like to point **what makes my core motivation & energy last, what keeps me in movement : my curiosity.**
I only understood recently that **this is curiosity and the satisfaction we get once got answers that (from my POV) makes things possible.**

Of course we are building software or products, but first, **I want to focus on creating and experimenting news ways of viewing problems that affect us and prototype new ways of fixing issues** (regardless of programming languages or technologies) or rewiring known problems, then share these techniques and POVs with others to confront perspectives.

**Nothing excites me more that seeing the solution come to life**, talk with my teammates about how to tweak an output, what to remove until we get something really useful and pleasant.

Some call this being nerd... I don't care but **what I enjoy the most is talking about software engineering, DEVOPS and architecture while enjoying a coffee, drawing something on a paper**, challenging perspectives and make it happen on a schedule, at a regular pace... and gain experience.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cv0jgkgzq4g9j8313rrq.png)



## 💭 About the core idea

Back in time time in January, I submitted a first try to porting [`eol`](https://github.com/hugovk/norwegianblue) to a `golang` stack : 

{% embed https://dev.to/adriens/github-copilot-1-day-build-challenge-eol-a-tiny-go-client-to-manage-eols-j %}

Also I previously talked - a lot - about these data and why it matters: 

{% twitter 1968410713480733162 %}

I wanted to push  ~~a bit~~ much  further around around stack lifecycle management and bring `DEVOPS`,`DEVSECOPS` and `SECOPS` to the front and imagine complementary practices to automate things around that.

After a paper and pen ideation session :

{% twitter 1974974775836754362 %}

I finally opted for a full unboxing video that would focus on the MVP, from start to end.

## 🍿 Unboxing demo

{% youtube vhFXWGqB_-g %}

## 🧑‍🤝‍🧑 Team mates

Innovation is much more interesting when it's achieved with other people, below the [core team](https://github.com/opt-nc/geol?tab=readme-ov-file#%E2%80%8D%E2%80%8D-core-team-and-roles):

- [👨 Adrien](https://dev.to/adriens) : `adriens`
- [👨 Vinh](https://dev.to/supervinh) : `supervinh`
- [👱🏻‍♀️ Michèle](https://dev.to/mbarre) : `mbarre`

## 🎯 Our `MVP`

I designed a [`MVP` milestone](https://github.com/opt-nc/geol/milestone/1) to be sure to be ready to deliver for D-day and at last deliver the demo:

{% embed https://github.com/opt-nc/geol/issues/4 %}

## 🤩 What we learned and techniques we developed on the journey

### 🧰 Stack

- [Charmbracelet](https://github.com/charmbracelet)
- [`charmbracelet/fang`](https://github.com/charmbracelet/fang) _"The CLI starter kit"_
- [`charmbracelet/lipgloss`](https://github.com/charmbracelet/lipgloss) _"Style definitions for nice terminal layouts 👄"_
- [`Cobra`](https://github.com/spf13/cobra)
- [`gemini-cli`](https://github.com/google-gemini/)
- [`charmbracelet/crush`](https://github.com/charmbracelet/crush) _"The glamourous AI coding agent for your favourite terminal 💘"_
- [`GoReleaser`](https://github.com/goreleaser/goreleaser)
- [`go-task/task`](https://github.com/go-task/task)
- [`pandoc`](https://pandoc.org/)
- [`asciidoctor`](https://asciidoctor.org/)
- [`fish-shell/fish-shell`](https://github.com/fish-shell/fish-shell) _"The user-friendly command line shell."_
- [`aquasecurity/trivy`](https://github.com/aquasecurity/trivy) _"Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more"_

### ➿ `cli` design tuning with AI

I used `gemini-cli` and `crush` to continuously evaluate & improve the design of our `cli` : which command to add, examples to provide, better options, option names, sub-commands layouts,...

👉 Our goal was to achieve zero-prompts answers, eg. : 

{% twitter 1970676017556865268 %}

1. Ask the agent _"learn to use `geol` thanks to `man` pages"_ (it appeared than, after benchmarking, `man` was the best option)
2. Challenge the assistant to produce new kind of documents, for example with the help of third parties `cli` like `trivy` or `grype`

## 📰 Original report productions

I challenged `geol` and `trivy` as data producers, `gemini-cli` as thinker to efficiently produce `LaTeX` some original reports pretty easily and share them:

{% twitter 1971740458331394521 %}

## 🔭 Further ideas

Below some features to be implemented that excites us a lot:

- Stack survey : [🔔 Lock, warn & report watch stack 👀 ](https://github.com/opt-nc/geol/issues/15)
- Data exports : [📤 Add `export` and `duckdb` sub-command : `geol export duckdb`](https://github.com/opt-nc/geol/issues/96)
- Documentation export : design still in progress 😅 but preparing some cool work
 
## 🙌 Last words

This project makes us learn a lot about software packaging, distribution, make choice to be sure to deliver the most ~~important~~ useful features, also carefully not implement the things that should not be... and learn learn and learn about free software.