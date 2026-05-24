---
name: ridetnc-api
url: https://github.com/adriens/ridetnc-api
description: ""
language: Java
topics: []
stars: 0
created_at: 2021-08-07
updated_at: 2021-08-09
archived: false
has_readme: true
---

![Docker Pulls](https://img.shields.io/docker/pulls/rastadidi/ridetnc-api)
![Docker Stars](https://img.shields.io/docker/stars/rastadidi/ridetnc-api)

# :grey_question:About

`ridetapi-nc` is an API that wrapps an easy to use set of endpoints on top of
[New Caledonia Open Data Dataset](https://data.gouv.nc/explore/dataset/entreprises-actives-au-ridet/).

The aim of this API is to make things easier than ever to get that datas.

# :joystick:Katacoda Playground

You can give a try to this API thanks to this [dedicated KataCoda scenario](https://www.katacoda.com/rastadidi/courses/open-data/ridet-nc).

# Related stuff

- [New Caledonia Open Data Dataset](https://data.gouv.nc/explore/dataset/entreprises-actives-au-ridet/)
- [Open Data Soft documentation](https://help.opendatasoft.com/apis/ods-search-v1/#dataset-search-api)
- [Online Isee.nc form](https://avisridet.isee.nc/)
- [ridetnc-api on DockerHub](https://hub.docker.com/r/rastadidi/ridetnc-api)

# Run API by yourself

## Maven

```
mvn spring-boot:run
```

## :whale:Docker

```
sudo docker run -d --name ridets-nc -p 8080:8080 rastadidi/ridetnc-api:latest
sudo docker ps
```

# Usage

- Swagger : http://localhost:8080/
- Get a given ridet : `http://localhost:8080/ridet/0426049`
- Search ridets : `http :8080/ridets q==sports page==1`

# Call examples

Get infos about the **unique** society that has ridet `0426049` :

```
http :8080/ridet/0426049
```

Check if a society does exist (will return ` "status": 404`)

```
http :8080/ridet/04260499
```

Get a list of societies and search with a matching keyword (send back society where at least one field
contains the query). Get the first page :

```
http :8080/ridets q==sports page==1
```

# Developers section

## jib build

In your `~/.m2/settings.xml` put your Docker hub

```xml
<server>
    <id>registry.hub.docker.com</id>
    <username>rastadidi</username>
    <password>XXXXXXX</password>
</server>
```

Then build/push to DockerHub :

```
mvn compile jib:build
```

## TODO

- [x] Push to DockerHub
- [x] Write DEV.to demo Post
- [ ] Post to contribs on OpenData Gouv.nc
- [ ] Release with jreleaser
- [ ] Publish doc with Slate