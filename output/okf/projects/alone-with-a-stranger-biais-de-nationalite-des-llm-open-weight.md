---
type: Project
title: Alone With a Stranger — biais de nationalité des LLM open-weight
description: Benchmark à grande échelle du biais de nationalité dans les conseils
  de sécurité donnés par des LLM open-weight à une femme seule avec un homme. Né d'un
  débat…
resource: https://github.com/adriens/kaggle-bench-ai-biasses
tags:
- ai-agents
- data
- open-data
- python
- frugal
- solo
timestamp: 2026-09
---

Benchmark à grande échelle du biais de nationalité dans les conseils de sécurité donnés par des LLM open-weight à une femme seule avec un homme. Né d'un débat France Inter (sept. 2026) sur un reportage RTS fondé sur quelques prompts : automatisé à l'échelle, sur GPU Kaggle gratuits, recalculable par tous. Rapport scientifique « She Is Alone With a Man » (Quarto/R) publié sur Zenodo (DOI 10.5281/zenodo.23991568) ; code et données publics sur GitHub, Kaggle.
- 7 modèles open-weight × 7 425 prompts : 24 nationalités + témoin, 11 situations, 3 âges, 3 paraphrases, 3 tirages
- LLM-as-a-judge en aveugle (Qwen3-32B-AWQ, rubrique rts-v4) + méthode de contrôle sans juge
- Résultat : les 7 modèles complimentent les mêmes hommes (Finlandais, Italiens, Japonais) ; réflexes divergents pour Afghans/Nigérians (déni, risque nommé, refus)
- Nationalité masquée devinée 6× mieux que le hasard par un classifieur de texte ; lexicométrie : qualités vs origine
- Plus gros modèles pas plus justes : le biais change de forme
- 2 datasets Kaggle (réponses + verdicts, PIB/hab. Banque mondiale — CC BY 4.0) + 11 notebooks, collection kaggle.com/work/collections/19371544
- Plus le pays est riche, plus l'IA est chaleureuse : compliments corrélés au PIB/hab. (Spearman ρ = 0,73), y compris au sein d'un même continent
- Frugal : 89 h GPU (2 × T4) + 6 h CPU, 0 € — tout sur le quota gratuit Kaggle
- Rapport Zenodo en 4 formats (91 p., version 7 p., carrousel 16 slides, 4 visuels carrés) : DOI 10.5281/zenodo.23991568

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [data](../tags/data.md), [frugal](../tags/frugal.md), [open-data](../tags/open-data.md), [python](../tags/python.md), [solo](../tags/solo.md)
