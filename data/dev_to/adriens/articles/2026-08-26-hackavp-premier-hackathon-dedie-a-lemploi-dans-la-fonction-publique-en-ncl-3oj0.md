---
comments: 7
id: 4400434
is_dev_challenge: false
published_at: '2026-08-26T22:49:06Z'
reactions: 1
reading_time_minutes: 15
tags:
- hackathon
- career
- opensource
- ai
title: '🏆 #HackAVP, premier hackathon dédié à l''emploi dans la fonction publique
  en NCL'
url: https://dev.to/adriens/hackavp-premier-hackathon-dedie-a-lemploi-dans-la-fonction-publique-en-ncl-3oj0
---

### ⏳ Challenge Status: Not yet Live (article en Draft)

👉 Pour participer : venez le mercredi 09 septembre 17h00, à la Station N

{% twitter 2092744648494358943 %}


Aucune inscription préalable, aucune formalité. Les équipes se constituent sur place et tout le fonctionnement du hackathon est présenté ce soir-là — c'est la seule date de présence requise sur les sept semaines.
Vous n'avez pas d'équipe ? Venez quand même : c'est précisément à ça que sert la soirée.

## ❔ À propos du hackathon, du recrutement et des talents calédoniens

Une offre d'emploi publiée n'est pas une offre d'emploi trouvée.

Entre les deux, il y a deux sites web : 

- [Site institutionnel de l'OPT-NC](https://office.opt.nc/fr/emploi-et-carriere/postuler-lopt-nc/avp)
- [Site institutionnel de la DRHFPNC](https://drhfpnc.gouv.nc/avis-vacances-postes-AVP)

Pas forcément optimum pour une recherche confortable depuis un mobile, une tablette, sans forcément de moteur de recherche adapté (recherche par métier, compétences ou technologies), un vocabulaire administratif qui peut décourager, ou une fiche de poste qui ne dit pas à qui elle s'adresse, ou encore des problèmes d'accessibilité.

Ce sont des problèmes d'accès à l'information — et ils se traitent par la donnée et par le design.

L'**OPT-NC** en tant qu'EPIC, a depuis de nombreuses années l'intégralité de ses **avis de vacance de poste** (AVP), publiés sur [`data.gouv.nc/avis-de-vacances-de-poste-avp-drhfpnc`](https://data.gouv.nc/explore/dataset/avis-de-vacances-de-poste-avp-drhfpnc/).

Ce qui est nouveau, c'est que désormais, l'ouverture ne s'est pas arrêtée à la publication sur le [site de la DRHFPNC](https://drhfpnc.gouv.nc/avis-vacances-postes-AVP) : chaque annonce est désormais:

- Normalisée au format [`schema.org/JobPosting`](https://schema.org/JobPosting),
- Exposée par une [API](https://apigee-optnc-prd-api.apigee.io/docs/avps/1/overview),
- Publiée dans un dataset versionné sur [Hugging Face](https://huggingface.co/datasets/opt-nc/odata-avps),
- Et accessible par un [serveur MCP](https://apigee-optnc-prd-api.apigee.io/docs/mcp-emploi/1/overview) directement branchable sur un agent conversationnel.

Une infrastructure de données publiques de ce niveau de finition reste rare à l'échelle du territoire.

Elle pose une question simple :

> **Maintenant que la donnée est réellement exploitable, qui va s'en emparer — et pour en faire quoi ?... et quels sont les gains attendus par l'organisation qui a fait cet effort d'ouverture et d'interopérabilité ?**

Le Hackathon AVPs est la réponse organisée à cette question. Pendant sept semaines, des équipes calédoniennes construisent des services qui rendent le recrutement de l'OPT-NC plus lisible et plus accessible — ou qui valorisent cette donnée d'une autre manière à laquelle l'Office lui-même n'aurait pas songé ou tout simplement pas eu le temps de traiter (on parle alors d'Open Innovation).

12 familles de métiers sont représentées dans le référentiel (voir [`odata-referentiel-metiers/familles-metiers`](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/)):

- [VENTE & RELATION CLIENT](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/vente_relation_client/)
- [MARKETING ET COMMUNICATION](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/marketing_et_communication/)
- [SERVICES BANCAIRES](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/services_bancaires/)
- [ACTIVITES POSTALES](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/activites_postales/)
- [TELECOMMUNICATIONS](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/telecommunications/)
- [ADMINISTRATION](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/administration/)
- [RESSOURCES HUMAINES](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/ressources_humaines/)
- [FINANCES & BUDGET](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/finances_budget/)
- [PATRIMOINE BÂTI](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/patrimoine_bati/)
- [LOGISTIQUE](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/logistique/)
- [SYSTÈMES D'INFORMATION](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/systemes_d_information/)
- [PILOTAGE](https://opt-nc.github.io/odata-referentiel-metiers/familles-metiers/pilotage/)

pour un employeur de **~ 1000 personnes**.

**Co-organisé par** l'OPT-NC · la Station N (gouvernement de la Nouvelle-Calédonie) · la commission Data & IA du cluster OPEN NC.

**Participation gratuite et ouverte à tous** : développeurs, étudiants, designers, professionnels RH et de la donnée.
Une seule date de présence est requise — la soirée de lancement.

> 💡 **La mixité des équipes est activement encouragée.** Sur un sujet d'accessibilité du recrutement, une équipe exclusivement technique produit une solution élégante à un problème mal posé.

## 🎁 Ce que vous y gagnez

Au-delà des dotations :

- **📢 Une trace publique, durable et référencée.** Le rendu impose un article sur dev.to. Des développeurs calédoniens qui documentent leur travail sur une plateforme internationale, c'est un actif — pour vous, pour votre employeur, et pour l'image du territoire.
- **🎤 Une scène.** Le 4 novembre, les finalistes démontrent en live à TECH'N CO, devant l'écosystème numérique calédonien réuni.
- **🛠️ Une montée en compétence sur du réel.** `schema.org`, serveur MCP, embeddings vectoriels, API management : vous travaillez sur une infrastructure de données publique en production, pas sur un jeu de données jouet.
- **🤝 Apprendre en innovant à plusieurs.** Sept semaines à construire en équipe, sur un sujet neuf, avec des profils qui ne sont pas les vôtres : c'est la façon la plus rapide d'apprendre, et la plus difficile à organiser seul chez soi.
- **🌐 Un réseau.** Le kickoff, les échanges pendant les sept semaines, les mentors, le jury, la scène du 4 novembre : vous repartez en connaissant l'écosystème numérique calédonien — et en étant connu de lui.
- **👀 De la visibilité auprès d'un employeur de ~1000 personnes.** Sept familles de métiers, des recrutements permanents. Passer sept semaines dans la donnée de l'OPT-NC, c'est aussi se faire connaître de ses équipes.

> ☝️ Pour lever toute ambiguïté : **participer ne donne aucun avantage dans un processus de recrutement.** Les AVP restent ouverts à tous, dans les mêmes conditions.... mais se faire connaître,... ça compte.

## 🗓️ Calendrier

| Date | Étape | Lieu |
|---|---|---|
| **Mercredi 09 septembre, 17h00** | 🚀 Lancement — présentation de la donnée, énoncé du défi, constitution des équipes | Station N, Nouméa |
| **Mercredi 16 septembre** | 🔧 ON BOARDING — | Station N, Nouméa |
| **09 septembre → 21 octobre** | 💻 Cinq semaines de travail en autonomie, avec accompagnement à la demande | À distance |
| **Mercredi 21 octobre, 23h59** | 📦 Jour du rendu — article dev.to publié + vidéo de démonstration via formulaire | En ligne |
| **Jeudi 22 octobre** | 🧑‍⚖️ Délibération du jury — **les finalistes sont connus** | — |
| **Mercredi 4 novembre** | 🏆 Jour J — remise des prix et démonstrations live | **TECH'N CO**, salon du numérique et de la tech |

Le 4 novembre, les projets sont présentés en démo live à **TECH'N CO** (French Tech NC · OPEN NC), devant l'écosystème numérique calédonien réuni.

## 🎯 Le `PROMPT`

> ### Une Calédonienne ou un calédonien cherche à rejoindre l'OPT-NC.
>
> Elle/il a un parcours, des compétences, une envie, un projet professionnel. En face, des postes ouverts, décrits dans un vocabulaire administratif qui n'est pas le sien, sur une plateforme qui ne comprend pas la question qu'elle pose — quand elle pense à la poser.
>
> **Construisez ce qui manque entre les deux.**

### Les quatre fonctions à couvrir

Quatre fonctions. Elles sont **obligatoires** — c'est ce qui rend les projets comparables entre eux, et c'est exactement ce que note le bloc **Valeur RH** de la grille.

Ce sont bien des **fonctions à couvrir**, pas un scénario d'écrans à dérouler dans l'ordre. Qui les déclenche, à quel moment, et dans quel sens circule l'information : c'est à vous de le décider.

| | Fonction | Ce que ça veut dire |
|:---:|---|---|
| **①** | **Un profil entre dans le système** | Votre solution se constitue une représentation du candidat : compétences, expérience, contraintes, aspirations. **Par quel moyen ne regarde que vous** — un CV déposé (PDF, [JSON Resume](https://jsonresume.org/), export LinkedIn), un formulaire, un agent conversationnel qui pose les questions au clavier ou **à la voix**, un échange sur une messagerie, quelques phrases dictées. Le candidat n'a pas forcément de CV sous la main : votre solution peut très bien être ce qui l'aide à formuler son profil. Un profil le temps d'une session, ou une base de profils conservée et surveillée dans la durée : les deux comptent. |
| **②** | **Le matching** | Vous confrontez profil(s) et **AVP réellement ouverts** à l'OPT-NC, et vous en tirez des correspondances. Le sens est libre : d'un profil vers les postes ouverts, ou d'un AVP fraîchement publié vers un vivier de profils. Le score, lui, doit être **explicable** : on comprend *pourquoi* ce poste et ce candidat se rencontrent — et pourquoi tel autre rapprochement a été écarté. |
| **③** | **Les assets de candidature** | Pour un AVP donné, vous produisez quatre pièces. **Deux partent chez l'employeur** : une **lettre de candidature** et un **CV recentré sur ce poste**. **Deux restent au candidat** : une **restitution du matching** — où il est fort, où il est en écart face aux attendus de l'AVP, ce qu'il peut faire de cet écart — et un **document de préparation à l'entretien**, qui s'appuie dessus. C'est là que la candidature cesse d'être une intention et devient un dossier. |
| **④** | **La candidature part** | La candidature doit **sortir de votre solution** sous une forme réellement transmissible à un employeur — des fichiers qu'on télécharge, un mail qui s'envoie, un dossier qui s'archive. En face, un chargé de recrutement et un responsable opérationnel l'ouvrent : **ils reçoivent un CV et une lettre, rien d'autre**, et ignorent tout de la façon dont ces documents ont été produits. Ce qui se joue là est simple : ces deux pièces déclenchent, ou non, une convocation en entretien. |

> 🧑‍⚖️ **Comment la fonction ④ est évaluée.** Pas besoin d'un accès à l'OPT : **le jury se met en position d'employeur en phase de recrutement** et dépouille les candidatures que votre solution produit — dans les conditions réelles, c'est-à-dire un CV et une lettre, sans savoir d'où ils sortent. Ce qu'il regarde : est-ce que ce dossier **se lit vite**, est-ce qu'il **répond au poste** plutôt que de réciter le profil, est-ce qu'il **donne envie de recevoir cette personne** ? Un pavé générique, poli mais interchangeable, part en bas de la pile. Le dépouillement de candidatures est une réalité que connaissent toutes les entreprises et toutes les organisations publiques — concevez contre celle-là.

> 🎦 **Le recruteur ne sait pas comment les documents ont été produits. Le jury, lui, doit le voir.** Votre **vidéo de démonstration** montre la chaîne complète — du profil qui entre jusqu'aux documents qui sortent — **produite par votre solution, sous nos yeux**. C'est ce qui distingue un générateur qui fonctionne d'un beau PDF écrit à la main la veille du rendu. Une pièce montrée dans la vidéo sans qu'on voie votre solution la produire n'est pas comptabilisée.

### Ce qui est libre : tout le reste

Les quatre fonctions sont imposées, **la manière ne l'est pas du tout** :

- **L'interface** — web, mobile, terminal, extension navigateur, agent conversationnel, assistant vocal, borne physique, papier imprimé. Ce que vous voulez.
- **La technologie** — c'est le rôle de votre track (voir plus bas).
- **Le canal** — et si la candidature se préparait par SMS ? En langue vernaculaire ? Depuis une tribu, sans connexion stable ?
- **Le déclencheur** — rien n'oblige le candidat à venir poser sa question. Un service qui tourne en tâche de fond, qui connaît son profil et qui l'alerte dès qu'un AVP correspond à ses compétences ou à ses aspirations, est parfaitement dans le sujet — il supprime l'étape où il faut penser à chercher.
- **L'échelle** — un candidat à la fois, ou une base de profils : plateforme d'emploi, cabinet de recrutement, chasseur de tête qui reçoit chaque nouvel AVP et le rapproche de son vivier. Le rapprochement candidat ↔ poste est le même, seul le point d'entrée change.
- **Le public** — un jeune sorti du BTS, un salarié en reconversion, quelqu'un qui n'a jamais rédigé de lettre de motivation, un candidat hors territoire. Choisissez à qui vous parlez, et assumez-le.

> ☝️ Déclencheur et échelle changent le point d'entrée, pas le périmètre : **les quatre fonctions restent dues**. L'alerte ou le rapprochement couvre ① et ②, mais la chaîne va jusqu'aux documents produits et à la candidature transmise — un service de veille qui s'arrête à la notification ne concourt pas.

### Ce qu'on ne vous demande pas

- ❌ **De remplacer le recruteur.** L'objectif est de lui présenter des candidatures qui se traitent vite et se décident bien, pas de décider à sa place.
- ❌ **De couvrir tous les publics.** Une solution excellente pour un public précis vaut mieux qu'une solution tiède pour tout le monde.
- ❌ **Un produit fini.** Sept semaines, en autonomie, souvent le soir. On note une démonstration convaincante, pas un service en production.

> 💡 **Le vrai sujet, c'est l'accès.** Une offre publiée n'est pas une offre trouvée. Tout ce qui réduit la distance entre un Calédonien et un poste ouvert à l'OPT est dans le périmètre.

### ⚠️ Une règle : vraies données ou fakes ?

La fonction ① vous demande de récupérer un profil — parfois plusieurs, si vous constituez un vivier comme par exemple vos camarades de promotion ou amis en métropole.

**Travaillez sur des profils fictifs, ou sur le vôtre.** N'utilisez pas le CV d'un tiers — **ou alors son accord explicite**.

Un CV est un concentré de données personnelles : identité, adresse, parcours, parfois santé ou situation familiale. Ces données vont transiter par vos prompts, vos logs, vos services tiers et votre vidéo de démonstration, qui sera publique. Des profils fictifs vous évitent ça — et vous permettent de tester des cas limites qu'un CV réel ne vous donnera jamais.

Les **AVPs**, eux, sont des données publiques : servez-vous sans retenue, mais ne candidatez pas pour de vrai (sauf si voulez vraiment avoir cet emploi 😅)

## 🛣️ Les « tracks »

Une **track**, c'est le cadre technique dans lequel vous choisissez de concourir. Elle ne change ni le sujet, ni les livrables : elle change les **contraintes d'architecture** que vous acceptez ou vous imposez — et donc la manière dont votre chaîne de traitement est évaluée.

> ☝️ **Déclarer une track est obligatoire.** Chaque équipe en choisit **une seule**, au plus tard au moment du rendu.
Elle pèse 20 points sur 100 dans la grille d'évaluation.

### 🤯 Track « SaaS no limit »

Aucune limite, de quelque nature que ce soit. Tous les services SaaS, toutes les plateformes, où qu'elles soient, quelles qu'elles soient. Agents, voix, avatars, robots, modèles propriétaires, orchestrateurs managés : si ça sert votre idée, prenez-le.

Ce qu'on regarde ici : **la qualité de la chaîne que vous assemblez** — choix et orchestration des services (embeddings, LLM, agents, vector store), qualité de l'architecture, et reproductibilité du déploiement (IaC).

### 🛡️ Track `onPrem` souverain — « ma data à moi, chez moi, sur mon caillou »

La règle est simple : **toute la partie valorisation et orchestration de votre innovation doit résider sur un matériel physique opéré en Nouvelle-Calédonie.**

Ce matériel peut être :

- **Chez vous** : laptop, Jetson, [NVIDIA DGX Spark](https://www.nvidia.com/fr-fr/products/workstations/dgx-spark/), Mac Studio, mini-PC…
- **Dans un datacenter situé en Nouvelle-Calédonie**

Le matériel peut être **loué ou prêté**, mais il **DOIT IMPÉRATIVEMENT ÊTRE OPÉRÉ EN NOUVELLE-CALÉDONIE**.

> **⚠️ Exception explicite sur les sources de données.**
> Les référentiels officiels mis à votre disposition — API AVP, serveur MCP, dataset Hugging Face, `data.gouv.nc` — sont **consommables où qu'ils soient hébergés**. C'est la matière première, elle ne compte pas dans la contrainte de souveraineté.
> En revanche, **tout ce que vous construisez par-dessus tourne en Nouvelle-Calédonie** : embeddings, modèles de langage, vector store, orchestration, back-end, front-end.

Ce qu'on regarde ici : **votre capacité à produire un résultat comparable sous contrainte locale** — chaîne de matching exécutée sur votre matériel, frameworks Open Source, cohérence des licences de la stack, facilité d'installation.

## 🧑‍⚖️ Grille d'évaluation

Le score final est sur **100 points**, répartis en trois strates:

- Les deux premières sont communes à tout le monde
- La troisième dépend de votre track.

```plaintext
① SOCLE COMMUN      ████████████  30   →  tous les projets
② TECHNICITÉ        ██████████    25   →  tous les projets
② VALEUR RH         ██████████    25   →  tous les projets
③ TRACK             ████████      20   →  SaaS  OU  onPrem
                              ────
                              /100
```

*Technicité et Valeur RH portent le même numéro ② : ce n'est pas une coquille, elles forment une seule et même strate — les deux sont évaluées sur tous les projets, quelle que soit la track.*

### ① Socle commun — 30 points

Évalué sur tous les projets, quelle que soit la track.

| Critère | Ce que le jury regarde |
| ------- | ---------------------- |
| 🎨 **Créativité & esthétique    `/4`** | Originalité de l'idée, qualité visuelle du rendu |
| 🖱️ **UX & utilisabilité `/5`** | Le produit se comprend et s'utilise sans mode d'emploi |
| ♿ **Accessibilité  `/4`** | Le produit reste utilisable par tous — c'est le sujet même du hackathon |
| 💻 **Adéquation moyens/résultats `/5`** | Rapport entre moyens mis en oeuvre et résultat (effet bazouka pour une mouche) |
| 🌐 **Standards & Open Data `/6`** | Usage et maîtrise de référentiels publics et de schémas normés — en particulier [`schema.org`](https://schema.org/) |
| 📖 **Storytelling `/4`** | Qualité de l'article dev.to et de la vidéo : on comprend le problème, la solution et la démarche |
| 🔁 **Réutilisabilité & essaimage `/4`** | Facilité à recycler/déployer cette solution pour d'autres organisations de la fonction publique |



### ② Technicité — 25 points

- Pertinence de l'utilisation des ressources disponibles (API, MCP, dataset, référentiels)   /8
- Intégrabilité aux plateformes d'emploi et aux ATS   /8
- Maintenabilité de la solution   /5
- L’usage de l'IoT, de la voix, de la vidéo ou de tout autre média permettant une interaction inédite rapporte des points. *   /4
- *Ne pas en faire n'en coûte aucun : une excellente application web reste à égalité. Inutile, donc, de coller un capteur pour cocher une case — seul un usage réellement pertinent est valorisé.

### ② Valeur RH — 25 points

- Qualité du matching candidat ↔ AVP : pertinence, explicabilité du score, absence de faux positifs    /5
- Qualité de la lettre de candidature générée, du CV customisé et qualité du document de préparation à l'entretien     /5
- Qualité de la restitution du matching au candidat : forces, écarts face aux attendus du poste, lucidité de l'analyse     /5
- Facilité de création des assets de candidature, côté candidat    /5
- Effet sur la décision de convoquer, côté employeur     /5

### ③ Track — 20 points

Le **résultat** du matching est noté ci-dessus, en Valeur RH, identiquement pour tout le monde — c'est ce qui rend les projets comparables entre eux. Ici, on note le **moyen** : la chaîne d'ingénierie qui produit ce résultat, sous les contraintes de votre track.

| 🤯 SaaS no limit | 🛡️ onPrem souverain |
| -----------------| --------------------|
| Qualité de la chaîne de matching : choix et orchestration des services (embeddings, LLM, agents, vector store) /4 | Qualité de la chaîne de matching **sous contrainte locale** : modèles et embeddings exécutés sur votre matériel /4 |
| Qualité technique de l'architecture /2| Frameworks Open Source retenus /2 |
| Déployabilité : IaC, reproductibilité du déploiement /2 | Cohérence des licences de la stack /2 |
| Pertinence des intégrations (agents, voix, avatars, robots…) /2 | Accessibilité de la plateforme hardware, facilité d'installation  /2|

## ✅ Comment soumettre

Au plus tard le **mercredi 21 octobre à 23h59 ** :

- **📝 Article DEV.to public publié** — **obligatoire**, citant cet article à l'aide d'un `embed`
- **🎦 Vidéo de démonstration livrée** — format `mp4` ou `mkv`, durée **3 à 5 minutes**, montrant la **génération en direct** des documents de candidature par votre solution, via lien soumis dans le formulaire en ligne dédié
- **🛣️ Track déclarée** — SaaS no limit *ou* onPrem souverain
- **🔗 Lien du projet** (dépôt, démo en ligne, ou les deux)


Les vidéos pourront (si vous le souhaitez) être publiées sur une **playlist dédiée** de a chaîne [`@Station-N`](https://www.youtube.com/@Station-N) YT de la Station N.

### 🎨 Comment vous codez ne regarde que vous

Aucune contrainte sur la méthode de production :

- IA générative,
- Vibecoding,
- No-code,
- Low-code,
- Agents de développement,
- Intégrations SaaS assemblées à la main
- Plateformes SaaS prêtes à l'emploi
- ...

**Ce qui est noté, c'est le résultat** — pas la façon dont il a été écrit. 

## 🤓 Prix spéciaux

Ce hackathon se veut le plus inclusif possible, y compris envers les personnes non techniques, les juniors en développement, les étudiants, les professionnels du recrutement ou du marketing,...

Le jury se réserve donc le privilège de décerner une "Mention spéciale Station N", en plus du classement par track.

## 📑 Ressources

Tout est construit, délivré _as a Service_ par les équipes de l'OPT-NC.
La donnée est propre et son accès documenté.
Les données sont organisées en deux grands axes, qui fonctionnent de concert : 

- **Les métiers** : le référentiel de fondation, statique et pilier des compéténces
- **Les AVPs** : les offres d'emploi qui émanent directement des besoins du terrain et s'appuient sur les métiers et compétences

### 🗞️ Les AVPs

- 🔌 [`avps-api` — API des avis de vacance de poste](https://apigee-optnc-prd-api.apigee.io/docs/avps/1/overview)
- 🤖 [Serveur MCP AVPs OPT](https://apigee-optnc-prd-api.apigee.io/docs/mcp-emploi/1/overview) — branchement direct d'un agent conversationnel sur la donnée
- 🤗 Dataset Hugging Face [`opt-nc/odata-avps`](https://huggingface.co/datasets/opt-nc/odata-avps) — JSONL (une ligne par poste ouvert) **+ embeddings vectoriels au format Parquet**
- 🌐 [Portail web des AVP](https://opt-nc.github.io/odata-avps/) — JSON-LD, sitemap emploi, indexation Google for Jobs
- 📡 [Flux RSS des AVP](https://opt-nc.github.io/odata-avps/index.xml)

### 📕 Le référentiel des métiers

- 🔌 [`metiers-opt` — API du référentiel métiers](https://apigee-optnc-prd-api.apigee.io/docs/metiers-opt/1/overview)
- 🌐 [Site du référentiel des métiers OPT-NC](https://opt-nc.github.io/odata-referentiel-metiers/)
- 💾 [Open data des métiers sur GitHub](https://github.com/opt-nc/odata-referentiel-metiers)

### 💭  Autres référentiels

- [data.gouv.nc](https://data.gouv.nc/pages/accueil/) — l'Open Data de la Nouvelle-Calédonie
- [jsonresume.org](https://jsonresume.org/) — schéma de CV normé

## 💡 Idées

La vidéo ci-dessous montre ce que la donnée AVP permet déjà : trouver le bon poste à partir d'un seul `PROMPT`, et pousser l'analyse du match jusqu'à la datascience.

Elle est là pour vous donner la mesure de ce qui est atteignable en quelques heures une fois branché sur la donnée.

**Ce n'est pas un modèle à reproduire.** C'est juste une idée pour vous inspirer.

{% youtube 5iPqMv49R1c %}

### Préparer son cv efficacement

{% twitter 2092733403007520910 %}

## 📮 Contacts

| Sujet | Interlocuteur |
| ----- | ------------- |
| Donnée AVP, API, serveur MCP, accompagnement technique | Rdv aux ateliers |
| Accueil, logistique de la soirée de lancement | Station N · `station-n@gouv.nc` |
| Partenariats, dotations, mobilisation des entreprises | Commission Data & IA — OPEN NC · `tavron@apid.nc` |


