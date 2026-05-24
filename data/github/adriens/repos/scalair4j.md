---
name: scalair4J
url: https://github.com/adriens/scalair4J
description: "SDK Java pour Scal-Air"
language: Java
topics: []
stars: 0
created_at: 2019-03-03
updated_at: 2019-10-11
archived: false
has_readme: true
---

[![Build Status](https://travis-ci.org/adriens/scalair4J.svg?branch=master)](https://travis-ci.org/adriens/scalair4J)
[![](https://jitpack.io/v/adriens/scalair4J.svg)](https://jitpack.io/#adriens/scalair4J)

# scalair4J

SDK Java pour Scal-Air pour interagir simplement avec ces données.

***Pour l'instant seules les données live sont disponibles, 
c'était la priorité.***

# Récupération des données estimés live du jour :

Pour récupérer les données que l'on retrouve en pemier sur la
[page de ScalAir](http://www.scalair.nc/)

![Screenshot](./Screenshot.png)

# Usage

```java
StationCrawler crawler = new StationCrawler();
Station aStation = crawler.getStationsStatuses().get(Station.NOM_STATION_ANSE_VATA);
System.out.println("#########################################");
System.out.println(aStation);
System.out.println("#########################################");
```

Donne ceci :

```
#########################################
Nom : <Anse Vata>
Coleur : <GREEN>
IGA : <3>
Message : <Bon>
Typologie : <URBAINE>
#########################################
```