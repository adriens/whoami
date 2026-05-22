---
comments: 0
id: 784896
is_dev_challenge: false
published_at: '2021-08-08T04:18:26Z'
reactions: 2
reading_time_minutes: 3
tags:
- opendata
- rest
- opensource
- docker
title: 🏢 Open Data & Ridets en Nouvelle-Calédonie
url: https://dev.to/adriens/open-data-ridets-en-nouvelle-caledonie-52pl
---

## :birthday:Introduction:birthday:

Il y a tout juste un an, le 1er Août 2020, le [Gouvernement de Nouvelle-Calédonie](https://gouv.nc/) lançait officiellement sa [plateforme Open Data](https://data.gouv.nc/pages/accueil/) :

{% twitter 1289475231774457857 %}

Depuis, un nombre important de données statiques et dynamiques sont régulièrement poussées non seulement par le Gouvernement lui-même mais également les autres institutions Calédoniennes : [15 partenaires](https://data.gouv.nc/pages/Partenaires/) jouent le jeu.

## Réalisation précédente

L'année dernière a été développée une [application mobile](https://play.google.com/store/apps/details?id=com.github.adriens.nc.emploi) qui met en valeur les offres d'emplois, grâce au DataSet [offres-demploi](https://data.gouv.nc/explore/dataset/offres-demploi/information/?disjunctive.experience&disjunctive.typecontrat&disjunctive.communeemploi&disjunctive.niveauformation&disjunctive.employeur_type&disjunctive.employeur_nomentreprise&disjunctive.specifites_multivalue&disjunctive.zonesdeplacement_multivalue&disjunctive.permis_affichage&disjunctive.langues_affichage) et qui compte un **pool de 120 utilisateurs réguliers**.

{% youtube 8-O66XnNtsM%}

Il est toujours intéressant de fournir des services vivants qui mettent en valeur ces données, voire permettent de simplifier les démarches interinstitutionnelles ou tout simplement de favoriser la digitalisation des services.

## Faciliter l'accès à la donnée

Le succès d'une API tiennent en deux caractéristiques principales :

- La disponibilité
- La qualité des données (juste, à jour, ...)
- Le design : simplicité d'intégration, documentation

J'ai donc eu envie d'appliquer cela au dataset [entreprises-actives-au-ridet](https://data.gouv.nc/explore/dataset/entreprises-actives-au-ridet) qui a récemment rejoint la plateforme :

{% twitter 1385086684589481984%}

L'API fournie par défaut n'est pas si évidente bien que [parfaitement documentée](https://data.gouv.nc/explore/dataset/entreprises-actives-au-ridet/api/?disjunctive.libelle_formjur&disjunctive.code_ape&disjunctive.libelle_naf&disjunctive.section_naf&disjunctive.libelle_section_naf&disjunctive.libelle_commune&disjunctive.hors_nc&disjunctive.province&disjunctive.employeuse).

En tant que développeur, je suis davantage habitué à des endpoints dédiés et simples. J'ai eu envie de deux choses.

Un endpoint du type :

```
/ridet/0132720
```

Une documentation de type [Swagger](https://swagger.io/) et de proposer mon API documentée via [OpenAPI](https://www.openapis.org/).

## :rocket:Expérimentation

Je me suis donc lancé dans une expérimentation : **développer un proxy REST qui consomme l'API Open Data dans le but de la rendre plus "sexy".**

Je la livrerai en Open Source, via une image [Docker publique](https://hub.docker.com/r/rastadidi/ridetnc-api) afin de voir les retours et faire ma propre expérience sur ce jeu de données que je ne connaissais pas vraiment.

## :sparkler:A vous de jouer !:sparkler:

Quoi de mieux, pour expérimenter, que de jouer avec un scénario interactif... en live ?

:joystick:J'ai donc créé le scénario [Get Ridets with Open Data](https://www.katacoda.com/rastadidi/courses/open-data/ridet-nc).

## Code source

{% github adriens/ridetnc-api %}

## :moneybag:Un autre jeu de données très prometteur:moneybag:

En Juillet 2021, [data.gouv.nc](https://twitter.com/datagouvnc) a ouvert l'[API publique des prix à la consommation](https://data.gouv.nc/explore/dataset/prixnc/information/) affichés sur le site [prix.nc](http://prix.nc), ainsi que la [documentation Swagger](https://prix.nc/api/v1/swagger-obsprix.html) :

{% twitter 1419422023462182912 %}