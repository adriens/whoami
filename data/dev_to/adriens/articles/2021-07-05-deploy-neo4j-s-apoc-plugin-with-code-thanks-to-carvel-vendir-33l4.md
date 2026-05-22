---
comments: 3
id: 747447
is_dev_challenge: false
published_at: '2021-07-05T01:42:54Z'
reactions: 6
reading_time_minutes: 3
tags:
- docker
- neo4j
- devops
- wecoded
title: Deploy Neo4J's APOC plugin with code thanks to CARVEL vendir
url: https://dev.to/adriens/deploy-neo4j-s-apoc-plugin-with-code-thanks-to-carvel-vendir-33l4
---

## :rocket:Teaser

[CARVEL](https://carvel.dev/)

> "provides a set of reliable, single-purpose, composable tools that aid in your application building, configuration, and deployment to Kubernetes."

Let's see how `vendir`, which is one of these tools can help deploy things easier, even if you don't work with kubernetes.

## :bookmark_tabs:Introduction

[Neo4J](https://neo4j.com/) is a very nice way to play with a Graph Database.

Is is delivered as packages, [as a Service](https://neo4j.com/cloud/) and as a [Docker image](https://neo4j.com/developer/docker/).

Neo4J features can be extended thanks to plugins, one of them is [APOC](https://neo4j.com/labs/apoc/) :

{% github neo4j-contrib/neo4j-apoc-procedures %}

Here are [some features](https://neo4j.com/labs/apoc/4.2/) APOC adds to Neo4J :

- [Import](https://neo4j.com/labs/apoc/4.2/import/) `csv`, `json` and even `xls` files
- [Connect to any jdbc driver](https://neo4j.com/labs/apoc/4.2/database-integration/) to we can query any external datasource
- [Natural Language Processing (NLP)](https://neo4j.com/labs/apoc/4.2/nlp/)
- Run http queries so we can load datas by calling REST services
- Provide ready to use [graph algorithms](https://neo4j.com/labs/apoc/4.2/algorithms/)
- [Generate documentation](https://neo4j-contrib.github.io/neo4j-apoc-procedures/3.5/schema/meta-graph/) thanks to graph introspection
- ...

All you have to get done do is :

1. Download the APOC library
2. Drop the plugin in a specific directory

## :gift:Distribution flavors

Let's focus on two specific flavors : 

- The GUI mode
- The docker mode

### GUI mode

The GUI mode is very helpful and packages all install operations in a very smooth way, perfect to perform demos, explain each step, but requires a quite important amount of clicks. Also, you get wizard to install APOC library the proper way.

This mode is very well suited for live demos as it provide nice visuals that make it easier for you to explain concepts while playing with them.

### :whale:Docker mode

This mode makes it possible to run everything from the code. Still, **you have to perform some additional an eventually manual tasks** :

1. Download the APOC jar
2. Put the `jar` in the right directory  and give the proper privileges

:point_right:The aim of this post is to document this to make things even easier with a tool called [CARVEL vendir](https://github.com/vmware-tanzu/carvel-vendir)

## CARVEL vendir

The aim of `vendir` is to *declaratively state directory's contents.*

You can :

> "Sync any number of data sources into a consistent structure by writing a YAML definition. Share the definition or generated lockfile and ensure that your whole team is working under the same expectations."

{% github vmware-tanzu/carvel-vendir %}

## Doing the whole thing from the shell

First, install `vendir` :

On linux :

```bash
brew tap vmware-tanzu/carvel
brew install vendir
```

On Windows :

```bash
choco install vendir
```

Next, create `vendir.yml` file with the following contents : 

```yaml
apiVersion: vendir.k14s.io/v1alpha1
kind: Config
directories:
- path: plugins/
  contents:
    - path: .
      githubRelease:
        slug: neo4j-contrib/neo4j-apoc-procedures
        tag: 4.3.0.0
        disableAutoChecksumValidation: true
        assetNames: ["apoc-*-all.jar"]
```

Let's assume you have the following directory hierarchy :

```
vendir.yml
|__plugins
```

:fireworks:Next, let `vendir` do the job :

```bash
vendir sync
```

Finally, run the docker image and enjoy a fully operational (customize the volumes mapping) Neo4J instance with pre-installed APOC :

```bash
docker run \
    --name vendir-loves-neo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v /vagrant/import:/var/lib/neo4j/import \
    -v /vagrant/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/S3CR37 \
    --env NEO4J_dbms_security_procedures_unrestricted=apoc.\\\* \
    neo4j:latest
```

You're done and the installation process is totally automated and of course self-documented.

Now you can enjoy APOC extension. For an example, check how to [import PostgreSQL relational model in Neo4J](https://www.linkedin.com/pulse/digging-mining-datas-structures-extracting-from-neo4j-adrien-sales/) to run [cypher](https://neo4j.com/developer/cypher/) queries and create nice looking [Gephi](https://gephi.org/) graphs.

## Conclusion

Hopefully this post has helped you make install process smoother, smarter, and made you discover [CARVEL tools](https://github.com/vmware-tanzu/carvel.dev).

{% github vmware-tanzu/carvel.dev %}