---
name: edb-noumea-threejs
url: https://github.com/adriens/edb-noumea-threejs
description: "Visualisation 3D (Three.js) des niveaux de pollution des plages de Nouméa — données edb-noumea-data"
language: JavaScript
topics: []
stars: 0
created_at: 2026-07-19
updated_at: 2026-07-24
archived: false
has_readme: true
---

# 🌊 EDB Nouméa — Visualisation 3D

**➡️ Démo en ligne : https://adriens.github.io/edb-noumea-threejs/**

Visualisation interactive en **Three.js** des niveaux de pollution microbiologique
(E. coli & entérocoques) des plages de Nouméa, à partir des données historiques de
[adriens/edb-noumea-data](https://github.com/adriens/edb-noumea-data).

![Aperçu](docs/screenshot.png)

## Lancer

Les modules ES nécessitent un serveur statique (pas de `file://`) :

```bash
python3 -m http.server 8642
# puis ouvrir http://localhost:8642
```

Aucune dépendance réseau : Three.js est vendorisé dans `vendor/`.

## La scène

- **Fond de carte réel de Nouméa** (tuiles CARTO `dark_all`, © OpenStreetMap
  contributeurs · © CARTO), drapé en projection Web-Mercator — barres et côte
  coïncident, le nord est en haut.
- **Un halo par plage**, positionné d'après les coordonnées (approximatives) des
  points de prélèvement.
- **Une paire de barres par point de prélèvement** : E. coli (large, devant) et
  entérocoques (fine, derrière), hauteur en échelle log, en NPP/100 mL.
- **Couleur des barres** = qualité vs seuils réglementaires :
  🟢 bonne · 🟡 acceptable · 🔴 seuil dépassé (les barres rouges pulsent).
  Seuils : E. coli 250 / 1 000 · entérocoques 100 / 370.
- **Anneau autour de chaque plage** = état sanitaire officiel du moment :
  🟢 baignade autorisée · 🟠 déconseillée · 🔴 interdiction temporaire.
- **Timeline** en bas : ~100 campagnes de prélèvement (sept. 2025 → juil. 2026),
  lecture animée ou navigation au curseur. Les **marqueurs colorés** sous le
  curseur signalent les événements sanitaires ; un **bandeau** raconte chaque
  épisode quand la lecture le croise (interdictions 🚫, déconseillées ⚠️,
  ré-autorisations ✅ — tirés de `resume_history.csv`).
- **Survol** d'une barre : valeurs mesurées · **clic** : historique complet du
  point (courbes log avec seuils).

L'ambiance : **océan à reflets réels** (shader `Water` de three.js) visible
jusque dans les baies — les pixels « mer » du fond de carte sont rendus
transparents ; **bloom** sur les émissifs (anneaux, barres en alerte,
étiquettes, lune) ; **lumières de ville** scintillantes échantillonnées sur le
réseau routier de la carte ; **ondes d'alerte** qui se propagent depuis un point
dont la mesure se dégrade pendant la lecture ; **intro cinématique** au
chargement (interrompue par toute interaction) puis orbite lente après 12 s
d'inactivité. Finitions : barres arrondies au vernis physique (`clearcoat`),
dôme de ciel dégradé avec lueur lunaire, vignettage et grain film en
post-traitement.

**Au chargement, le spectacle démarre tout seul** : intro caméra puis lecture
automatique de toute la chronologie (pauses sur les événements). Toute
interaction reprend la main à tout moment.

Deep-links : `?date=2025-12-17` ouvre la timeline à cette date,
`?point=P18031` ouvre le panneau historique d'un point — ces deux liens
désactivent l'autoplay, comme `?play=0` ; `?nointro=1` saute l'intro caméra.

## Mettre à jour les données

```bash
# rafraîchir les CSV depuis le repo source
for f in beaches details details_history resume resume_history; do
  curl -s -o data/$f.csv "https://raw.githubusercontent.com/adriens/edb-noumea-data/main/data/$f.csv"
done

# régénérer js/data.js
node tools/build-data.mjs

# régénérer le fond de carte (assets/map.png + js/map-meta.js ; requiert ImageMagick)
node tools/fetch-map.mjs
```

## Notes

- Les coordonnées des points de prélèvement (`tools/build-data.mjs`) sont
  **approximatives** : elles servent au placement relatif dans la scène, pas à la
  cartographie.
- L'état sanitaire (anneaux) provient de `resume_history.csv` (arrêtés de la
  ville) et peut différer ponctuellement de la couleur des barres : les mesures
  et les décisions n'évoluent pas exactement au même rythme.