---
comments: 9
id: 1052364
is_dev_challenge: false
published_at: '2022-04-12T20:09:49Z'
reactions: 7
reading_time_minutes: 2
tags:
- docker
- angular
- api
- devops
title: '🐋 DOMAINE.nc : the fun (docker) way... and screenshots contest 🎨'
url: https://dev.to/optnc/domainenc-the-fun-docker-way-and-screenshots-contest-17o8
---

## ❔ Intro

A few months ago, during COVID lockdown in New-Caledonia, we decided to build cohesion around a simple yet very efficient innovation project across two teams, challenging us about what we could achieve together within less than 3 days.

> _Our main concern was to show what can be achieved when we have public APIs... and what we could do with [Open Innovation](https://en.wikipedia.org/wiki/Open_innovation)._

## 🐋 Do it the Docker way

The we built and released this project relying on dedicated and public

- Back image : [optnc/domaine-nc-api](https://hub.docker.com/r/optnc/domaine-nc-api)
- Front-end image : [optnc/domaine-nc-front](https://hub.docker.com/r/optnc/domaine-nc-front)

## 💡 Our goals

- 🧪 Create a whole new `UX` on an existing web app
- 🧑‍🤝‍🧑 Collaborate accross two teams and experiment [Github issues](https://github.com/features/issues)
- 😛 Have fun
- 🧑‍🎓 Get knowledge on Github Actions and pure front image building
- 😎 Make something cool together we can enjoy and play with

Then we did this👇

## 🕹️ Run the demo

```shell
cat << EOF > docker-compose.yml
version: "3.7"
services:
  api:
    image: docker.io/optnc/domaine-nc-api:latest
    ports:
      - "8080:8080"
  front:
    links:
      - api
    image: docker.io/optnc/domaine-nc-front:stable
    environment:
      - DNS_BACKEND=api:8080
    ports:
      - "80:80"
EOF

# Run docker-compose
docker-compose up -d
```

Now you're ready to give it a try :

```
# Give it a try 🤩
firefox http://localhost/opt.nc
firefox http://localhost
```

## 🙏🏻 Acknowledgements

This post is dedicated to [Laurent Schaeffer](https://www.linkedin.com/in/laurent-schaeffer-b1174a173/) (aka. [lschaeffer313](https://github.com/lschaeffer313)) and [Michèle Barré](https://www.linkedin.com/in/michelebarre/) (aka. [@mbarre](https://github.com/mbarre)) who where the core developers.

Also I want to thank [Sabrina](https://www.linkedin.com/in/sabrinaverolle/) who did trust us and accepted to invest 3 days of dev of Laurent.

We really enjoyed a lot developing together and role playing.

Now, I'm happy to welcome [Daniel Santos](https://www.linkedin.com/in/daniel-santos-dev-fullstack/) (aka. [@Dougniel](https://github.com/Dougniel)) on the team as front-end and DEVOPS, and of course Michèle as back-end active maintainer.

## 📷 Drop your screenshots 🎁

If you enjoyed this approach, drop a screenshot of your favorite  `.nc` domain in New-Caledonia in the discussion 👇