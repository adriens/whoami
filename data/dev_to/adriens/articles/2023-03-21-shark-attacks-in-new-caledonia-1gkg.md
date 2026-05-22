---
comments: 30
id: 1405291
is_dev_challenge: false
published_at: '2023-03-21T08:32:07Z'
reactions: 1
reading_time_minutes: 2
tags:
- opendata
- datascience
- python
- jupyter
title: 🦈 Shark Attacks in New Caledonia 📈
url: https://dev.to/adriens/shark-attacks-in-new-caledonia-1gkg
---

## 🤔 Context

After tragic shark attacks in New-Caledonia, The mayor of Nouméa has banned swimming until December 31st, 2023:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wa0r6mdk5pkj3yjk0mhu.png)](https://www.noumea.nc/sites/default/files/publications/2023-911-arrete-portant-interdiction-temporaire-toute-baignade-bande-littorale-300-metres-noumea-du.pdf)

Here is a brief about the decision:

{% embed https://la1ere.francetvinfo.fr/nouvellecaledonie/province-sud/noumea/risque-requin-noumea-a-pris-l-arrete-qui-interdira-la-baignade-jusqu-au-31-decembre-et-autorisera-les-activites-nautiques-aux-risques-et-perils-des-usagers-1376142.html %}

After all these **numerous recent dramatic events ** I wanted to know more about these attacks... but I was a bit disappointed by the lack of local and easy to use data.

So I decided to start to do something:

- 📥 **Get** the data
- 🧽 **Cleanup** and standardize (dates, locations,...)
- 💉 **Put data under steroids**(with **keys that allow the use of local datasets** from [`data.gouv.nc`](https://data.gouv.nc/pages/accueil/)) and international codes (`ISO2`,...)
- 🎀 **Help discover** the data and its possibilities

## 🗃️ Kaggle dataset

I decided to **prepare a dedicated dataset** on Kaggle with : 

- ✅ Very clean `csv` files
- ✅ A ready to use [`sqlite`](https://sqlite.org/index.html) database

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/twfeiryoi97btgf7wz25.png)

And data about : 

- 🛡️ **Sharks conservation status** (from [IUCN Red List of Threatened Species](https://www.iucnredlist.org/))
- 🌝 **Lunar phasis** in New Caledonia
- 📅 **Shark attacks** (date, day of week, season, attack type, commune, codes to local cities open data keys, province/state, activity/age/sex of the victim, injury, fatal or not, shark species involved, shark size,... )
- 🦈 **Sharks species** we have in New Caledonia

{% embed https://www.kaggle.com/datasets/adriensales/shark-attack-nouvelle-caldonie/settings %}

## 💯 Data Usability first❕

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/939fylg3mxexqblchzlo.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5qr9iggrgy4sb4gz6sr0.png)

## 📊 Then a first notebook

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cndabkmaee325dq7a00g.png)](https://www.kaggle.com/code/adriensales/shark-attacks-new-caledonia-for-dummies)

{% twitter 1636923470180417538 %}

## 📰 Related press resources

{% embed https://www.lemonde.fr/planete/article/2023/03/08/la-nouvelle-caledonie-mise-sur-l-abattage-des-requins-apres-de-graves-attaques_6164691_3244.html %}

{% embed https://la1ere.francetvinfo.fr/nouvellecaledonie/la-caledonie-est-un-hot-spot-mondial-du-risque-requin-selon-le-chercheur-francois-taglioni-1364026.html %}
