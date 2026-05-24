---
name: unc-temps-attente-nextjs
url: https://github.com/adriens/unc-temps-attente-nextjs
description: "Un front-end NEXT.js  pour localiser les agences de l'OPT-NC"
language: TeX
topics: []
stars: 0
created_at: 2025-06-30
updated_at: 2025-10-10
archived: false
has_readme: true
---

# Installation et démarrage du projet

Ce projet **Next.js** affiche les agences et leurs informations via l'API de l'OPT, avec recherche et géolocalisation.

---

##  Prérequis

- [Node.js](https://nodejs.org) (version ≥ 14 recommandée)
- [npm](https://www.npmjs.com/) (installé avec Node.js)

---

##  Installation

1. Cloner le dépôt et s'y positionner :
   ```bash
   git clone https://github.com/adriens/unc-temps-attente-nextjs.git
   cd unc-temps-attente-nextjs

2. Installer les dépendances:
   ```bash
   npm install

3. Ajouter une clé API pour accéder au portail OPT (via [Apigee](https://apigee-optnc-prd-api.apigee.io)) :\
    Créer un fichier .env.local à la racine avec :
   ```bash
   API_KEY=TaCleAPI_GENEREE_sur_le_portail_APIGEE

##  Démarrage en local
1. Pour lancer le serveur de développement (hot-reload inclus) : 
    ```bash
    npm run dev

2. Ouvre en suite ton navigateur sur : http://localhost:3000

# ❔ A propos

Chaque année, l'[Université de Nouvelle-Calédonie](https://unc.nc/) challenge ses étudiants
sur des projets tutorés afin de leur donner une première expérience de développement 
sur des problématiques en lien avec le monde de l'entreprise.

# 🍿 Video introductive

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yOAKC5cTDc8/0.jpg)](https://www.youtube.com/watch?v=yOAKC5cTDc8)

# ℹ️ Définition

Selon [leur définition](https://iut.unc.nc/espace-entreprises/projets-tutores/), les projets tutorés

> "[...] répondent à la commande d’une entreprise sur laquelle travaillent les étudiantes et étudiants en groupe de 3 à 5, tout au long de l’année. Contrairement au stage, les étudiantes et étudiants ne sont pas présents en entreprise, mais s’y rendent pour des réunions."

> "Quelques exemples : optimisation de coûts d’importation, création d’un service de vente à domicile, réalisation de vidéos 360°, création d’un chatbot, application web et mobile, mains myoélectriques en 3D, etc."

## ➡️  Processus

1. L'UNC **lance un appel** à projets auprès des entreprises
2. Les tuteurs des **entreprises fournissent** une liste de sujets
3. Les **étudiants choisissent** un sujet
4. Les **développements** sont opérés
5. Un support de présentation est livré
6. Un rapport de projet est livré
7. La soutenance projet est **assurée par les étudiants à l'Université** en la présence de l'équipe pédagogique et du tuteur
8. **L'entreprise évalue** le travail fourni

# 📦 Livrables

Le tuteur produire l'évaluation finale dès lors que les livrables ci-dessous auront été soumis aux tuteur

- 📰 Support de présentation au format pdf (**une semaine avant la soutenance pour review**)
- 📘 Rapport au formal pdf (**une semaine avant souteance pour review**)
- 🎦 Démo video au format `mp4` (`20'` max) livrée par les étudiants durant laquelle le produit est démontré, et pour un public général (que l'OPT utilisera sur [`dev.to/optnc`](https://dev.to/optnc))

**☝️ L'évaluation du projet sera effectuée dès lors que tous ces élements auront été fournis en temps et en heure,
au plus tard une semaine avant la soutenance. Faute de quoi deux options :**

- L'évaluation sera **livrée une semaine après obtention des livrables**
- L'évaluation est malgré tout livrée mais **sur la base d'une copie blanche**


## 🎙️ Pitch

Ci-dessous l'elevator pitch : 

> Ce projet tutoré a pour but de ....

## 🤝 DoD (_Definition of Done_)

Ci-dessous les éléments qui permettent de définir que l'objectif aura été atteint:

- ✔️ Objectif 1
- ✔️ Objectif 2


# 🏆 Projets tutorés remarquables

Ci-dessous une sélection de projets tutorés remarquables:

- [`domaine-nc-javafx`](https://github.com/adriens/domaine-nc-javafx) (_"Application JavaFX pour consulter les données de DOMAINE.nc "_)
- [🧑‍🎓 Follow package delivery in New-Caledonia w/ Discord 🤖](https://dev.to/optnc/follow-delivery-in-new-caledonia-with-rapidapi-4bh9)
- [🤖 Un assistant en réalité augmentée pour suivre la livraison de ses colis](https://youtu.be/ddqJ-ZAlk9U)
- [🙌 API marketplace & Open Innovation w/ UNC students 🎓](https://dev.to/optnc/api-marketplace-open-innovation-w-unc-students-50fc)
- [📊 Benefits of a historic wait time API: apigee developer portal & Streamlit](https://dev.to/adriens/benefits-of-a-historic-wait-time-api-apigee-developer-portal-streamlit-2d9a)

👉... à vous de jouer pour y inscrire le votre 💪.

<table>
  <tr>
    <td>
        <a href = "https://office.opt.nc/"><img src="https://raw.githubusercontent.com/opt-nc/.github/main/img/nc_opt.gif" width="200"/></a>
    </td>
    <td>
        <a href="https://rapidapi.com/organization/opt-nc" target="_blank">
            <img src="https://storage.googleapis.com/rapidapi-documentation/connect-on-rapidapi-dark.png" width="215" alt="Connect on RapidAPI">
        </a>
    </td>
    <td>
        <a href="https://hub.docker.com/u/optnc" target="_blank">
            <img src="https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png" width="100"/>
        </a>
    </td>
    <td>
        <a href="https://dev.to/optnc" target="_blank">
            <img src="https://d2fltix0v2e0sb.cloudfront.net/dev-black.png" width="150"/>
        </a>
    </td>
    <td>
        <a href="https://killercoda.com/opt-labs/" target="_blank">
            <img src="https://avatars.githubusercontent.com/u/88902003?s=200&v=4" width="150"/>
        </a>
    </td>
  </tr>
</table>