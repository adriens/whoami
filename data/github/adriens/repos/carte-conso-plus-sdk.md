---
name: carte-conso-plus-sdk
url: https://github.com/adriens/carte-conso-plus-sdk
description: "SDK java pour interagir avec le site (http://www.consoplus.nc/) de la Carte Conso + (Nouvelle-Calédonie)"
language: Java
topics: []
stars: 0
created_at: 2018-03-17
updated_at: 2020-08-17
archived: false
has_readme: true
---

[![Build Status](https://travis-ci.org/adriens/carte-conso-plus-sdk.svg?branch=master)](https://travis-ci.org/adriens/carte-conso-plus-sdk)
[![](https://jitpack.io/v/adriens/carte-conso-plus-sdk.svg)](https://jitpack.io/#adriens/carte-conso-plus-sdk)


# carte-conso-plus-sdk
SDK java pour interagir avec le site (http://www.consoplus.nc/) de la Carte Conso + (Nouvelle-Calédonie).

# Demo

![Dummy demo screenshot](DEMO.png "Dummy demo screenshot")

# Howto

Usage :

```java
public static void main(String[] args) {
        try {
            String login = "YOUR_LOGIN";
            String passwd = "YOUR_PASSWORD";
            CarteConsoCrawler wrap = new CarteConsoCrawler(login, passwd);
            logger.info(wrap.toString());
            logger.info("Bye.");
            System.exit(0);
        } catch (IOException ex) {
            ex.printStackTrace();
            System.exit(1);
        }
    }
```