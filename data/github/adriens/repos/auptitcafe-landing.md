---
name: auptitcafe-landing
url: https://github.com/adriens/auptitcafe-landing
description: ""
language: CSS
topics: []
stars: 0
created_at: 2026-07-31
updated_at: 2026-07-31
archived: false
has_readme: true
---

# Au P'tit Café — la cuisine réconfort de Nouméa

Une landing page pour **Au P'tit Café**, un vrai café-restaurant de Nouméa
(Nouvelle-Calédonie), construite pour le hackathon
[DEV "Perfect Landing: Comfort Food"](https://dev.to/challenges/frontend-2026-07-29).

**🔗 Site en ligne : https://adriens.github.io/auptitcafe-landing/**

![Capture d'écran de la landing Au P'tit Café](docs/screenshot.jpg)

## Le principe

Plutôt qu'une carte inventée, ce site affiche le **vrai menu du moment** et
**un an d'historique réel**, tirés du jeu de données ouvert
[`auptitcafe-data`](https://github.com/adriens/auptitcafe-data).

- **Le menu du moment** — les plats de la semaine (Terre / Mer / Végé, soupe,
  suggestion du soir, desserts) avec prix, recettes et photos.
- **Le plat de la signature** — mis en avant avec son historique de présence
  sur la carte.
- **La machine à remonter le temps** — un curseur pour parcourir plus d'un an
  de cartes hebdomadaires, semaine par semaine.

## Une page qui se met à jour toute seule

Le dépôt [`auptitcafe-data`](https://github.com/adriens/auptitcafe-data) fait
tourner sa propre GitHub Action **chaque mardi à 12h00 UTC** (`0 12 * * 2`)
pour récupérer la nouvelle carte du restaurant et la commiter. Cette page lit
ces données **en direct** (`raw.githubusercontent.com`) à chaque chargement,
avec un repli automatique sur une copie embarquée si la source est
inatteignable. Résultat : **aucune intervention humaine** entre le moment où
le café change son menu et le moment où le site l'affiche.

```
auptitcafe.nc → auptitcafe-data (auto) → raw GitHub → cette landing (lecture live) → GitHub Pages
```

Le déploiement suit le même principe : chaque `push` sur `main` déclenche une
GitHub Action qui build et republie le site automatiquement (voir
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)).

## Stack

- [Vite](https://vitejs.dev/) + JavaScript vanilla (pas de framework)
- [Bun](https://bun.sh/) comme gestionnaire de paquets et runtime
- Zéro dépendance de production — un parseur CSV maison, une palette
  tropicale chaude, thème clair/sombre, animations au scroll

## Développer en local

```bash
bun install
bun run dev       # serveur de dev
bun run build     # build de production dans dist/
bun run preview   # prévisualiser le build
```

## Crédits

- Données : [adriens/auptitcafe-data](https://github.com/adriens/auptitcafe-data)
- Photos : [auptitcafe.nc](https://auptitcafe.nc)
- Réalisé pour le défi [DEV Perfect Landing: Comfort Food](https://dev.to/challenges/frontend-2026-07-29)