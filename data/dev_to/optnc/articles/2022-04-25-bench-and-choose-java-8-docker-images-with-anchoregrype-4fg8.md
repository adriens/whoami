---
comments: 3
id: 1061131
is_dev_challenge: false
published_at: '2022-04-25T22:19:42Z'
reactions: 7
reading_time_minutes: 4
tags:
- docker
- security
- devsecops
- infosec
title: ⚖️ Bench (and choose) Java-8 docker images with anchore/grype
url: https://dev.to/optnc/bench-and-choose-java-8-docker-images-with-anchoregrype-4fg8
---

## 🛡️ Context : security 🐳

We recently started to put [`grype`](https://github.com/anchore/grype) and [Anchore Container Scan](https://github.com/marketplace/actions/anchore-container-scan) in our (GH based) CI pipeline.

In the mean time, we started to **spread container security culture accross Dev & OPS teams**, especially around `grype` tooling (which is very easy to handle).

Now ...

> all the people who produce and release docker images have `grype` installed on their workstation... hence helps promote shiftleft culture

Next to that we wanted to **automate, monitor and alert** on **security issues** so we'll be able to run a proper maintenance pipeline **by linking issues to code actions.**

## 🛤️ Action

Finally we created the following scheduled workflows to monitor our `stable` and `latest` tags (the ones we deploy)... and be noticed when they fail according to 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1lx0dkvn67348p9gn2dt.png)
 
## 📉 Issue management & kanban

We wanted to be noticed and embed security concerns into our [project planning](https://github.com/features/issues) : we needed to get alerts as issues :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cf1luyumnbr1a5zm5tyq.png)
 
Also, thanks to custom and shared labels accross our organization, it is possible to report these issues globally.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hml6nftnov1irsdvpu84.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p0cak9hm3lwpya0wrajv.png)

Now we get all the required details within the (self updating) issue so we can assign it, investigate, link it to other tasks, assign it to a SCRUM and so many other things.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rmf08i1rimz52clf00u8.png)

## 🚨 Then the real world came to us

For now, we have set the workflow to fail as soon as a `Critical` level has been reached... and here is what we got on one of our projects :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lxf1wr3o0dnjmmmbxruq.png)

These issues were affecting our core java image that was relying on : `openjdk:8-alpine`.

Then here is what we got 😱 👇

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wdlkqtxuc8b2xish5lsi.png)

So I started to count them :

```
grype openjdk:8-alpine | grep Critical | wc -l
grype openjdk:8-alpine | grep High | wc -l
```

Then, with that methodology I could very quickly build the following benchmark : 

| Image | Critical | High | Medium | Low  | Negligible | 
| ---              | ---| ---| --- | --- | ---|
| openjdk:8-alpine | 10 | 55 | 110 | 142 | 0  |
| openjdk:8u102    | 6  | 234| 685 | 140 | 232|
| adoptopenjdk/openjdk8 | 0 | 0 | 8 | 21 | 7  |
| adoptopenjdk/openjdk8:alpine-jre | 0 | 0 | 0 | 0 | 0 |

## ❇️ Jaw dropping `adoptopenjdk/openjdk8:alpine-jre`

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dbksatuikizgbnouvi9w.png)
 

👉 Finally we started to migrate our core java layer from `openjdk:8-alpine` to [`adoptopenjdk/openjdk8:alpine-jre`](https://hub.docker.com/r/adoptopenjdk/openjdk8)

{% embed https://hub.docker.com/r/adoptopenjdk/openjdk8 %}

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8vtkg5l7z4ohs3qe1usq.png)

☝️ Be aware that if under certain circumstances vulnerabilities should be considered as acceptable, it is **possible to create a configuration file to ignore certain matches** : 


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nu1oplik2yltho1cqo9f.png)
 
## ☝️ Conclusion

Thanks to continuous scan and proper alerting we could seriously enhance our core Java runtime for legacy source code that only supports java 8 runtime, 

> we could switch from a **runtime with 10 `Critical` issues** to a runtime with **21 `Low` security issues**.

It is possible to generate [`SARIF`](https://docs.oasis-open.org/sarif/sarif/v2.0/sarif-v2.0.html) vulnerability report so it can be displayed : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ppc4zl7zg3lu50e7hkac.png)

... delivered to other systems. 

See more details about `SARIF` support in `grype` :

{% embed https://github.com/anchore/grype/issues/304 %} 

## 🌌 Further

- [Anchore :  Continuous security checks directly in container image registry](https://anchore.com/container-registry-scanning/) : _ready to play solution (native integration, monitor public & private repos, enforce policies, gain security insights, ready to use reporting)_
- [Snyk report for `openjdk:8-jdk-alpine`](https://snyk.io/test/docker/openjdk%3A8-jdk-alpine)
- [Uploading a SARIF file to GitHub](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)
- [SARIF support for code scanning on Github](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning) _to display results from a third-party static analysis tool  & CodeQL static analysis_
- [Managing container vulnerability risks: Tools and best practices](https://www.csoonline.com/article/3656702/managing-container-vulnerability-risks-tools-and-best-practices.html)
- [The Role of SBOMs in Securing Software Supply Chains by Gartner](https://get.anchore.com/gartner-sboms-report/)

## 🔭 Organisation wide strategy

Finally many strategies are possible : 

- Per-repo strategy : each repo is reponsible of its own monitoring with CI
- Per-org single repo strategy : within a single repo, monitor all published images with CI
- Global & ready-to-use [Container Registry Scanning by  `anchore`](https://anchore.com/container-registry-scanning/) for policy enforcement, security insights

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lvyigfqnylu0lujig8j5.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hg3vy9r98kfq67gulmv5.png)

See global solution below : 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o2r9f2kx49hyqeaqlzxo.png)
 
> Each of these approaches has its pros and cons,... just pick (or create) your own solution to achieve this goal. 
 

## 👀 Remarkable grype issues

Find below some issues :

- [Replacements for the inline scanning script](https://github.com/anchore/grype/issues/600)
- [grype can't detect spring4shell (CVE-2022-22965) ](https://github.com/anchore/grype/issues/704)
- [Add support for cyclonedx 1.4 and VEX](https://github.com/anchore/grype/issues/591)
- [generate fig autocompletion](https://github.com/anchore/grype/issues/604)
- [False positive for alpine package](https://github.com/anchore/grype/issues/601)
- [Consistent sort order for grype output](https://github.com/anchore/grype/issues/709)
- [Add show-grype-output option to show vulnerabilities in console](https://github.com/anchore/scan-action/pull/135)
- [Can't see findings in console?](https://github.com/anchore/scan-action/issues/168)
