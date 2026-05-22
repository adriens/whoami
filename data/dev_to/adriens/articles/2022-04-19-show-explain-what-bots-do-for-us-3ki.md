---
comments: 1
id: 1058241
is_dev_challenge: false
published_at: '2022-04-19T20:49:39Z'
reactions: 5
reading_time_minutes: 2
tags:
- devops
- programming
- productivity
- codenewbie
title: 🦾 Show & explain what BOTs do for us 🧑‍🤝‍🧑
url: https://dev.to/optnc/show-explain-what-bots-do-for-us-3ki
---

## ❔ Context


Everyday, **BOTs and CI are doing more and more things for us**.

At the office, to

> build a shared an efficient digital culture,

it is important for programmers (DEVs & OPS) to explain to middle and top management how this technology helps to :

- ➿ **Maintain** existing source code
- 🚀 **Release** software, new features,...
- ⤴️ **Loop** between the two previous activities

> Still it remains a bit abstract.

The goal of this short post is to show how, from a source code point of view,

> how BOTs are an extension of the team and can (should ?) be considered as "real" programmers...

that help us in our daily missions... and focus on what really matters :

> Innovate, learn, create new features as fast as possible to the market... so they can be released (and then maintained).

## 🎥 Movie show

Visual management is a powerful tool to help understand and gain attention on abstract concepts.
So, to put in evidence how BOTs participate to the teamwork, I thought **a short movie could do the job**.

👉 This is where [`gource`](https://gource.io/) helps :

{% github acaudwell/Gource %}

## 🍿 Enjoy collaboration replay

Within a very simple command line :

```
gource \
    --key \
    --highlight-users \
    --date-format "%d/%m/%y" \
    --hide mouse,filenames \
    --file-idle-time 0 \
    --max-files 0  \
    --background-colour 000000 \
    --font-size 25 \
    --output-ppm-stream - \
    | ffmpeg -y -r 30 -f image2pipe \
    -vcodec ppm -i - -b 65536K movie.mp4
```

We can see :

- how humans and BOTs collaborate
- on what
- on which pace
- on wich parts of the project
- new programmers arrival

{% youtube jwXX2jFKUv8 %}

👉 Notice that from a code point of view you can't see the difference between BOTs code and human... **except that BOTS often modify the same files, according to a same pattern.**

## 🙏 Acknowledgments

Thanks a lot to the programmers who played the role of actors in the movie, **_by order of appearance_** 😉 :

- 👨 [`@lschaeffer313`](https://github.com/lschaeffer313)
- 🧔‍♂️ [`@Dougniel`](https://github.com/Dougniel)
- 🤖 [`DependaABOT`](https://github.com/dependabot)
- 🦾 [`semantic-release-bot`](https://github.com/semantic-release-bot)