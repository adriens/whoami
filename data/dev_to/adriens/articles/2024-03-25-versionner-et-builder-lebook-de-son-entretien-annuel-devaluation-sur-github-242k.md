---
comments: 10
id: 1056317
is_dev_challenge: false
published_at: '2024-03-25T21:35:21Z'
reactions: 2
reading_time_minutes: 6
tags:
- markdown
- pandoc
- ebook
- ai
title: 📓 Versionner et builder l'eBook de son Entretien Annuel d'Evaluation sur Git(Hub)
url: https://dev.to/adriens/versionner-et-builder-lebook-de-son-entretien-annuel-devaluation-sur-github-242k
---

## 🪝 Contexte

Chaque année nous utilisons [monportailrh.nc](https://www.monportailrh.nc/) pour saisir notre [Entretien annuel d'échange](https://drhfpnc.gouv.nc/formulaires-agents/entretien-annuel-dechange) : 

- L'atteinte des objectifs passés
- Les objectifs de l'année à venir

Ainsi que d'autres éléments liés par exemple à la performance des agents ou aux conditions de travail et moyens (matériel, formation, ...).

## 🎬 Live démo 🍿

{% youtube FRVsA7NoZv8 %}

## 👉 Deux points remarquables

Sur le site, on a :

- La possibilité d'activer un mode collaboratif où les deux parties (manager et collaborateur) **saisissent des changements dans les mêmes champs, en même temps**
- Des zones de texte éditables... **où le dernier qui saisit à raison** (la dernière modification écrase la précédente)

Or, lors du processus de saisie et réflexion :

- Il peut arriver que l'on arrive à **expiration de la session**
- Les zones de texte sont en **texte brut**
- Les **zones texte doivent être étirées** lorsque l'on charge du contenu

Pour contourner cela j'ai alors commencé à saisir mes contenus en [`markdown`](https://fr.wikipedia.org/wiki/Markdown) directement et à **utiliser ce contenu comme base de discussion avec mon manager**, 

> depuis mon éditeur de code préféré pour ce genre de chose : [VsCode](https://youtu.be/HcZHcpVCYc8?t=166)... puis à le copier/coller dans les formulaires.

La sensation était que disposer d'un **affichage stylé** (liste, paragraphes, liens, ...) était extrêmement confortable et changeait totalement mon expérience de l'[EAE](https://drhfpnc.gouv.nc/formulaires-agents/entretien-annuel-dechange) (Entretien Annuel d'Echange),** y compris dans le processus de collaboration avec mon manager.**

> Je venais de découvrir une toute nouvelle et excitante expérience utilisateur.

## 💡 Les idées

Et puis un jour... un flot d'idées à commencé à s'imposer : 

> **_
> Ça serait super cool (et un peu geek) de traiter mon EAE avec nos outils de dev et de charger tout cela sur GitHub pour collaborer dessus !_**

Puis, juste quelques jours plus tard :

> **_Et si... J'en profitais même pour mettre une chaîne de build autour ces données ?_**

Dès lors, je voulais voire au plus vite si l'idée tiendrait ses promesses...


## 🤓 Les EAEs pour les geeks (nerds ?)

Très vite, la solution a émergé, très simple :

- Une [repo template](https://docs.github.com/en/enterprise-server@3.1/repositories/creating-and-managing-repositories/creating-a-template-repository) pour distribuer le modèle de repo (et donc la possibilité de créer des repos privées à partir de ce modèle)
- Des [markdowns](https://fr.wikipedia.org/wiki/Markdown) pour le contenu : un fichier par étape de l'EAE pour un versioning optimal
- [`pandoc`](https://pandoc.org/) toolchain pour builder une version confortable/imprimable en phase de travail (ePub, pdf, docx, html)
- [Makefile](https://www.gnu.org/software/make/manual/html_node/Introduction.html) pour builder
- Processus classique de gestion de code autour de `git`, [discussions](https://resources.github.com/devops/process/planning/discussions/), [issues et planning](https://github.com/features/issues), [PRs](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests),...

## 🤯 Assistance IA

Dès lors que le contenu est disponible en fichiers structurés et interopérables, on bénéficie entre autre de toutes les fonctionnalités de nos IDEs... et donc... des opportunités de bénéficier de services d'Intelligence artificielle tels que : 

- [🤑 GitHub Copilot](https://github.com/features/copilot)
- [🤗 `llm-vscode`](https://marketplace.visualstudio.com/items?itemName=HuggingFace.huggingface-vscode) pour se plugger sur les APIs de HuggingFace
- [🦙 100% en local avec `ollama`](https://blog.codegpt.co/create-your-own-and-custom-copilot-in-vscode-with-ollama-and-codegpt-736277a60298)


## ⚡ Blitz demo 

Au final, pour déployer _from scratch _ et être prêt, c'est [aussi simple que cela](https://github.com/opt-nc/template-eae#-speedrun-script) depuis le terminal : 

```shell
brew install pandoc
pip install gitchangelog
gh repo create my-eae --description "Repo de mon EAE" \
    --private --template opt-nc/template-eae
gh repo clone my-eae && cd my-eae
make help
make epub
```

Et à ce stade, la première version ePub est buildée :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9gio8usnkw1cgu1cl0l7.png)

## 🔖 Enrichir avec des raccourcis

J'en ai alors profité pour enrichir avec des contenus tels que les [raccourcis vers des ressources utiles](https://github.com/opt-nc/template-eae/blob/main/ressources.md), très utiles lors de la campagne des EAEs 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/iffuljst6rro6wl70205.png)

## 📜 Enrichir avec l'historique `git`

Assez naturellement est arrivée l'envie d'avoir la log détaillée de la repo git, directement au sein du document.

Grâce à `pandoc` et [`gitchangelog`](https://github.com/vaab/gitchangelog), j'ai pu ajouter la log :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/28nxes6nelcc08hpbyoq.png)
 
## 📕 Pdf via `LaTeX`

Egalement disponible mais finalement moins pratique : l'export pdf... via LaTeX :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ck7ypgf8t6zdkzd2n6oe.png)

## 🪶 Des fichiers très légers

Pour partager efficacement autour de documents (par exemple sur le cloud), disposer de fichiers très légers est également un atout... et de ce côté-là, les résultats sont plutôt **très satisfaisants** :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/21sf6vhi1f2q68x3dvlo.png)
 
 
## 📓 ePub et eBook sur liseuse

Dans la foulée j'ai pu commencer à 

> consulter mon EAE sur ma liseuse pour faire la revue plus confortablement... **et sans imprimer**.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0ojq90mg7byapx8zh6k8.jpg)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qjlnzvaasijsbgz9vtkz.png)

## 🪙 Bénéfices ✨


- **Historisation fine de toute modification** au commit ([signé](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)) près
- Un EAE finalisé implique un [tag](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/managing-commits/managing-tags) et une [release](https://docs.github.com/en/repositories/releasing-projects-on-github) avec des assets
- On peut suivre son EAE tout au long de sa carrière **même lorsque l'on change d'organisation**
- Visu sur le versioning
- Notifications sur les changements possibles ([Teams](https://teams.github.com/), [Slack](https://slack.github.com/)) via des applications ou [webhooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks) ou encore [IFTTT](https://ifttt.com/github), [Zapier](https://zapier.com/apps/github/integrations),...
- Production de métriques
- **Facilité de saisie et d'accès** tout au long de l'année
- Production de documents de travail portables (`ePub ` pour liseuse), `pdf` via `LaTeX`
- Pas de timeouts lors de la conception/revue des objectifs
- Outil de sasie optimal pour les codeurs (VS Code, IntelliJ, `vim`, `emacs`,...) puisque contenu `markdown` natif
- Possibilité pour le manager de merger les fichiers de plusieurs agents via des chaînes de traitement dédiées
- Possibilité de lier des tickets d'objectifs à des commits lors de la modificaiton de l'EAE, voire à utiliser des labels
- **Revue très confortable** grâce aux éditeurs Markdown
- **Accessiblité** : possiblité de zoomer sur le ePub notamment pour une **taille de fonte optimale**
- Apprendre à compiler des documents, des livres avec `pandoc`
- Possibilité de faire le travail de revue, **y compris avec les collaborateurs externes**
- Possiblité de **faire des drafts via des branches**
- Possiblité de **faire des propostions via des Pull Requests**
- Facilite le travail de préparation, en particulier en distanciel
- Possiblité d'éditer depuis un env confortable web responsive (eg. tablette) ou codespace
- Possibilité pour un manager d'aggréger un fichier donné entre plusieurs agents pour créer des contenus dédiés aux besoins matériels par exemple
- Exports `docx` permettant une collaboration ou une publication plus aisée d'offres d'emplois

## 🐙 Collaborer sur le contenu avec GitKraken

Durant le processus d'élaboration, il est également possible de mettre la dataviz au centre du processus, par exemple avec [GitKraken](https://www.gitkraken.com/) :

{% youtube RiAeNSFjjLc %}


## 📽️ Dataviz : revivre les échanges en live

[`gource`](https://gource.io) permet de voir l'historique
des changement de code via de belles animations.

Il est donc possible de

> se passer le film mettant en scène le processus collaboratif autour de l'EAE :

{% youtube NjUuAuBcoqs %}

## 🔍 Découverte d'outils et pratiques

Last but not least, des outils découverts lors de cette expérimentation :

- [`gh-changelog`](https://github.com/chelnak/gh-changelog) : une [GitHub CLI extension](https://docs.github.com/en/enterprise-server@3.3/github-cli/github-cli/using-github-cli-extensions) qui permet de générer et visualiser la releaseNote depuis le terminal
- [`gitchangelog`](https://github.com/vaab/gitchangelog) : _Use your commit log to make beautifull and configurable changelog file_
- [`mdless`](https://github.com/ttscoff/mdless) : _utility that provides a formatted and highlighted view of Markdown files in Terminal_
- [Optimiser la gestion de ses eBooks](https://www.makeuseof.com/tag/personal-cloud-ebook-library/)
- [Dernières fonctionnalités de Calibre](https://calibre-ebook.com/whats-new)
- [Publier sur BookFusion](https://www.bookfusion.com/)

## 🙏 Feedback

N'hésitez à donner vos feedbacks et partager vos idées de réalisations ou applications sur le projet :

{% github opt-nc/template-eae %}