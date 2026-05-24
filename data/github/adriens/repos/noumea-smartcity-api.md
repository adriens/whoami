---
name: noumea-smartcity-api
url: https://github.com/adriens/noumea-smartcity-api
description: "Hub d'APIs REST pour la ville de Nouméa "
language: Java
topics: []
stars: 0
created_at: 2019-03-21
updated_at: 2019-10-11
archived: false
has_readme: true
---

[![Build Status](https://travis-ci.org/adriens/noumea-smartcity-api.svg?branch=master)](https://travis-ci.org/adriens/noumea-smartcity-api)

# noumea-smartcity-api

Hub d'APIs REST pour la ville de Nouméa.

Déployée sur Heroku : `https://noumea-smartcity.herokuapp.com`


## Scalair Endpoints

- `/scalair` : renvoie la liste des IGA live de tous les spots de Noméa, tel
que présenté sur [la carte de leur site](http://www.scalair.nc/)
- `/scalair/logicoop` : uniquement Logicoop
- `/scalair/logicoop/message` : endpoint [dédié au shield.io](https://shields.io/endpoint)
- `/scalair/montravel`
- `/scalair/montravel/message`
- `/scalair/faubourg`
- `/scalair/faubourg/message`
- `/scalair/vata`
- `/scalair/vata/message`
- `/scalair/general` : IQA général pour Nouméa entier
- `/scalair/general/message` ou `/scalair/message`
- `/scalair/iqa` : liste des IQAs
- `/scalair/iqa/{indice}` : détail de la défintion d'un IQA