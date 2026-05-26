# Goodreads — Livres lus

Livres marqués "read" sur le profil Goodreads `124105866`.

```sh
task fetch-goodreads
```

```mermaid
flowchart LR
    T([task fetch-goodreads]) --> P[fetch-goodreads.py]
    P <-->|RSS feed| A[goodreads.com]
    P --> F[(books/*.md\n_index.csv)]
    F --> KB([knowledge-base.md])
```
