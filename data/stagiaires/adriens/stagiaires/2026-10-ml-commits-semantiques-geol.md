---
slug: 2026-10-ml-commits-semantiques-geol
name: "Lucas Katjawan"
school: "Université de Nouvelle-Calédonie"
formation: "Licence Informatique"
type: stage
employer: "OPT-NC"
uo: "DSI/SMO/GLIA"
date_cadrage: 2026-07-22
date_debut: 2026-10
date_soutenance: ""
status: planned
etudiants: ["Lucas Katjawan"]
origins:
  "Lucas Katjawan": "Nouméa"
subject: "ML/NLP — classification des messages de commits sémantiques sur le code source de geol"
current_position: "Étudiant — Licence Informatique UNC"
url_git: "https://github.com/opt-nc/geol"
url_youtube: ""
url_article: ""
tags: [ml, data-science, nlp, embeddings, python, huggingface, kaggle, open-source, open-data, devsecops, go, pedagogy, unc-partnership, opt-nc, nouvelle-caledonie]
---

Stage à démarrer en octobre 2026. Cadrage présenté à Lucas Katjawan lors de l'entrevue du **22 juillet 2026**, puis sujet rendu public devant la Licence Info UNC lors de la présentation de `geol` à la Station N le 6 août 2026 (commissions Data-IA et Cyber réunies) — l'auditoire comptait des étudiants et enseignants de la Licence Informatique de l'UNC.

## Sujet

Analyser la data du code source de [geol](https://github.com/opt-nc/geol) — spécifiquement l'historique de **commits sémantiques**, sur deux variables :

- le **message** du commit (texte)
- le **verbe / type** (`fix`, `feat`, `doc`, `ci`…)

Le repo sert de terrain de recherche appliquée : historique de commits suivant une convention structurée (`type(scope): verb entity`), volume suffisant, et projet open source activement maintenu. Référence sur les pratiques de commits du projet : [Better collab flows w/ git conventional commits](https://dev.to/optnc/better-collab-flows-w-git-conventional-commits-49j8).

## Attendus

1. Vérifier et classer les commits par ML / DL / NLP — techniques laissées au choix du stagiaire selon la suite de son parcours
2. Évaluer si les commits sont réellement bien classables et si le **verbe est prédictible** — notamment à l'aide d'**embeddings**
3. **Benchmarker** les différentes méthodes et déterminer l'approche optimale en termes de qualité
4. Généraliser : appliquer l'approche retenue à des repos open source **n'implémentant pas** les commits sémantiques — quitte à produire un dataset dédié, manuel ou synthétique

## Cadre

- **Stack** : Kaggle, Hugging Face
- **Travail strictement public**, sous la même licence que geol — open source et open data de bout en bout
- **Livrables** : rapport de stage LaTeX/Quarto (rendu scientifique) + vidéo
- **Sujet volontairement très ouvert** — dépendant de ce qui sera découvert et des aspirations du stagiaire
- Réserve : ne pas publier d'annonce de faille de sécurité exploitable de geol au moment de la publication du rapport
- Portfolio-ready par construction : la nature open source rend le travail directement partageable par le stagiaire

## Antériorité

- Travail d'amorce d'Adrien sur l'analyse de commits d'un autre projet open source, présenté au PMI Horizons Nouméa 2026 : https://youtu.be/hcXYVpWKjqA?t=2240
- Document et vidéo dédiés à produire par Adrien avant le démarrage, pour inspirer le travail à venir
- Lignée directe avec le stage de Thomas Quillet (2022) — dataviz & ML sur les tickets GitHub avec BERT ([2022-12-01-thomas-quillet](2022-12-01-thomas-quillet.md))

## Corpus — état au 2026-08-08

Mesure faite sur `opt-nc/geol` (branche par défaut) avant le démarrage du stage. Le repo étant actif, ces chiffres auront évolué en octobre — la commande de reproduction est donnée plus bas.

| Catégorie | N | Statut |
|---|---:|---|
| Commits bruts | 877 | — |
| Merges + « Auto-merge main back to dev » | 405 | Bruit d'automatisation — à exclure |
| `chore(deps)` dependabot | 127 | Template généré — à exclure ou isoler |
| Non-conventionnels humains | ~35 | Non étiquetés |
| **Commits conventionnels humains** | **310** | **Corpus étiqueté exploitable** |

Répartition des 310 commits étiquetés :

| Type | N | Part |
|---|---:|---:|
| `fix` | 104 | 34 % |
| `feat` | 97 | 31 % |
| `doc` | 45 | 15 % |
| `chore` | 45 | 15 % |
| `ci` | 9 | 3 % |
| `refactor` | 6 | 2 % |
| `docs` / `site` | 4 | 1 % |

### À cadrer avant la première expérimentation

1. **Écarter ou isoler les 127 commits dependabot.** Tous de la forme `chore(deps): bump X from A to B` — classés à 100 % sans rien apprendre, ils gonflent artificiellement l'accuracy globale. Mesurer et publier l'écart avec/sans bots est un résultat en soi.
2. **Quatre classes exploitables, pas six.** `fix`, `feat`, `doc` et `chore` ont 45 à 104 exemples. `ci` (9) et `refactor` (6) sont sous le seuil d'apprentissage : les fusionner dans `chore` ou les écarter en annonçant la limite. Normaliser `docs` → `doc` (variante orthographique) et statuer sur `site` (type hors convention).
3. **Neutraliser la fuite de signal.** Les messages contiennent souvent le verbe en clair (`add`, `fix`, `enrich`). Masquer le préfixe **et** le verbe canonique, sinon la tâche est triviale et le benchmark ne mesure rien.

### Volume et choix de méthode

310 exemples, c'est peu pour un fine-tuning complet (sur-apprentissage probable) mais correct pour des embeddings pré-entraînés suivis d'un classifieur léger (kNN, régression logistique). Le benchmark TF-IDF vs embeddings vs fine-tuning a d'autant plus d'intérêt qu'à ce volume, l'approche la plus simple peut gagner.

### Piste corpus multi-repos

`whoami` (taxonomie encore plus stricte : `type(scope): verb entity`, verbes fermés), `domaine-nc`, `colis-nc` et les autres repos opt-nc partagent la convention. Un corpus agrégé dépasse largement le millier de commits humains étiquetés, et surtout permet un **test de généralisation mesurable dès le départ** — entraîner sur geol, tester sur un autre repo — au lieu de le réserver à la fin du stage.

### Reproduire ces chiffres

```sh
git clone --filter=blob:none --no-checkout https://github.com/opt-nc/geol.git
cd geol
git rev-list --count HEAD                       # total brut
git log --pretty=format:'%an|%s' | uv run python -c "
import sys, re
from collections import Counter
bots, humans = Counter(), Counter()
for l in sys.stdin:
    an, _, s = l.strip().partition('|')
    m = re.match(r'^([a-zA-Z]+)(\([^)]*\))?!?:', s)
    if not m: continue
    (bots if '[bot]' in an else humans)[m.group(1).lower()] += 1
print('type      bot   humain')
for t in sorted(set(bots) | set(humans), key=lambda x: -(bots[x] + humans[x])):
    print(f'{t:10} {bots[t]:4d}   {humans[t]:4d}')
"
```

Dates précises de début et de soutenance à compléter au démarrage.
