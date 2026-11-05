---
type: Project
title: Alone With a Stranger — biais de nationalité des LLM open-weight
description: Benchmark à grande échelle du biais de nationalité dans les conseils
  de sécurité donnés par des LLM open-weight à une femme seule avec un homme. Né d'un
  débat…
resource: https://www.kaggle.com/datasets/adriensales/alone-with-a-stranger-analysis-data
tags:
- ai-agents
- data
- open-data
- python
- frugal
- solo
timestamp: 2026-09
---

Benchmark à grande échelle du biais de nationalité dans les conseils de sécurité donnés par des LLM open-weight à une femme seule avec un homme. Né d'un débat France Inter (sept. 2026) sur un reportage RTS fondé sur quelques prompts : automatisé à l'échelle, sur GPU Kaggle gratuits, recalculable par tous. Rapport scientifique « She Is Alone With a Man » (Quarto/R).
- 7 modèles open-weight × 7 425 prompts : 24 nationalités + témoin, 11 situations, 3 âges, 3 paraphrases, 3 tirages
- LLM-as-a-judge en aveugle (Qwen3-32B-AWQ, rubrique rts-v4) + méthode de contrôle sans juge
- Résultat : les 7 modèles complimentent les mêmes hommes (Finlandais, Italiens, Japonais) ; réflexes divergents pour Afghans/Nigérians (déni, risque nommé, refus)
- Nationalité masquée devinée 6× mieux que le hasard par un classifieur de texte ; lexicométrie : qualités vs origine
- Plus gros modèles pas plus justes : le biais change de forme
- 2 datasets Kaggle (réponses + verdicts CC0, PIB/hab. Banque mondiale CC BY 4.0)

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [data](../tags/data.md), [frugal](../tags/frugal.md), [open-data](../tags/open-data.md), [python](../tags/python.md), [solo](../tags/solo.md)
