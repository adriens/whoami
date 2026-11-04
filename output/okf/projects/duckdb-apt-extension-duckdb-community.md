---
type: Project
title: duckdb-apt — Extension DuckDB Community
description: 'Extension officielle DuckDB Community (sœur Debian/Ubuntu de duckdb-brew)
  permettant de requêter en SQL le gestionnaire de paquets apt/dpkg : paquets installés…'
resource: https://github.com/adriens/duckdb-apt
tags:
- data
- duckdb
- open-source
- maintainer
- international
- packaging
- devsecops
- linux
- debian
- saga
timestamp: 2026-10
---

Extension officielle DuckDB Community (sœur Debian/Ubuntu de duckdb-brew) permettant de requêter en SQL le gestionnaire de paquets apt/dpkg : paquets installés, dépendances, dépôts et leur niveau de confiance, provenance de chaque paquet, mises à jour en attente et historique des changements. Lecture directe des fichiers dpkg/apt (sans sous-processus) via le file system DuckDB, paramètre root pour auditer une image disque ou un conteneur monté. Acceptée sur duckdb.org le 2026-11-02.
- Listée officiellement sur duckdb.org/community_extensions/extensions/apt — documentation : https://adriens.github.io/duckdb-apt/
- Posture sécurité supply chain en SQL : paquets orphelins, dépôts tiers ou non signés, dépôts expirés, mises à jour de sécurité en attente, purl pour les scanners (OSV, Grype, Dependency-Track)
- Base DuckDB prête à l'emploi (tables + clés + vues commentées) enrichie des vulnérabilités connues via OSV.dev, et rapport PDF de sécurité généré en Quarto
- Écrite en C++, testée en CI sur Debian 12/13 et Ubuntu 22.04/24.04/26.04 (comparaison avec apt list --upgradable)

*Type : open-source*

**Tags :** [data](../tags/data.md), [debian](../tags/debian.md), [devsecops](../tags/devsecops.md), [duckdb](../tags/duckdb.md), [international](../tags/international.md), [linux](../tags/linux.md), [maintainer](../tags/maintainer.md), [open-source](../tags/open-source.md), [packaging](../tags/packaging.md), [saga](../tags/saga.md)
