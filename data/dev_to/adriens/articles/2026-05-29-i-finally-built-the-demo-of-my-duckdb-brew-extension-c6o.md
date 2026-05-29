---
comments: 0
id: 3735712
is_dev_challenge: true
published_at: '2026-05-29T08:07:18Z'
reactions: 0
reading_time_minutes: 2
tags:
- devchallenge
- githubchallenge
- datascience
- security
title: 📊 I (finally) built the demo of my duckdb brew extension
url: https://dev.to/adriens/i-finally-built-the-demo-of-my-duckdb-brew-extension-c6o
---

*This is a submission for the [GitHub Finish-Up-A-Thon Challenge](https://dev.to/challenges/github-2026-05-21)*

## 💭 Where it comes from

In the previous [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21) I submitted a realization ; a `duckdb` extension to make `brew` packages reporting easier for analysis and security/audit concerns : 

{% embed https://dev.to/adriens/built-a-duckdb-community-extension-for-brew-4k6f %}

Since that my extension got accepted as part of community extensions (see [dedicated page](https://duckdb.org/community_extensions/extensions/brew)), I maintain it along `duckdb` releases and have an constant 824 downloads/month, slowly gaining in popularity : 

{% twitter 2058293935114801558 %}

I've provided a set of ready to use `SQL`, yet for some it may not show the full potentiel that I had in my head : I needed to make it more visual with dataviz and professionan datascience tools.

I must confess I was a bit procrastinating that part... But this DEV Challenge PROMPT triggered the action!

## 🤗 What I Built

<!-- Provide an overview of your project, where it started, and what it means to you. -->

I have created a Python based Quarto Notebook that generates a nice looking pdf report, thanks to the extension, ad put Graph Datascience in it.

## 🍿 Demo

{% youtube 7oVyu5jouxU %}

## 🤔 The Comeback Story

<!-- Tell us where the project was before and what you changed, fixed, or added to finish it up. -->

## 🦥 My Experience with GitHub Copilot

I built the Quarto notebook within 2 hours of prompting before getting out of tokens : 


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/99fkl0m9k49pf2fea0qb.png)



<!-- Explain how GitHub Copilot supported your process. -->

<!-- Don't forget to add a cover image (if you want). -->

<!-- Team Submissions: Please pick one member to publish the submission and credit teammates by listing their DEV usernames directly in the body of the post. -->

<!-- Thanks for participating! -->