---
name: opt-temps-attente-agences-sdk
url: https://github.com/adriens/opt-temps-attente-agences-sdk
description: "SDK Java des temps d'attente en agence OPT.nc"
language: Java
topics: []
stars: 0
created_at: 2020-03-09
updated_at: 2020-12-09
archived: false
has_readme: true
---

[![](https://jitpack.io/v/adriens/opt-temps-attente-agences-sdk.svg)](https://jitpack.io/#adriens/opt-temps-attente-agences-sdk)



# tempsattente-sdk

Java SDK pour le temps d'attente dans les agences OPT de Nouvelle-Calédonie

## Utiliser

### Dépendance

Ajouter le dépôt:

```xml
<repositories>
  <repository>
    <id>jitpack.io</id>
    <url>https://jitpack.io</url>
  </repository>
</repositories>
```

Puis la dépendance:

```xml
<dependency>
  <groupId>com.github.adriens</groupId>
  <artifactId>opt-temps-attente-agences-sdk</artifactId>
  <version>${opt-temps-attente-agences-sdk.version}</version>
</dependency>
```

### Code snippet

```java
System.out.println("<" + Agences.getAgences().size() + "> agences trouvées");
System.out.println(Agences.getAgences());
System.out.println("<" + Agences.getAgences(Commune.NOUMEA).size() + "> agences trouvées pour <" + Commune.NOUMEA + ">");
System.out.println(Agences.getAgences(Commune.NOUMEA));
System.out.println("Correspondance trouvée pour l'ID 4177 : " + Agence.getAgence("4177").toString());  
System.exit(0);
```