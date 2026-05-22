---
comments: 9
id: 2200466
is_dev_challenge: true
published_at: '2025-01-11T12:18:43Z'
reactions: 17
reading_time_minutes: 2
tags:
- devchallenge
- githubchallenge
- ai
- go
title: '⏳GitHub Copilot 1-Day Build Challenge : eol, a tiny Go client to manage eols'
url: https://dev.to/adriens/github-copilot-1-day-build-challenge-eol-a-tiny-go-client-to-manage-eols-j
---

## What I Built

A very raw & basic implementation of the famous [`hugovk/norwegianblue`](https://github.com/hugovk/norwegianblue) - aka. `eol` - wich is:

> _"CLI to show end-of-life dates for a number of products."_

See below about the tool and API:

{% embed https://dev.to/optnc/manage-eols-like-a-boss-with-endoflifedate-2ikf %}

## Demo

{% youtube https://youtu.be/zcXKJ1KPn28 %}

## Repo

{% embed https://github.com/adriens/eol  %}

## Copilot Experience

I only used GH Copilot Chat to code this app as I almost know nothing about Go...but I find its distribution much nicer...

The whole code was made from prompting, including the workspace creation at the very beginning of the project.
I first started to ask to implement the `--list` option by providing him the most simple API endpoint. It almost worked out of the box : I did a very few prompts to make it modify the resulting behavior.
Then I added the most interesting option to get a single product details, print a formatted table, add colors according to eol dates, print console output with the GH `markdown` flavor.

I struggled a bit with non well structured output types from the API that are sometimes boolean or dates...

**👉 Finally I asked it to create the `README.md` file and that made the first running prototype.**

## Conclusion

I really **enjoyed a lot the resulting prototype I manage to get within almost 2 hours** and it gave me the confirmation that I wanted to spend more time to make a clean code and lear more about Go best practices and probably use [Cobra.dev](https://cobra.dev/) (_A Framework for Modern CLI Apps in Go_) to learn while building something fun yet useful.