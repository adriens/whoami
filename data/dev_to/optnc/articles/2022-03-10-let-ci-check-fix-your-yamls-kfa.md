---
comments: 0
id: 996836
is_dev_challenge: false
published_at: '2022-03-10T02:32:02Z'
reactions: 10
reading_time_minutes: 3
tags:
- github
- yaml
- devops
- docker
title: Let CI check & fix your yamls
url: https://dev.to/optnc/let-ci-check-fix-your-yamls-kfa
---

## 👉 Intro

A few months ago, we have started to migrate our sourcecode [CI & CD to Github.com](https://github.com/features/actions).

Then, both DEV and OPS started to migrate source codes.

It appeared that OPS had to migrate a huge amount of [Ansible](https://www.redhat.com/en/topics/automation/what-is-an-ansible-playbook) related repos from an onPrem Gitlab instance to Github.com, and we wanted to take advantage of linting and code quality of the yamls.

OPS started to develop the migration process so it could be entirely code driven and tested.

What appeared was that we needed to manage that huge amount of code to : 

- :one: **lint** (syntax validity, but for weirdnesses like key repetition and cosmetic problems such as lines length, trailing spaces, indentation, etc)
- :two: **fix/implement lints** feedbacks in a massive way (they were so huge that we could not imagine do that by hand)

OPS did choose to use the following approach : 

- :one: **Lint** with [yamllint](https://github.com/tamere-allo-peter/yamllint)
- :two: **Fix** with [yamlfixer](https://github.com/opt-nc/yamlfixer), which in facts uses `yamllint` in his core

As DEV & OPS are using `yaml` everyday a -bit- lot more ([k8s](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/), [CI configuration](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions), [Spring Boot configuration](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.external-config), ...), we started to 

> think about a common toolbox that we could embed in our CI pipeline, on Github.com.

What we needed to do was to :

1. **Integrate** OPS sourcecode (DevOPS **teamwork**)
2. **Package** it inside as a dedicated GH Action that everyone could add to their pipeline within a few lines of code

## 🛠️ Yaml Fixer

An important work has been done by OPS on [yamlfixer](https://github.com/opt-nc/yamlfixer) so it could be used conveniently from the `cli` :

{% github opt-nc/yamlfixer %}

Still this `cli` needed a Python runtime to be used.

### 🐳 Deliver as a `Docker` image

Then we wanted to distribute it an easier way, which meaned :
> package it as a Docker image.

At that point, DEVs took the relay and implemented Docker release on GH CI, and pushed images on DockerHub under [optnc/yamlfixer](https://hub.docker.com/r/optnc/yamlfixer) :
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pz2by6kdbf410faltst6.png)

 
### 🏃 Deliver as a GH Action

Now, we could use the Docker image to implement the following Public GH Action : 

{% github opt-nc/yamlfixer-action %}

... that could be released on the [Marketplace](https://github.com/marketplace/actions/yaml-fixer) :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f0k521qfwnihag6pgmyu.png)
 
### 🤖 Action usage

Here is the code (and... it's `yaml` 🐔🥚🐣) required to use the action in any workflow :

```yaml
name: Lint yaml files

on: [push]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout my app
        uses: actions/checkout@v2
      - name: Lint yaml files
        uses: opt-nc/yamlfixer-action
        with:
            yaml_file: .github/*.yml
            options: --verbose
            user: ${{secrets.my_user}}
            token: ${{secrets.my_user_password}}
```
:point_right: Notice that the action **creates a new branch and the pull request to be merged into the working branch** so this code activity can be managed and reviewed as any other source code proposal.

# 🎦 Live demo

As a live video worths a thousand words : discover how the Github Action runs on a [dedicated repository](https://github.com/opt-nc/demo-yamlfixer-action) :

{% youtube https://youtu.be/GuloRWeTavY %}

## 📷 Examples in details

### ❌ Rejected PR because of lint failure

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/i6iu8hyolrklfmzywxrr.png)
 
### ✔️ Valid PR coming from GH Action

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d5ufe4c20ziakrfebqqa.png)

And code change review : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/phx1aa6pe5jc92ansosg.png)

## 🪙 ROI

Now, **both DEVs and OPs** are using it to enhance `yaml` quality proactively with the help of CI and `yaml` quality issues are managed on our [daily workflow on GH Issue](https://github.com/features/issues).

:point_right: **Also notice that all the teams using the GH Action have the same level of quality accross the whole organization.**

## 🙏 Acknowledgments 🧑‍🤝‍🧑

A lot of thanks to the team that made this work come true, all on our DEVOPS pipeline : 

- [Jerome ALET](https://github.com/tamere-allo-peter) as core `Yaml Fixer` developer & integrator
- [Michèle BARRE](https://www.linkedin.com/in/michelebarre/) for Docker packaging and GH Action development
- [Daniel SANTOS](https://www.linkedin.com/in/daniel-santos-dev-fullstack/) for its test on DockerHub publish and his continuous feedbacks on this new Gh Action