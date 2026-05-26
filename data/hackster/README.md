# Hackster.io — Projets @adriensales

Projets hardware/IoT publiés sur Hackster.io par `adriensales`.

```sh
task fetch-hackster
```

```mermaid
flowchart LR
    T([task fetch-hackster]) --> P[fetch-hackster-projects.py]
    P <-->|Algolia API + scraping HTML| A[hackster.io]
    P --> F[(projects/*.md\n_index.csv\n_stats.json)]
    F --> KB([knowledge-base.md])
```
