---
comments: 2
id: 4864939
is_dev_challenge: false
published_at: '2026-10-18T20:54:09Z'
reactions: 0
reading_time_minutes: 4
tags:
- hacktoberfest
- hackavp
- ai
- datascience
title: 🔬 J'ai mappé les offres d'emploi public de l'OPT-NC avec le référentiel ESCO
  à l'aide d'embeddings et de Qwen3-32B-AWQ
url: https://dev.to/adriens/jai-mappe-les-offres-demploi-public-de-lopt-nc-avec-le-referentiel-esco-a-laide-dembeddings-5765
---

## ❔ Contexte

Avant de me lancer de l'organisation du HackAVP : 

{% embed https://dev.to/adriens/hackavp-premier-hackathon-dedie-a-lemploi-dans-la-fonction-publique-en-ncl-3oj0 %}

J'avais à cœur de préparer un _"trésor de données"_, qui pourrait patiemment être constitué au fil du temps.

> Mon but était avant tout d'assouvir ma curiosité

sur ces données : les postes recherchés, les corpus, les compétences, les métiers, les exigences.

Et en faisant cette veille sur ces données et les référentiels liés, j'ai fini par découvrir le référentiel Européen [ESCO](https://esco.ec.europa.eu/fr) :

> La classification ESCO recense et catégorise les aptitudes, les compétences, les certifications et les professions pertinentes pour le marché du travail, lenseignement et la formation au sein de lUE. Elle présente systématiquement les liens entre les différents concepts.

## 🍿 Pour les impatients

{% youtube cKV_tJ6qdSo %}

## 🤩 Ce que j'adore faire

S'il y a bien une activité que j'adore mener car très satisfaisante pour moi, c'est de : 

> relier des corpus de texte bruts à des référentiels stricts élaborés par des experts afin d'apporter cette perspective experte sur nos propres données : celles des offres d'emploi (Avis de Vacances de Postes)

... mais n'étant pas expert RH et les données étant volumineuses (surtout côté ESCO), utiliser de l'automatisation pour faire cela à l'échelle... et _voir ce que ça donne._

Mais avant tout... c'est vraiment une histoire de curiosité : 

{% twitter 2111329792230641813 %}

## 👨‍🔬 L'expérimentation

A l'aide des données ESCO que j'avais préparées en amont via le [dataset Kaggle ESCO v1.2.1](https://www.kaggle.com/datasets/adriensales/esco-v1-2-1), le processus consiste en 3 étapes : 

1. **🔗 Rappel — des embeddings** ([multilingual-e5-large](https://www.kaggle.com/refs/hf-model/intfloat/multilingual-e5-large)) proposer pour chaque AVP une douzaine de professions ESCO candidates, et pour chaque exigence (skills, competencyRequired) une douzaine de compétences candidates
2. **🤖 Validation** — un LLM ([Qwen3-32B-AWQ](https://www.kaggle.com/refs/hf-model/Qwen/Qwen3-32B-AWQ) via vLLM, mode raisonnement) choisit parmi ces candidates celles qui correspondent réellement, ou aucune. (Son raisonnement est conservé pour expliquer chaque lien à posteriori.)
3. **📊 Analyses** : On analyse directement dans le notebook ce qui en ressort


## 💡 Les découvertes

### La carte


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/uqqwpavup3ygii77kg5x.png)


### Mapper des titres de postes avec des professions ESCO


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ap22mikglmi2rwhc5brk.png)

### Mapper des phrases avec des compétences ESCO


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ztzuslu9le38xaepenhp.png)


### Les liens impossibles à trouver


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/rp2iybgdabb6kmq630n5.png)

### La constellation des compétences attendues


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/cxbix9wxozzlw02lrcyf.png)

### Les 25 compétences ESCO les plus demandées

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/1bjs70eddo9qduq364ed.png)

### Le profil de compétences ESCO par direction


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/tnv22b0couw0vg89wkkp.png)

### Thématiques ESCO les plus représentées


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/fzsvawlr1y97qcfs26nm.png)

### Les métiers recrutés selon la classification internationale ISCO


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/li0h2s8024on5sj6o71e.png)


### Liens direction et groupes ISCO


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/z9awq797fps6rkddyy8y.png)


### Ressemblances entre postes


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/rmdtd8bg9b3xn6t4xo3d.png)

### Le spécifique : ce que les AVPs ajoutent ou oublient

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/y5kkmtuoxa3vi5c80fyp.png)

### Exigences sans équivalent ESCO

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/ilkf1shsy9dsf9vbipen.png)

### Explication du raisonnement

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/weaeuihbfmytfoknqnk9.png)



## 🔭 Perspectives d'amélioration data

- Compléter avec les données permettant d'améliorer le matchin en labélisant certaines données
- Prototyper un agent pour aider à rédiger des AVPs qui matchent mieux le référentiel ESCO

## 📑 Ressources

### 📚 Référentiels

- [ESCO](https://esco.ec.europa.eu/fr)
- [ISCO](https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/international-standard-classification-occupations-isco)
- [International Standard Classifi cation of Occupations](https://webapps.ilo.org/ilostat-files/ISCO/newdocs-08-2021/ISCO-08/ISCO-08%20EN%20Vol%201.pdf)
- [ESCO v1.2.1](https://www.kaggle.com/datasets/adriensales/esco-v1-2-1/data) sur Kaggle

### 💻 Notebooks et modèles

- [Le Notebook final](https://www.kaggle.com/code/adriensales/avp-opt-nc-esco-qwen/notebook)
- [Qwen/Qwen3-32B-AWQ](https://www.kaggle.com/refs/hf-model/Qwen/Qwen3-32B-AWQ)
- [intfloat/multilingual-e5-large](https://www.kaggle.com/refs/hf-model/intfloat/multilingual-e5-large)

