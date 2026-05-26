# YouTube — Chaîne devops-lab

Vidéos, playlists et statistiques de la chaîne YouTube `devops-lab`.

```sh
task fetch-youtube          # vidéos + stats
task fetch-youtube-playlists  # playlists uniquement
```

```mermaid
flowchart LR
    T([task fetch-youtube]) --> P[fetch-youtube-channel.py]
    P <-->|yt-dlp| A[youtube.com]
    P --> F[(videos/*.md\nplaylists/*.md\n_index.csv\n_stats.json)]
    F --> KB([knowledge-base.md])
```
