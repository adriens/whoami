---
comments: 0
id: 421158
is_dev_challenge: false
published_at: '2020-08-07T22:15:10Z'
reactions: 1
reading_time_minutes: 1
tags:
- docker
- vagrant
- cowsay
- rest
title: Kalolo API from scratch with Docker (inside hashicorp/bionic64)
url: https://dev.to/adriens/kalolo-api-from-scratch-with-docker-inside-hashicorp-bionic64-1959
---

See [linkedIn article](https://www.linkedin.com/posts/adrien-sales_unix-linux-culture-activity-6697629162578042880-P4X1) for more details.

```shell
mkdir kalolo-box
cd kalolo-box
vagrant init hashicorp/bionic64
vagrant up
vagrant ssh
clear

sudo apt-get update
sudo apt-get remove docker docker-engine docker.io
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
docker --version

# run the kalolo-api locally
sudo docker pull rastadidi/kalolo-api:latest
sudo docker images
sudo docker run -d -p 8080:8080 rastadidi/kalolo-api:latest
sudo docker ps

 
sudo apt-get install jq boxes toilet cowsay fortune -y


echo "We are ready" | boxes -d dog

alias kalolo='clear && echo $(curl -sS http://localhost:8080/expressions/tag/bonjour/random | jq -r '.texte') | boxes -d boy | toilet --gay -f term'
kalolo
```