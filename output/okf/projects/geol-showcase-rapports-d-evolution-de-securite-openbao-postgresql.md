---
type: Project
title: geol-showcase — Rapports d'évolution de sécurité (OpenBao, PostgreSQL)
description: 'Vitrine de ce que permet geol combiné à la data science, à l''IA et
  aux outils DevSecOps : rapports PDF d''évolution de sécurité d''images conteneurs,
  générés en…'
resource: https://github.com/adriens/geol-showcase
tags:
- devsecops
- open-source
- geol
- ai-agents
- solo
timestamp: 2025-09
---

Vitrine de ce que permet geol combiné à la data science, à l'IA et aux outils DevSecOps : rapports PDF d'évolution de sécurité d'images conteneurs, générés en LaTeX à partir de scans Trivy, de métadonnées skopeo et des cycles de vie geol. Chaque rapport est maintenu par un agent IA (Claude Code) guidé par un CLAUDE.md qui documente la méthodologie de mise à jour.
- OpenBao v2.4.0 → v2.7.0 (15 versions, rapport 17 pages) : 235 → 1 vulnérabilité (-99,6 %), score de sécurité 29,1 → 100/100, recommandation de production v2.6.3+
- Scoring CVE pondéré (Critical 10, High 5, Medium 2, Low 1) à dénominateur fixe — scores stables d'une édition à l'autre et comparables entre produits
- Analyse de la dérive de la base CVE : mêmes images re-scannées à 5 dates pour séparer le vrai travail de sécurité de l'artefact de mesure
- Fraîcheur de l'OS de base : croisement geol × historique des tags Docker Hub pour vérifier si chaque image embarquait la dernière Alpine disponible
- Rapport PostgreSQL (versions supportées et EOL) : à l'origine de la publication Zenodo PostgreSQL Security Analysis
- Méthodologie reproductible : Taskfile (rescan de toutes les versions sur une même base Trivy), scripts Bash d'extraction et de scoring

*Type : open-source*

**Tags :** [ai-agents](../tags/ai-agents.md), [devsecops](../tags/devsecops.md), [geol](../tags/geol.md), [open-source](../tags/open-source.md), [solo](../tags/solo.md)
