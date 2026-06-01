---
comments: 2
id: 1048298
is_dev_challenge: false
published_at: '2022-04-07T22:12:05Z'
reactions: 5
reading_time_minutes: 2
tags:
- security
- serverless
- kubernetes
- devops
title: 🕵️ About Java Bytecode, native binaries & security (short Grype benchmark)
url: https://dev.to/optnc/about-java-bytecode-native-binaries-security-short-grype-benchmark-4ng9
---

## ❔ Intro

We are currently working on the following topics :

- Native Docker images delivery through Github Actions, on various registries (mainly [GHCR.io](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) and [Docker Hub](https://hub.docker.com/u/optnc))
- Java native experience : migration to [Spring Boot Native](https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/) & [Quarkus](https://quarkus.io/) experimentations
- Security for our Images Continuous Deployment pipeline

## 🛡️ Security

For our **source code & dependencies**, we are applying security strategy thanks to Dependabot :

{% embed https://dev.to/optnc/dependency-management-automation-with-dependabot-3l62 %}

...and [GitHub Advanced Security](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/about-github-advanced-security) for some repositories.

## 🖕 Controlling Docker images releases

More and more we release and rely on an ever growing set of Docker images.
To make short, as Software Developers and DEVOPS engineers, the ones that interest us currently are :

- The images we rely on
- The image we build ourselves (on top of previous ones)

👉 **What we  ~~want~~ need to be able to do is : to be able to control the security level of the images we are building...**

⚠️ **And not release them if they do not reach the expected level of security, depending of the target service.**

> _As all services do not have the same criticity, vulnerabilities level may have different impacts on runtime security governance._ 

## 👐 Experimentation and solutions

Fortunately [anchore](https://anchore.com/) provides a set of ready to use tools that helps... a lot :

- [grype](https://github.com/anchore/grype) (_vulnerability scanner for container images and filesystems_)
- [syft](https://github.com/anchore/syft) (_CLI tool and library for generating a Software Bill of Materials from container images and filesystems_)
- [`grype` as a Anchore GitHub Action](https://github.com/marketplace/actions/anchore-container-scan) : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ilqrmjadb1ttgfz8vukw.png)
 
👉 So you can easily protect your Continuous Delivery pipeline  thanks to the `severity-cutoff` :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8zf94iv7slu5dvopsevg.png)
 
## 🤔 Bytecode vs. native impact on security

We wanted to give a quick look at if - and so how - native strategy impacts security, discover the `grype` output below:

{% youtube LPrxUb82wCY %}

## 🔖 Resources

- [`grype`](https://github.com/anchore/grype) on GitHub
- [`grype` Feature request : Optional External Data Source Reference for Maven Packages](https://github.com/anchore/grype/issues/711)

{% embed https://github.com/anchore/grype %}