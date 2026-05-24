---
name: auptitcafe-slideshow
url: https://github.com/adriens/auptitcafe-slideshow
description: "Slideshow des menus du restaurant \"Au p'tit café\""
language: TypeScript
topics: []
stars: 0
created_at: 2025-08-14
updated_at: 2025-08-15
archived: false
has_readme: true
---

# Au P'tit Café - Diaporama du Menu

Cette application a été créée avec Next.js et affiche le menu du jour pour le restaurant "Au P'tit Café" sous la forme d'un diaporama élégant. Elle est conçue pour être affichée sur une tablette ou un écran dans le restaurant.

L'application récupère les données du menu en temps réel à partir d'un fichier CSV distant, garantissant que le menu affiché est toujours à jour.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé :

*   [Node.js](https://nodejs.org/) (version 18.x ou plus récente est recommandée)
*   [npm](https://www.npmjs.com/) (généralement inclus avec Node.js)

## Démarrage

Suivez ces étapes pour lancer l'application en local.

**1. Installation des dépendances**

Ouvrez un terminal à la racine du projet et exécutez la commande suivante pour installer toutes les dépendances nécessaires :

```bash
npm install
```

**2. Lancement du serveur de développement**

Une fois les dépendances installées, lancez le serveur de développement avec la commande :

```bash
npm run dev
```

**3. Visualisation**

Ouvrez votre navigateur et rendez-vous à l'adresse [http://localhost:3000](http://localhost:3000).

Le diaporama du menu devrait s'afficher et commencer à défiler automatiquement.

## Fonctionnalités

*   **Mise à jour en direct** : Le menu est chargé depuis une source de données distante à chaque visite.
*   **Diaporama automatique** : Les plats défilent à un intervalle régulier.
*   **Navigation** : Contrôlez le diaporama avec les flèches de navigation à l'écran, les gestes tactiles sur tablette, ou les flèches gauche et droite du clavier.
*   **Design réactif** : L'affichage s'adapte à différentes tailles d'écran.