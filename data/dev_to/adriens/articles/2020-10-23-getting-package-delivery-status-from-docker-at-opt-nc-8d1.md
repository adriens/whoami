---
comments: 0
id: 495561
is_dev_challenge: false
published_at: '2020-10-23T09:19:57Z'
reactions: 6
reading_time_minutes: 2
tags:
- docker
- kubernetes
- vagrant
title: Getting package delivery status from docker at opt.nc
url: https://dev.to/adriens/getting-package-delivery-status-from-docker-at-opt-nc-8d1
---

# Context

Being able to get package delivery status is possible, and there is a dedicated Docker image fo this. This post explain how to do this within a very few lines of code so you can integrate that into your ERP, develop mobile app or simply develop any integration.

# Code snippet

```
sudo docker run --net=host -d -p 8080:8080 rastadidi/colisnc-api:latest
sudo apt-get install httpie jq boxes toilet
http http://localhost:8080/colis/CA107308006SI/latest
http http://localhost:8080/colis/CA107308006SI

# Shell: now the fun part
cat << EOF > colis.sh
#!/bin/bash          
curl -sS http://localhost:8080/colis/\$1/latest | jq -r '.status' | boxes -d boy | toilet --gay -f term
EOF

chmod u+x colis.sh
./colis.sh CA107308006SI
cowsay -f tux That\'s all folks
```

# Outputs

Finally json output for the latest known status of the delivery process:

```json
{
    "country": {
        "code": "NC",
        "iso": "NCL",
        "name": "nouvelle-caledonie"
    },
    "date": "2019-09-09T09:41:13",
    "informations": "",
    "itemId": "CA107308006SI",
    "localisation": "NOUMEA CDC",
    "localization": {
        "longName": "Office des Postes - Agence Principale",
        "name": "NOUMEA CDC",
        "url": "https://goo.gl/maps/verSQbb6tQaqzKq87"
    },
    "pays": "NOUVELLE-CALÉDONIE",
    "rawDateHeure": "09/09/2019 09:41:13",
    "status": "COLIS_LIVRE",
    "typeEvenement": "Votre courrier/colis a été livré"
}
```

# Resources

- [Original Web Front-end I scrap to get the core data](http://webtrack.opt.nc/ipswebtracking/)
- [Refactored website, relying on the API and other APIs with Google authentication and Maps](https://colisnc.redstone.nc)
- [Mobile app demo (with native cloud services like IFTTT, messenger, ...)](https://youtu.be/zlqzmUYxasM)
- [Mobile app on Google Play Store](https://play.google.com/store/apps/details?id=com.adriens.github.mescolisnc)
- [Augmented Reality (AR) experiment that relies on the API](https://youtu.be/BrZoOfFZS9w) 
- [API on RapidAPI Marketplace](https://rapidapi.com/adriens/api/colis-nc)
- [KataCoda Scenario showing how to deploy the API on Kubernetes Cluster](https://www.katacoda.com/rastadidi/scenarios/k8s)

# Full demo

Find below the full video demo, from scratch, with system install thanks to Vagrant: 
{% youtube J57Qhkg8S28 %}