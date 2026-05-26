# Dev.to — Articles @adriens & @opt-nc

Articles publiés sur Dev.to, deux comptes : `adriens` (perso) et `opt-nc` (institutionnel).

```sh
task fetch-devto
```

```mermaid
flowchart LR
    T([task fetch-devto]) --> P[fetch-devto-articles.py]
    P <-->|REST API| A[dev.to]
    P --> F[(articles/*.md\n_index.csv)]
    F --> KB([knowledge-base.md])
```
