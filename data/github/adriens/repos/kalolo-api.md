---
name: kalolo-api
url: https://github.com/adriens/kalolo-api
description: "API de gestion des expressions caldoches à nous les mecs du caillou"
language: Java
topics: []
stars: 0
created_at: 2020-06-15
updated_at: 2020-08-10
archived: false
has_readme: true
---

# Kalolo-api

API de gestion des expressions caldoches à nous les mecs du caillou.

# Consommer l'API

API dispo sur le [marketPlace Rapid API](https://rapidapi.com/adriens/api/kalolo)
ainsi que sur [DockerHub](https://hub.docker.com/r/rastadidi/kalolo-api)

# Démo et réalisations utilisant Kalolo-API

- [Article linkedIn](https://www.linkedin.com/pulse/eaas-expressions-service-nos-ont-une-api-sont-fin-barr%C3%A9s-adrien-sales)
- [Post de publication de l'article](https://www.linkedin.com/posts/adrien-sales_cagougeeks-noumea-nouvellecaledonie-activity-6694135449662971904-9biE)
- [MEME de Kalolo in the shell](https://www.linkedin.com/posts/adrien-sales_shell-unix-linux-activity-6697227023942868992-Z26_)
- [Article complet dédié à l'implémentation dans cowsay](https://www.linkedin.com/pulse/hacking-your-terminal-regional-slang-expressions-from-adrien-sales)
- [Dev.to Post for doing it the Docker way](https://dev.to/adriens/kalolo-api-from-scratch-with-docker-inside-hashicorp-bionic64-1959)


## Démarrer le service
`mvn spring-boot:run`

## Endpoints

```
/ : Documentation Swagger
```

```
/auteurs : La liste de tous les auteurs

/auteurs/random : Un auteur au hasard

/auteurs/auteur/{idAuteur} : L'auteur d'identifiant {idAuteur}

/auteurs/{cleAuteur} : L'auteur d'identifiant {cleAuteur}
```

```
/types : La liste de tous les types de média

/types/type/{idType} : Le type de média d'identifiant {idType}
```

```
/medias : La liste de tous les médias

/medias/media/{idMedia} : Le média d'identifiant {idMedia}

/medias/random : Un média au hasard

/medias/auteur/{cleAuteur} : La liste de tous les médias de l'auteur {cleAuteur}

/medias/auteur/{cleAuteur}/media/{idMedia} : Le média d'identifiant {idMedia} de l'auteur {cleAuteur}

/medias/auteur/{cleAuteur}/random : Un média au hasard de l'auteur {cleAuteur}
```

```
/tags : La liste de tous les tags

/tags/tag/{idTag} : Le tag d'identifiant {idTag}

/tags/{cleTag} : Le tag d'identifiant {cleTag}
```

```
/expressions : La liste de toutes les expressions

/expressions/expression/{idExpression} : L'expression d'identifiant {idExpression}

/expressions/random : Une expression au hasard

/expressions/keyword/{motscles} : La liste de toutes les expressions contenant au moins un mot-clé de {motscles}
(les mots-clés séparés par ",")

/expressions/keyword/{motscles}/random : Une expression au hasard contenant au moins un mot-clé de {motscles}
(les mots-clés séparés par ",")

/expressions/tag/{cleTag} : La liste de toutes les expressions ayant pour tag {cleTag}

/expressions/tag/{cleTag}/expression/{idExpression} : L'expression d'identifiant {idExpression} ayant pour tag {cleTag}

/expressions/tag/{cleTag}/random : Un expression au hasard ayant pour tag {cleTag}
```


## Exemples d'appels

```
/auteurs
/auteurs/random
/auteurs/auteur/3
/auteurs/ollivaud
```

```
/types`
/types/type/2
```

```
/medias
/medias/random
/medias/media/11
/medias/auteur/kingtaz
/medias/auteur/kingtaz/media/8
/medias/auteur/kingtaz/random
```

```
/tags
/tags/tag/3
/tags/bonjour
```

```
/expressions
/expressions/random
/expressions/expression/11
/expressions/keyword/{fin}
/expressions/keyword/{bien}/random
/expressions/keyword/{yossi,kalolo}
/expressions/keyword/{ben,ça}/random
/expressions/tag/joie
/expressions/tag/joie/expression/113
/expressions/tag/joie/random
```

# jib build

In your `~/.m2/settings.xml` put your Docker hub

```xml
<server>
    <id>registry.hub.docker.com</id>
    <username>rastadidi</username>
    <password>XXXXXXX</password>
</server>
```

Then build/push to DockerHub :

`mvn compile jib:build`

# Docker pull command

```
docker pull rastadidi/kalolo-api:latest
docker images
docker run -d -p 8080:8080 rastadidi/kalolo-api:latest
sudo apt-get install jq boxes toilet cowsay fortune -y
echo "We are ready" | boxes -d dog

alias kalolo='clear && echo $(curl -sS http://localhost:8080/expressions/tag/bonjour/random | jq -r '.texte') | boxes -d boy | toilet --gay -f term'
kalolo
```