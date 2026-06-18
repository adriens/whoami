---
type: Project
title: Catalogue d'APIs publiques OPT-NC — Vitrine & produit d'appel
description: Conception et pilotage d'un catalogue d'APIs publiques gratuites exposées
  sur le portail APIGEE de l'OPT-NC (https://apigee-optnc-prd-api.apigee.io/). Toutes
  e…
resource: https://apigee-optnc-prd-api.apigee.io/
tags:
- interoperability
- architecture
- devrel
- api-fication
- team-lead
- pacifique
- nouvelle-caledonie
timestamp: 2021-01
---

Conception et pilotage d'un catalogue d'APIs publiques gratuites exposées sur le portail APIGEE de l'OPT-NC (https://apigee-optnc-prd-api.apigee.io/). Toutes en lecture seule. Sources hétérogènes selon l'API : données statiques gérées en interne, scraping de sites sans API officielle, ou croisement avec de l'open data (data.gouv.nc). Stratégie vitrine : prouver la valeur de l'interopérabilité, attirer développeurs et entreprises, créer l'appétit pour des APIs supplémentaires ou sur-mesure. Rôle : Product Owner & architecte — l'équipe GLIA développe.
- Localisation des boîtes postales : géolocalisation de toutes les BP en NC — a donné lieu à une réutilisation applicative par la communauté
- Suivi de colis : API de tracking OPT-NC exposée publiquement — genèse de l'écosystème colisnc (SDK Java, webapp, AR, Discord, mobile Flutter)
- Noms de domaine .NC : scraping du site domaine.nc → première et unique API publique sur les domaines .NC — app mobile Flutter tierce (25 releases, Google Play Store)
- Pharmacies de garde : scraping → API exposant les pharmacies d'astreinte en NC — information critique pour les usagers en dehors des heures ouvrées
- Validateur de numéro de téléphone : validation des numéros NC (format, opérateur) — donnée interne OPT-NC
- RIDET : API sur le registre des entreprises actives en NC — données data.gouv.nc, 2 articles DEV.to
- Référentiel des agences : localisation et informations de toutes les agences OPT-NC
- Transitaires : API listant les transitaires habilités à gérer les taxes de colis de fret en NC — usage professionnel direct

*Type : professional*

**Tags :** [api-fication](../tags/api-fication.md), [architecture](../tags/architecture.md), [devrel](../tags/devrel.md), [interoperability](../tags/interoperability.md), [nouvelle-caledonie](../tags/nouvelle-caledonie.md), [pacifique](../tags/pacifique.md), [team-lead](../tags/team-lead.md)
