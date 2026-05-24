---
name: temps-attente-streamlit
url: https://github.com/adriens/temps-attente-streamlit
description: "Front-end web API driven sur Streamlit qui présente les temps d'attente en Agence à l'OPT Nouvelle-Calédonie"
language: Python
topics: [api-client, apigee, docker, innovation, internship-project, streamlit-application, streamlit-dashboard, streamlit-webapp, student-project, web]
stars: 0
created_at: 2024-09-19
updated_at: 2025-09-25
archived: true
has_readme: true
---

# ❔ A propos

Chaque année, l'[Université de Nouvelle-Calédonie](https://unc.nc/) challenge ses étudiants
sur des projets tutorés afin de leur donner une première expérience de développement 
sur des problématiques en lien avec le monde de l'entreprise.

# 🧑‍🤝‍🧑 Team

- 👦 LEAD Dev : [Malcolm Bertaina](https://github.com/MalcolmBrt)
- 👦 Dev : [Morgan CARRE](https://github.com/morgancarre)
- 🧔 PO/Tuteur : [Adrien](https://dev.to/adriens)
- 👱‍♀️ Dev Expert : [Michèle BARRE](https://github.com/mbarre/)
- 🧑‍💻 API support : [Vinh Faucher](https://github.com/Supervinh)

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

Le tuteur produira l'évaluation finale dès lors que les livrables ci-dessous auront été soumis au tuteur :

- 📰 Support de présentation au format pdf (**une semaine avant la soutenance pour review**)
- 📘 Rapport au format pdf (**une semaine avant soutenance pour review**)
- 🎦 Démo vidéo au format mp4 (20' max) livrée par les étudiants, démontrant le produit pour un public général (que l'OPT utilisera sur [dev.to/optnc](https://dev.to/optnc))

**☝️ L'évaluation du projet sera effectuée dès lors que tous ces éléments auront été fournis en temps et en heure,
au plus tard une semaine avant la soutenance. Faute de quoi, deux options :**

- L'évaluation sera **livrée une semaine après obtention des livrables**
- L'évaluation est malgré tout livrée mais **sur la base d'une copie blanche**

# 🚀 Lancer le projet

Voici comment lancer le projet sur votre machine :

```sh
# Cloner le dépôt
git clone https://github.com/adriens/temps-attente-streamlit
cd temps-attente-streamlit

# Builder l'image  
docker build -t hellooptnc .

# Créer un fichier .env avec les clés API
OPTNC_WAITINGTIME_APIKEY=[clé API APIGEE]
OPTNC_WAITINGTIME_APIKEY_RAPIDAPI=[clé API Rapidapi]

# Démarrer l'application via Docker  
docker run -p 80:8501 --env-file .env hellooptnc
```

Pour accéder à l'application, aller sur : http://localhost

```sh
xdg-open http://localhost
```

👀 **Vérifier** que la page web s'affiche 

![image](https://github.com/user-attachments/assets/c89221c0-4c13-4d10-8ec7-09fd1b77811f)




# 🎙️ Pitch

Ci-dessous l'elevator pitch :

> Ce projet tutoré a pour but de fournir une application web responsive (TV, PC, tablette) développée sur Streamlit, sous forme d'image Docker, et
> qui permet d'afficher en direct le temps d'attente d'une agence en direct, ainsi que la tendance de la journée afin d'optimiser l'expérience client.

# 🤝 DoD (_Definition of Done_)

Ci-dessous les éléments qui permettent de définir que l'objectif aura été atteint :

- ✔️ On peut démarrer l'application comme une image Docker sous Linux
- ✔️ Le site web consomme l'API depuis le portail d'API APIGEE
- ✔️ On peut choisir une agence via un menu
- ✔️ On peut choisir une agence et afficher son temps d'attente avec un dataviz simple et éclairant
- ✔️ On peut voir l'historique de la journée, la tendance afin d'optimiser sa venue en agence


# 🏆 Projets tutorés remarquables

Ci-dessous une sélection de projets tutorés remarquables :

- [domaine-nc-javafx](https://github.com/adriens/domaine-nc-javafx) (_"Application JavaFX pour consulter les données de DOMAINE.nc "_)
- [🧑‍🎓 Follow package delivery in New-Caledonia w/ Discord 🤖](https://dev.to/optnc/follow-delivery-in-new-caledonia-with-rapidapi-4bh9)
- [🤖 Un assistant en réalité augmentée pour suivre la livraison de ses colis](https://youtu.be/ddqJ-ZAlk9U)
- [🙌 API marketplace & Open Innovation w/ UNC students 🎓](https://dev.to/optnc/api-marketplace-open-innovation-w-unc-students-50fc)

👉 ... à vous de jouer pour y inscrire le vôtre 💪.

<table>
  <tr>
    <td>
        <a href="https://office.opt.nc/"><img src="https://raw.githubusercontent.com/opt-nc/.github/main/img/nc_opt.gif" width="200"/></a>
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