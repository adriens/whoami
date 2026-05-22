---
comments: 0
id: 495330
is_dev_challenge: false
published_at: '2020-10-23T00:04:36Z'
reactions: 0
reading_time_minutes: 1
tags:
- docker
- kubernetes
title: Waiting time API at OPT.nc
url: https://dev.to/adriens/waiting-time-api-at-opt-nc-pfm
---

# Context

Just using this post to share the API usage with collaborators. This shows how to locally deploy and use the API to get waiting times in agencies.

# Run it!

To be up and running, just:

```shell
docker pull rastadidi/opt-temps-attente-agences-api:latest
docker images
docker run -d -p 8081:8081 rastadidi/opt-temps-attente-agences-api:latest
docker ps

# Pour essayer l'API
sudo apt-get install httpie jq -y
http http://127.0.0.1:8081/temps-attente/agence/4161
http http://127.0.0.1:8081/temps-attente/agence/4161 | jq '.idAgence'
```

# Resources

- [Source code repository](https://github.com/adriens/opt-temps-attente-agences-api)
- [Image on DockerHub](https://hub.docker.com/r/rastadidi/opt-temps-attente-agences-api)