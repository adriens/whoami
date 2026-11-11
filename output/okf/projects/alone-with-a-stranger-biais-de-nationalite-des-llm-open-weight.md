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
- international
- civic-tech
- responsible-ai
timestamp: 2026-09
---

Benchmark à grande échelle du biais de nationalité dans les conseils de sécurité donnés par des LLM open-weight à une femme seule avec un homme. Né d'un débat France Inter (sept. 2026) sur un test viral relayé par RTS, sans nombre de prompts déclaré ni témoin : automatisé à l'échelle, sur GPU Kaggle gratuits, recalculable par tous. Rapport scientifique « She Is Alone With a Man » (Quarto/R) publié sur Zenodo (DOI 10.5281/zenodo.23991568), positionné face au rapport ONU A/HRC/56/68 ; code et données publics sur GitHub, Kaggle.
- 7 modèles open-weight × 7 425 prompts : 24 nationalités + témoin, 11 situations, 3 âges, 3 paraphrases, 3 tirages
- LLM-as-a-judge en aveugle (Qwen3-32B-AWQ, rubrique rts-v4) + méthode de contrôle sans juge
- Résultat : les 7 modèles complimentent les mêmes hommes (Finlandais, Italiens, Japonais) ; réflexes divergents pour Afghans/Nigérians (déni, risque nommé, refus)
- Nommer une nationalité suffit : réponses à préjugés de 3 % (« un homme ») à 62 % dès qu'il en a une, quelle qu'elle soit (4 modèles ≥ 8B, taxi, ascenseur, rue isolée)
- Nationalité masquée devinée 6× mieux que le hasard par un classifieur de texte ; lexicométrie : qualités vs origine
- Plus gros modèles pas plus justes : le biais change de forme
- 2 datasets Kaggle (réponses + verdicts, PIB/hab. Banque mondiale — CC BY 4.0) + 11 notebooks, collection kaggle.com/work/collections/19371544
- Plus le pays est riche, plus l'IA est chaleureuse : compliments corrélés au PIB/hab. (Spearman ρ = 0,73), y compris au sein d'un même continent
- Frugal : 89 h GPU (2 × T4) + 6 h CPU, 0 € — tout sur le quota gratuit Kaggle
- Positionnement ONU (v1.5) : l'alerte (RTS), le cadre (rapport A/HRC/56/68 de la Rapporteuse spéciale sur le racisme), la mesure. 13 questions sur 15 mesurées, matrice sourcée paragraphe par paragraphe ; 4 recommandations (§68 d, k, m, f) traduites en protocole reproductible — « The UN asks for tests; here is one. »
- Rapport Zenodo en 7 PDF (92 p., version 8 p., carrousel 16 slides, visuels carrés, positionnement ONU 10 p. + 6 p.), 5 versions publiées avec changelog — résultats inchangés : DOI 10.5281/zenodo.23991568

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [civic-tech](../tags/civic-tech.md), [data](../tags/data.md), [frugal](../tags/frugal.md), [international](../tags/international.md), [open-data](../tags/open-data.md), [python](../tags/python.md), [responsible-ai](../tags/responsible-ai.md), [solo](../tags/solo.md)
