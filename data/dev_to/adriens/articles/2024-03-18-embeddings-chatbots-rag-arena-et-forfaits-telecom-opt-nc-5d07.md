---
comments: 4
id: 1782692
is_dev_challenge: false
published_at: '2024-03-18T22:47:58Z'
reactions: 2
reading_time_minutes: 8
tags:
- openai
- ai
- showdev
- tutorial
title: ⚔️ Embeddings, Chatbots RAG Arena et forfaits Telecom OPT-NC
url: https://dev.to/adriens/embeddings-chatbots-rag-arena-et-forfaits-telecom-opt-nc-5d07
---

## 🎯 LA question centrale

Le but de ce post est de **se concentrer sur les challenges clients suivants** : 

- _"Choisissez le `${produit}` qui vous ressemble"_
- _"Quelle  `${produit}` choisir ?"_
- _"Comparez et trouvez le `${produit}` adapté à vos besoins."_

Où  `${produit}` peut très facilement être remplacé par:

- Forfait
- Offre mobile
- Tout autre produit ou service

Ce sujet avait déja été abordé, ainsi que son potentiel de chatBOT:

{% embed https://youtube.com/clip/UgkxcC6mMeFRsT0w2T4sAvTcCr56hQCLdW4c?si=hYcLE4bqYileDVwH %} 

👉 Aujourd'hui, nous allons construire un prototype et jouer avec 🙌

## 🍿 Pour les impatients

{% youtube L7Mc2y7EQcs %}

## _💡 Un deuxième chatBOT ?_ 

Par le passé, j'avais créé un chatBOT connecté à notre [API de suivi des colis](https://rapidapi.com/opt-nc-opt-nc-default/api/suivi-colis/details) pour suivre le processus de livraison des colis, via une interface conversationnelle et pour qui j'avais créé un [_custom tool_](https://python.langchain.com/docs/modules/agents/tools/custom_tools):

{% embed https://dev.to/adriens/track-package-delivery-w-langchain-agent-custom-tools-18jf %}

Cette fois-ci on va venir **enrichir la collection avec un chatBOT dans un autre domaine fonctionnel - le Telecom - et avec une autre technologie cette fois.

Ne disposant pas d'API publique, mais **uniquement d'un [site web](https://www.opt.nc/particuliers/mobile/choisissez-le-forfait-qui-vous-ressemble)** - ce qui est très courant -, **on va voir comment construire un prototype fonctionnel.**

Ensuite, on regardera comment évaluer les performances des chatBOTs...

{% twitter 1766921390970581142 %}

## 💭 Pitch

Voici la question centrale qui a suscité la création de ce contenu:

> _"Quelle serait l'utilité de disposer d'un chatBOT expert dans la connaissance des forfaits telecom d'une entreprise Telecom, et qui saurait efficacement conseiller les prospects sur les forfaits les plus adaptés à leurs usages ?
Et comment en mesurer les performances ?"_

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5nkjpz73hxtow1vd3hos.png)

## 🤔 Le chatBOT : un gadget ?

Nous allons donc adresser très concrètement les points ci-dessous via une expérimentation de bout en bout, **dans le but d'illustrer les gains et objectifs stratégiques** suivants:

1. **⚡ Améliorer l'expérience client** grâce à des réponses rapides et précises.
2. **⏳ Améliorer le service client** via la gestion de demandes simultanées
3. **🤗 Personnaliser des offres** via la collecte des données sur les préférences des clients
4. **🗓️ Disponible 24/7** pour une assistance en dehors des heures de bureau
5. **🤗 Améliorer globalement l'Expérience client** : efficacité, personnalisation etdisponibilité accrues
6. **📊 Evaluer** les performances

> _"Gartner Predicts Chatbots Will Become a Primary Customer Service Channel Within Five Years"_

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oqruppq7yu2fhz8h0yry.png)
](https://www.gartner.com/en/newsroom/press-releases/2022-07-27-gartner-predicts-chatbots-will-become-a-primary-customer-service-channel-within-five-years)

## 📜 Déroulé

On va dérouler les étapes suivantes:

1. **Construire un chatBOT** très basique en mesure de connaître les forfaits de l'OPT-NC
2. **Déterminer un échantillon de questions étalon** (issues de la vraie vie) que des prospects pourraient poser lors de l'achat de nouveau forfait
3. **Evaluer notre chatBOT** vs. Cagou en mode "⚔️ Chatbot Arena"
4. **Conclure le classement** en mode "Chatbot Arena Leaderboard"


## 🧰 A propos

Pour créer notre prototype, nous allons nous appuyer sur la stack suivante:

- Les [APIs d'Open AI](https://openai.com/blog/openai-api)
- [Llama Index](https://www.llamaindex.ai/) comme framework pour interagir avec notre LLM
- Les [embeddings d'Open AI](https://platform.openai.com/docs/guides/embeddings) 

... et pousser le tout sur un [Notebook dédié](https://www.kaggle.com/code/adriensales/chatter-avec-les-forfaits-telecom-opt-nc):

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/p60jri6wic4q1vscyn3x.png)](https://www.kaggle.com/code/adriensales/chatter-avec-les-forfaits-telecom-opt-nc)


## 🏅 Classement final

Pour commencer par la fin, ci-dessous, le **🏅 Chatbot Arena Leaderboard** résultant:

|Rank|`BOT`|Score/40| Description | 🤖 Eval | 🧑 Eval |
| ---| --- |   ---   |     ---     | --- | --- |
| 1  | Prototype | **36** | [OpenAI Embedding/ WebPageReader](https://www.kaggle.com/code/adriensales/chatter-avec-les-forfaits-telecom-opt-nc)| 17 | 19 |
| 2  | Cagou | **10**     | [CAGOU L'ASSISTANT `OPT-NC`](https://www.conversationnel.fr/portfolio/chatbot-opt-nc) | 5 | 5 |

ℹ️ Chaque concurrent doit répondre aux challenges suivants (dont la qualité de la réponse sera alors évaluée):

- _💰 Le forfait "le moins cher"_
- _📶 Besoin d'un "forfait data"_
- _🔒 Forfaits "bloqués"_
- _🎒 "Je suis lycéen et..."_

Pour memo : les notes de 1/5 données par les humains ont été accompagnées des **commentaires spontanés** suivants:

- _"Je ne vois pas le rapport en fait"_
- _"Je ne vois pas le rapport avec le contexte"_

## 🔭 Remarques et opportunités

Au cours des expérimentations sont remontées les idées suivantes qui pourraient permettre d'atteindre des niveaux de qualité de réponses bien supérieurs.

En voici quelques unes:

- **Récupération et constitution d'un dataset** issu de vraies demandes clients avec les réponses optimales
-  **Enrichissement du dataset précédent** avec des données synthétiques
- **Automatisaiton** du _benhcmark Arena_
- **Diminution des coûts** via l'utilisation de modèles Open Source
- **Tuning de réponses** via l'implémentation de [Few-shot prompt templates](https://python.langchain.com/docs/modules/model_io/prompts/few_shot_examples)
- **Préparation de datasets structurés** pour diminuer les coûts de RUN du bot
- **Création d'un unique textbook `markdown`** de très haute qualité dédié aux forfaits afin de l'utiliser comme source de données pour des BOTs.

## 🔬 Détails

A ce stade l'article est terminé, mais tous les détails ont été consignés, la suite leur est dédiée.

### 💰 _Le forfait "le moins cher"_

La question:

> "Je ne téléphone presque pas : quel forfait mobile le moins cher me permet de recevoir des appels ? Donne moi le nom des forfaits répondant à mon besoin. Explique pas à pas."

Réponses de BOTs:

| `WebPageLoader` & OpenAI | Cagou OPT |
|              ---         |    ---    |
| Le forfait mobile le moins cher qui vous permet de recevoir des appels est le "Forfait Bloqué 1000" à 1 060 F TTC par mois. Ce forfait vous offre la possibilité de recevoir des appels à un prix avantageux. Pour répondre à votre besoin de ne pas téléphoner souvent, ce forfait est le plus adapté parmi les options disponibles. | Sur quel appareil souhaitez-vous suivre votre conso ? |


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xst7eio6ws823s4p3mor.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/slq7f9i3yfbeq8xuop0w.png)


### 📶 _Besoin d'un "forfait data"_

La question:

> "J'ai besoin d'un forfait data : quelles sont les options disponibles ? Explique pas à pas."

Réponses de BOTs:

| `WebPageLoader` & OpenAI | Cagou OPT |
|              ---         |    ---    |
| Pour obtenir un forfait data, vous avez plusieurs options en fonction de votre situation. Si vous êtes déjà client Mobilis, vous pouvez faire votre demande en ligne, envoyer un mail à l'adresse fournie avec les informations nécessaires, vous rendre dans une boutique partenaire Mobilis ou prendre rendez-vous avec un conseiller télécoms en ligne ou en appelant le 1000. Si vous n'êtes pas encore client Mobilis, vous pouvez prendre rendez-vous avec un conseiller télécoms en ligne ou en appelant le 1000, ou vous rendre dans une boutique partenaire Mobilis. Assurez-vous d'avoir une pièce d'identité, un justificatif de domicile de moins de 3 mois et un RIB si vous optez pour le prélèvement automatique. | Pour quel appareil souhaitez-vous consulter nos offres ? |


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1ukeyrra3n6keqef9v67.png)

### 🔒 _Forfaits "bloqués"_

La question:

> "Je n'ai pas les moyens de payer un forfait mobile chaque mois : donne moi le nom des forfaits répondant à mon besoin ? Explique."

Réponses de BOTs:

| `WebPageLoader` & OpenAI | Cagou OPT |
|              ---         |    ---    |
| Les forfaits qui pourraient répondre à votre besoin sont les forfaits bloqués. Ces forfaits nécessitent un paiement mensuel fixe et offrent des limites claires en termes de coûts. Vous pouvez choisir parmi les forfaits bloqués 1000, 2000, 3000, et 5000 F qui offrent des services à des prix différents tout en vous permettant de contrôler vos dépenses mensuelles de manière plus précise. | Sur quel appareil souhaitez-vous suivre votre conso ? |


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wh74vmof7rjkzds1phiu.png)

### 📝 La _"table des forfaits"_

> "Liste moi tous les forfaits dans un seul et même tableau."

Réponses de BOTs:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jmw9ut4q3ys94oqv6an8.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4tfqdykp3voa7fav153q.png)



### 🎒 _"Je suis lycéen et..."_

Question:

> "Je viens d'avoir 18 ans, je suis au lycée et j'ai juste besoin d'un forfait mobile pour que mes parents puissent m'appeler et aussi aller un peu sur Instagram : quel forfait me sont adaptés ? Explique."

| `WebPageLoader` & OpenAI | Cagou OPT |
|              ---         |    ---    |
| Le forfait qui vous conviendrait le mieux serait le Forfait Bloqué 1000. Il offre un bon équilibre entre les besoins de communication avec 1 060 F TTC par mois. Ce forfait vous permettra de recevoir des appels de vos parents et d'utiliser un peu d'Internet pour aller sur Instagram.| Sur quel appareil souhaitez-vous suivre votre conso ? | 


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o96ie0rtseqv2155tqmq.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/89sc9jyc3tz8d92bncdm.png)

## Les "⚔️ Chatbot Arena"

Les ⚔️ Chatbot Arena (ex celle de https://chat.lmsys.org/) permettent de comparer des BOTs ou des LLMs sur divers challenges.

On pose une même question et en parallèle à deux chatbOTs et on évalue leur réponses respectives.

Deux protocoles sont usités : 

- 100% automatisé : c'est une IA qui évalue la pertinence des réponse des autres chatBOTs
- Human in the loop : c'est un être humain qui évalue

... et nous allons faire les deux 🤩

## 📜 Méthode

Que l'on parle à un humain ou à une machine, **le protocole (ie. scénario) sera le même afin de disposer de conditions expérimentales identiques pour les évaluateurs** (humain ou machine):

1. **Préparer un `PROMPT SYSTEM` **: _"Je vais te donner une question et tu devras évaluer la qualité de la réponse sur une note allant de 1 à 5, 5 étant la meilleure note."_
2. **Enoncer le challenge** client
3. **Donner la réponse de notre chatBot** à base d'embeddings OpenAI (sans dire que c'est lui) et demander le score
4. **Donner la réponse de [CagouBOT](https://www.conversationnel.fr/portfolio/chatbot-opt-nc) **(sans dire que c'est lui) et demander le score


## ⚖️ Evaluation par l' `IA`

Nous allons utiliser un modèle Open Source et accessible gratuitement sur [HuggingChat](https://huggingface.co/chat/) :  [`Nous Hermes 2 Mixtral 8x7B DPO`](https://huggingface.co/NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO)**, particulièrement bon pour suivre des directives.**


|  Question  | OpenAI score      |Cagou score|
|              ---             | --- | --- |
| 💰 Le forfait "le moins cher"| 4/5 | 2/5 |
| 📶 Besoin d'un "forfait data"| 4/5 | 1/5 |
| 🔒 Forfaits "bloqués"        | 5/5 | 1/5 |
| 🎒 "Je suis lycéen et..."    | 4/5 | 1/5 |


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6ei80zatteuxy19l20s3.png)



## ⚖️ Evaluation humaine

Pour cette phase de test, j'ai interviewé deux collaborateurs, strictement déroulé le même protocole que pour l'IA et aie noté les notes, les réponses fournies pour évaluation sont fournies en aveugle : **la personne humaine ne sait pas qui est l'auteur de la réponse qu'il va évaluer.**

**ℹ️ La synthèse des deux scores est effectué en donnant la note maximale.**

|  Question  | OpenAI score      |Cagou score|
|              ---             | --- | --- |
| 💰 Le forfait "le moins cher"| 5/5 | 2/5 |
| 📶 Besoin d'un "forfait data"| 5/5 | 1/5 |
| 🔒 Forfaits "bloqués"        | 5/5 | 1/5 |
| 🎒 "Je suis lycéen et..."    | 4/5 | 1/5 |


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/clesw6wwgmfztahacxht.png)



### 🔎 Détail des évaluations

#### 💰 Le forfait "le moins cher"

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kivtm90bryt0ko1w9ajv.png)

#### 📶 Besoin d'un "forfait data"


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ciiw82vz98c7a0uq8vcr.png)

#### 🔒 Forfaits "bloqués"  


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hu6pdqnij4479ymcj97q.png)

#### 🎒 "Je suis lycéen et..." 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w8m6ihf459j1m67arnay.png)


## 📖 Résumé des Q&As


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8qx78nl7ow0ukfn56671.png)](https://docs.google.com/spreadsheets/d/1PQWjWfKO8kxTETHFlHZA1jV_YdRc10Z17BhPPXOs-6c/edit?usp=sharing)