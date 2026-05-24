---
name: excuses-sdk
url: https://github.com/adriens/excuses-sdk
description: "Enfin un SDK pour des excuses !"
language: Java
topics: []
stars: 0
created_at: 2021-09-20
updated_at: 2021-09-25
archived: false
has_readme: true
---

[![](https://jitpack.io/v/adriens/excuses-sdk.svg)](https://jitpack.io/#adriens/excuses-sdk)

# 😆 Des excuses pour nous les "informaticiens" 😆

# Usage

## 👉Prérequis

- Avoir [`sdkman`](https://sdkman.io/) installé
- Installer [JBang!](https://www.jbang.dev/documentation/guide/latest/installation.html) :
```shelll
sdk install jbang
```

Voila, c'est prêt.

## 🚀(J)Bang! sur les excuses !

Pour une expérience optimale depuis le votre shell qui vous permettra de trouver
des excuses de la manière la plus **efficace et discrète** possible :

```shell
jbang alias add --name excuses https://github.com/adriens/excuses-sdk/blob/main/nope.java
# Check des alias
jbang alias list
# Appel de excuses
jbang excuses -c boulot
```

Pour récupérer rester à jour et **toujours disposer des meilleures excuses** soumises par la communauté,
mettre à jour le cache :

```shell
jbang cache clear
jbang excuses -c boulot
```

# 😈 Pour les développeurs : `excuses-sdk`

Tu veux intégrer un moteur d'excuses dans tes softs java :

## Dépendance

```xml
<repositories>
  <repository>
    <id>jitpack.io</id>
    <url>https://jitpack.io</url>
  </repository>
</repositories>
```

```xml
<dependency>
  <groupId>com.github.adriens</groupId>
  <artifactId>excuses-sdk</artifactId>
  <version>Tag</version>
</dependency>
```

## Code

```java
Excuses excuses = new Excuses();
//tes collègue te gonflent avec le sport ?
List<Excuse> exc = excuses.getByCategory("Sport");
```


# 📑 TODO

- [x] Implement jbang scripts
- [x] Create REST API : [Work In Progress](https://github.com/adriens/excuses-api)