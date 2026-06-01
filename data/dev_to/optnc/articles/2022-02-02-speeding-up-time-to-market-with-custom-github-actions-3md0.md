---
comments: 0
id: 974401
is_dev_challenge: false
published_at: '2022-02-02T03:59:21Z'
reactions: 1
reading_time_minutes: 4
tags:
- github
- deployment
- devops
- docker
title: Speeding Up Time to Market with Custom Ansible GitHub Actions
url: https://dev.to/optnc/speeding-up-time-to-market-with-custom-github-actions-3md0
---

## Intro

Recently, we started to migrate our onPremise Jenkins/Gitlab based Continuous Integration platform to Github.com.

After having migrated our code and build tool from `gradle` to `maven`, implemented all the classic CI, including Continuous Delivery,

> we wanted to go one step further : achieve Continuous Deployment.

This post is about how we achieved that, while relying on hybrid onPremise and Cloud services, and the software we developed to achieve that, with an industrial approach.


## :blue_book: Our mantra : getting platform oriented

Our core mantra that would drive all of our DevOPS decisions was to

> perform a weak couplage... and avoid self hosted runners.

OPS would deliver us a ready to use platform (servers and deployment pipeline) while programmers (Dev and Ops) should integrate the OPS pipeline to implement the Continuous Deployment Pipeline.

## :zap: The pipeline

Finally, we should get a whole pipeline as follows :

1. **Cloud** : Code and deliver assets/artefacts or Docker images on Github.com
2. **onPremise**: Delegate deploy tasks by calling dedicated & ready-to-use [Ansible Tower Job](https://access.redhat.com/products/ansible-tower-red-hat)

Below see the same version deployed to both environments :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mkofd1q8z2eb58bnm38u.png)

On each deployment you can see the reference to the GH Action :


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ppkzug28sej4mvd1i438.png)

## :rocket: Deployment cases

We finally achieved the following deployment pipeline :

- **When a PR is merged into the `develop` branch** : trigger a deployment on integration environment
- **When a released is triggered** : a deployment in Qualification is triggered, but waiting for a reviewer to accept it
- **For production environment** : same approach as previous item, eventually with different reviewers

## :package: Package and deliver the Tower Action

To deliver the deployment, we naturally have chosen to implement a dedicated Github Action so other developers could use it too to implement deployment workflows.

Finally we managed to release this as a public action on [Github Action Marketplace](https://github.com/marketplace/actions/deploy-with-tower-ansible) :  

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1w9oprlr95t0rvxq2d05.png)

:point_right: Notice that we did put a lot of care to be able to produce public code, be able to manage secrets and not being too specific to our needs. **This is an important part of our philosophy.**

You can get a closer look as the action sourcecode below : 

{% github opt-nc/tower-deploy-action %}

## :gear: Maintaining the pipeline

> As any kind of dependency, a Github Action needs to be maintained, and as an end user, **you need to monitor that** (I mean... you really have to).

Fortunately, [since 2022/01/31](https://github.blog/2022-01-31-dependency-graph-now-supports-github-actions/) this can now be achieved through [the standard dependency graph](https://docs.github.com/en/enterprise-server@3.1/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph) (the same way you monitor through any package managers like npm, NuGet, Maven, or RubyGems).

From any repository which uses Actions, you can now see your Actions workflows listed alongside any other dependencies in the Insights/Dependency Graph experience:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6vv9g1su0bwucg9plm0f.png)

The [dependency graph](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph) is the foundation of GitHub’s supply chain security capabilities because understanding what you depend on is a crucial first step toward securing software.

> We can configure `Dependabot` version updates to keep your Actions dependencies up to date automatically... I mean as part of your development workflow through automated Pull requests.

See [official Github Blog Post](https://github.blog/2022-01-31-dependency-graph-now-supports-github-actions/) about this topic.

## Benefits

During this first Github Action development we had the following benefits : 

- Even **better code-related collaboration** with OPS Teams for code around Tower calls and security concerns
- **Better questions and responsibility** around deployment and the deployment reviews and roles
- Generate DevOps **metrics** to get data driven around on this area
- **Optimize workflow to save money** (switch from Docker image to js under investigation) : **the faster your pipeline runs, the less money you spend**
- This discipline behind the mantra opens the door for a very wide range of deployments, **making us very productive at no additional development cost**
- As on Github.com CPU time and storage come at a cost, cost and performance do now are investigated since the very beginning and are data-driven : **we have started to [shift left](https://dev.to/t/shiftleft) on these aspects too**

## Resources

- Keeping an eye on GH [public roadmap](https://github.com/github/roadmap/issues) for more information about upcoming supply chain improvements in this area.

## :cinema: Intro to Gh Actions

{% youtube R8_veQiYBjI%}

## :pray: Acknowledgements

I really want to thank all the people that made this first success possible : Dev, OPS, financial services, RSSI and CIO for their confidence. Without all this engagement this pipeline would have never been come true.