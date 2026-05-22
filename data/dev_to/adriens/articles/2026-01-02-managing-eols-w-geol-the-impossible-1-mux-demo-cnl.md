---
comments: 4
id: 3083050
is_dev_challenge: true
published_at: '2026-01-02T21:53:35Z'
reactions: 4
reading_time_minutes: 3
tags:
- devchallenge
- muxchallenge
- showandtell
- video
title: '⏳ Managing EOLs w. geol: the impossible 1'' Mux demo'
url: https://dev.to/adriens/managing-eols-w-geol-the-impossible-1-mux-demo-cnl
---

*This is a submission for the [DEV's Worldwide Show and Tell Challenge Presented by Mux](https://dev.to/challenges/mux)*

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i5pigtgt75nqxjsvsaw2.png)


## ❔ What I Built

We have built and maintain [`geol`](https://github.com/opt-nc/geol) a `cli` to help manage, report and survey software EOLs (end-of-life), both for:

- **Interactive** `cli` UX
- **Automates DEVOPS** `CI/CD` pipelines

See below for previous Hacktoberfest hackathon : 

{% embed https://dev.to/adriens/geol-the-cli-to-efficiently-manage-eols-like-a-boss-3hne %}

## ⏱️ My `1'` Pitch Video

{% embed https://player.mux.com/02sUXDw3XC3WkSDfzO2IQiEIfDB9d02yxqEgZ01q1PB0102E %}

## 📑 Demo

- **🤓 Project repository** : [`opt-nc/geol`](https://github.com/opt-nc/geol)
- **🍿 Youtube playlist** : [`geol` playlist](https://www.youtube.com/playlist?list=PL7GdrgVAWcDhTeW8rjUCZVp2Mic1fx-j9) 
- [🗓️ Product Kanban](https://github.com/orgs/opt-nc/projects/28)

## 💭 The Story Behind It

Since a long time now (December 2022), I started to work on following software technical debt, security, ... at scale with: 

- DEVOPS in mind
- Datascience & dataengineering
- Datavisualizations
- DEVSECOPS 

Then I discovered [`endoflife.date`](https://endoflife.date/) website, its API.
Since that day, [I contributed almost 200 PRs](https://github.com/endoflife-date/endoflife.date/pulls?q=is%3Apr+author%3Aadriens+is%3Aclosed) to add/enhance products.

Also, on a daily basis, I used [`hugovk/norwegianblue`](https://github.com/hugovk/norwegianblue) (aka. `eol`) to efficiently browse products end of lifes, for example with `markdown` to efficiently produce Github issues of html reports:

{% embed https://dev.to/adriens/manage-eols-like-a-boss-with-endoflifedate-2ikf %}

Then, years later I wondered what if I could try to push it harder and build a brand new Go based version of `eol`,... which I did during a 48h hours hackathon : 

{% embed https://dev.to/adriens/github-copilot-1-day-build-challenge-eol-a-tiny-go-client-to-manage-eols-j %}

The result was pretty nice, I like the feeling... especially : 

- The _"Eat your own dog food approach"_ (aka. Dogfeeding)
- Freedom to design a brand new client, with a dedicated UX
- Remove the need for Python runtime
- Try some exciting new ideas
- Improve productivity and talk about technical debt around me

Finally we officially created [`geol`](https://github.com/opt-nc/geol) : 

{% embed https://dev.to/adriens/geol-the-cli-to-efficiently-manage-eols-like-a-boss-3hne %}

## ⚙️ Technical Highlights

We wanted to learn as much and take as much profit as possible from Go ecosystem, to adopt the same stack of some tools we love - and admire - to use on a daily basis : 

- Language : `Golang` 
- Delivery : `brew` to deliver/install efficiently as fast - and yet secure - as we want
- Release Management : [`goreleaser/goreleaser`](https://github.com/goreleaser/goreleaser)
- [`spf13/cobra`](https://github.com/spf13/cobra) for CLI
- [`charmbracelet/fang`](https://github.com/charmbracelet/fang) on top of Cobra to give glamour to our cli
- [`charmbracelet/lipgloss`](https://github.com/charmbracelet/lipgloss) for styish terminal outputs : colors, arrays, links, `markdown` display and redirection t files
- `duckdb` as primary export format
- [`osv.dev`](https://osv.dev/#use-vulnerability-scanner) to continuously check for vulnerabilities in our base code
- [Code QL](https://codeql.github.com/) as part of our CI to ensure our tool does not bring security issues
- [Docusaurus](https://docusaurus.io/) for nice professional website (work in progress)
- [`crush`](https://github.com/charmbracelet/crush) and [`gemini-cli`](https://github.com/google-gemini/gemini-cli) to evaluate the design of our cli
- `pandoc` for document post-processing (eg. transform output `markdown` into `html` or `pdf`...)
- `LaTeX` to build the [cheetsheat](https://x.com/rastadidi/status/1995616096351891548)
- The way we an put together `geol` and `trivy` (with `crush` or `gemini-cli`) at work together to build efficient and nice looking technical debt and security reports
- [`distrobox`](https://distrobox.it/) to test install and binaries on various OS and architectures
- Now, I'm starting to focus on what can be done around `geol` outputs to automate reporting, with a professional data-stack, like [`Rmarkdown`](https://rmarkdown.rstudio.com/) or [`quarto`](https://quarto.org/) to make professional looking technical debt reports
- Also, I'm thinking about the most efficient way to share EOL's datas into other systems to make technical debt easier to monitor

## 🐦 Some Tweets showcasing what's achieved and how

### `distrobox`

{% twitter 1987002052460106151 %}

### Putting `geol`, `trivy`, `gemini` & `latex` to work

{% twitter 1989079778058727889 %}

### Building cheetsheat with pure code w. `LaTeX`

{% twitter 1995616096351891548 %}

### Build a website with `docusaurus`

{% twitter 2005772435057242580 %}