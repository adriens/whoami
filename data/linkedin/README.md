# LinkedIn — Adrien Sales

Données LinkedIn : articles Pulse, recommandations reçues et données. Pas d'API publique — alimentation **manuelle via Claude Code**.

## Mise à jour

Coller le contenu brut LinkedIn dans Claude Code. Le workflow complet (parsing, tagging, fichiers, resume.json, commit/tag) est documenté dans `CLAUDE.md`.

## Processus

```mermaid
flowchart LR
    U([Contenu LinkedIn brut]) --> CC[Claude Code]
    CC --> F[(recommendations/*.md\nrecommendations-given/*.md\narticles/*.md\n_index.csv)]
    CC -->|x-tags + métadonnées| R[(resume.json\nreferences[])]
    F & R --> KB([knowledge-base.md])
```

## Propagation des métadonnées

Chaque recommandation reçue est dupliquée dans deux endroits :

| Destination | Contenu | Rôle |
|---|---|---|
| `recommendations/*.md` | Texte brut + frontmatter | Dataset brut, knowledge base |
| `resume.json → references[]` | Texte + champs `x-*` | Source de vérité CV, filtrage par offre |

Les champs `x-*` dans `references[]` sont la clé du système :
- `x-tags` — taxonomie canonique cross-section, permet de générer des versions light du CV par offre (ex: ne garder que les recos taggées `data` ou `opt-nc`)
- `x-source` — origine (`LinkedIn`, `YouTube`) — permet de filtrer par canal
- `x-relationship` — type de relation (manager, prestataire, étudiant...) — filtrage par contexte
- `x-date` — date de la recommandation — tri chronologique
- `x-url` — lien source pour les recos non-LinkedIn (YouTube clips, etc.)

Les recommandations **données** (`recommendations-given/`) sont **data-only** : elles n'alimentent pas `references[]` dans `resume.json`.
