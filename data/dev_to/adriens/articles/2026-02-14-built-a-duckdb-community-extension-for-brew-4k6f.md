---
comments: 5
id: 3232987
is_dev_challenge: true
published_at: '2026-02-14T03:55:40Z'
reactions: 8
reading_time_minutes: 3
tags:
- devchallenge
- githubchallenge
- cli
- githubcopilot
title: 🦆Built a duckdb community extension for brew
url: https://dev.to/adriens/built-a-duckdb-community-extension-for-brew-4k6f
---

*This is a submission for the [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21)*

## 🤓 What I Built

Sometimes ago I got asked to report what I installed on my Ubuntu... and like many people it turned out I installed various softwares in very various ways : 

- `apt`
- `snap`
- [`brew`](https://brew.sh/)
- `pip` or `uv` (but mostly in virtual environments)

Basically, at first I started with that kind of data-analysis and dataviz (and made it open source, see [`adriens/ubuntu-rmarkdown-report`](https://github.com/adriens/ubuntu-rmarkdown-report)):


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xzhprk9t7dt9q83d90xg.png)

So I started to **look around how I could efficiently automate that with standard data tools to make this work look like a piece of cake (avoid boilerplate `R` code in my case).**

I then found the great [`osquery`](https://osquery.io/) initiative, which makes it possible to query any operating system metric or information from a simple `SQL` : 

> _`osquery` exposes an operating system as a high-performance relational database. This allows you to write SQL queries to explore operating system data. With osquery, SQL tables represent abstract concepts such as running processes, loaded kernel modules, open network connections, browser plugins, hardware events or file hashes._

But when I wanted to query installed `brew` packages, it turned out that I had to write an extension (which is very well documented).

So I finally opted to write a dedicated `Rmarkdown` notebook, started to play with custom dataframes (easy to share)... **but pretty soon I felt like it would be much more convenient to be able to query this data within `duckdb` itself so it could make the data much much easier to get in various usecases (`R`, `Python`, `Go`, ... ).**

## 💡 The idea : the `duckdb` extensions community

Therefore, I decided to build - and heopefully to get it accepted - a [`duckdb brew` community extension](https://duckdb.org/community_extensions/extensions/brew) so I can build reports on the installed homebrew packages from simple `SQL` and benefit from the amazing `duckdb` ecosystem and a very large amount of language bindings and data tools:

{% twitter 2016990414583321074 %}

## 🍿 Demo

Official `duckdb`'s [`brew` DuckDB CE extension's page.](https://duckdb.org/community_extensions/extensions/brew) 

Below the whole story, from the function table concept in various databases, to the pitch, including the developer experience with Copilot CLI:

{% youtube -BkiKuB1noI %}

## 📷 Screenshots 

### 📈  Historical brew install

When doing reports, I felt the need to know how many brew packages I installed, and when:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6r47y53f6dp80dh55ufp.png)


### 🌌  Graph Dependencies

For security analysis, it makes sense to be aware of the centrality of the installed software.

It is now made easy to produce and chart, see below:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4yv00v2czi0xwwjelzmr.png)


### 🐧 `SQL` reports from terminal

Then it's really very easy to do reports from the terminal itself:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/q72rkg4mw38vkhv7wbn9.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7jvr0ftjfk7a3bwv2aoh.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qa52du73d2o0dc9an5jg.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/uo7unfh9ddbugdklgf1f.png)

## 🤓 My Experience with GitHub Copilot CLI

Below my complete development workflow setup, which consists in three panels : 

1. **The top left one** : to run `make` commands by myself, which made things easier to handle
2. **The bottom left one** : the GH Copilot CLI to which I asked to add features, write nice commit messages, check CI for failures, write Release Notes, create tags and releases
3. **The right one** : dedicated to try the output binary by myself, purely manual written SQL statements etc...

This how it looks::

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3e02z22cfuf31wt6ugu3.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jvhan8qqlsnl9uob7mph.png)

Video announce : 

{% twitter 2019167438546563160 %}

## 👨‍🎓 Lesson learned : `CI`, tests and lint first

The CLI experience is very responsive, but what I would keep in mind and would like to put the maximum emphasis is how crucial are about build automation and CI : 

- Tests
- Linting process
- Code formating rules

The more they are part of the build tools and CI pipeline, the more the vibe coding experience is efficent and **the more we build trust with the generated code.**

In my case, `duckdb` community provided a repo template (see [`duckdb/extension-template`](https://github.com/duckdb/extension-template)) with all the required stuff **so I could very efficiently start to work, which means : get continuous feedback from CI and give it immediately to Copilot for continuous improvement** without having to ask help to community. 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/r2p0map40k632kfksz31.png)
](https://github.com/adriens/duckdb-brew/actions/runs/21662489997)


## 📑 Resources

- Extension source code : [`adriens/duckdb-brew`](https://github.com/adriens/duckdb-brew/)
- `duckdb brew` extension homepage : https://duckdb.org/community_extensions/extensions/brew
- [`adriens/ubuntu-rmarkdown-report`](https://github.com/adriens/ubuntu-rmarkdown-report)