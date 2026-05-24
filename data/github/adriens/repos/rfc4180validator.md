---
name: RFC4180Validator
url: https://github.com/adriens/RFC4180Validator
description: "POC in progress"
language: Java
topics: []
stars: 0
created_at: 2019-05-06
updated_at: 2019-05-16
archived: false
has_readme: true
---

# Install (from source)


Compile the java part :

```
mvn clean package
```

Next, locally build the docker image :

```
docker build -t rfc4180-validator .
```

Finally, perform your lint :


```
docker run -v C:\Users\3004sal\Documents\NetBeansProjects\RFC4180Validator\input:/input rfc4180-validator
```


# jib build

In your `~/.m2/settings.xml` put your Docker hub

```xml
<server>
    <id>registry.hub.docker.com</id>
    <username>rastadidi</username>
    <password>XXXXXXX</password>
</server>
```

Then build/push :

`mvn compile jib:build`

# Install from DockerHub

```
docker pull rastadidi/rfc4180-validator:latest
```

## Run the test

Simply :

```
docker run -v C:\Users\3004sal\Documents\NetBeansProjects\RFC4180Validator\input:/input rfc4180-validator
```