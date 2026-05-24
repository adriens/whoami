---
name: optnc-fiber-eligibility
url: https://github.com/adriens/optnc-fiber-eligibility
description: "Un scrapper Go en API  pour tester votre éligibilité à la Fibre Optique en Nouvelle-Calédonie"
language: Go
topics: [api, api-rest, fibre-optic, golang, nouvelle-caledonie]
stars: 0
created_at: 2025-12-13
updated_at: 2025-12-16
archived: false
has_readme: true
---

# OPT-NC Fiber Eligibility Checker


![Go](https://img.shields.io/badge/Go-1.21-00ADD8?style=flat&logo=go)
[![Docker](https://img.shields.io/docker/v/rastadidi/optnc-fiber-eligibility?style=flat&logo=docker&label=Docker%20Hub)](https://hub.docker.com/repository/docker/rastadidi/optnc-fiber-eligibility/)
[![Docker Image Size](https://img.shields.io/docker/image-size/rastadidi/optnc-fiber-eligibility?style=flat&logo=docker)](https://hub.docker.com/repository/docker/rastadidi/optnc-fiber-eligibility/)
![Swagger](https://img.shields.io/badge/Swagger-OpenAPI_3.0-85EA2D?style=flat&logo=swagger)
[![Alpine](https://img.shields.io/badge/Alpine-3.19-0D597F?style=flat&logo=alpine-linux)](https://alpinelinux.org/)
![API](https://img.shields.io/badge/API-REST-blue?style=flat)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](./LICENSE)

<img width="1032" height="885" alt="Screenshot_20251214_101303" src="https://github.com/user-attachments/assets/1bf5efed-554a-412d-8b97-716ca680c767" />


**🚀 API REST de vérification d'éligibilité à la fibre optique OPT Nouvelle-Calédonie**

📚 **[Documentation Swagger Interactive](http://localhost:8080/swagger/)** | 🐳 **[Docker Hub](https://hub.docker.com/r/rastadidi/optnc-fiber-eligibility)** | 🔧 **Taskfile**

Service de vérification d'éligibilité à la fibre optique OPT Nouvelle-Calédonie.

## 📁 Structure du projet

```
opt-nc-eligibilite/
├── cmd/
│   └── api/
│       └── main.go              # Point d'entrée de l'application
├── internal/
│   ├── api/
│   │   ├── handlers.go          # Handlers HTTP REST
│   │   └── middleware.go        # Middleware (Logger, CORS)
│   ├── models/
│   │   └── eligibility.go       # Structures de données
│   └── scraper/
│       ├── scraper.go           # Logique de scraping
│       └── parser.go            # Parsing HTML
├── pkg/
│   └── validator/
│       └── phone.go             # Validation numéros téléphone
├── Dockerfile                   # Image conteneur Alpine
├── docker-compose.yml           # Configuration Podman Compose
├── go.mod                       # Dépendances Go
└── README.md
```

## 🚀 Utilisation

**📚 Documentation API interactive :** http://localhost:8080/swagger/

### Mode CLI

```bash
# Sans conteneur
go run ./cmd/api 257364
go run ./cmd/api "25.73.64" --json

# Avec Podman
podman run --rm optnc-fiber-eligibility 257364
podman run --rm optnc-fiber-eligibility "25.73.64" --json
```

### Mode API

```bash
# Sans conteneur
go run ./cmd/api api 8080

# Avec Podman
podman run -p 8080:8080 optnc-fiber-eligibility
```

## 🐳 Podman / Docker

**🚀 Image disponible sur Docker Hub :** [rastadidi/optnc-fiber-eligibility](https://hub.docker.com/r/rastadidi/optnc-fiber-eligibility)

### Utiliser l'image Docker Hub (recommandé)

```bash
# Avec Podman (nécessite --network=host pour le scraping)
podman pull rastadidi/optnc-fiber-eligibility:latest
podman run -d --network=host --name opt-api rastadidi/optnc-fiber-eligibility
```

**⚠️ Important :** L'option `--network=host` est requise pour permettre à Chromium d'accéder au site OPT-NC.

### Build local

```bash
podman build -t optnc-fiber-eligibility .
```

### Run API

```bash
podman run -d -p 8080:8080 --name opt-eligibility-api optnc-fiber-eligibility
```

### Run CLI

```bash
podman run --rm optnc-fiber-eligibility 257364
podman run --rm optnc-fiber-eligibility "25.73.64" --json
```

### Avec podman-compose

```bash
podman-compose up -d
podman-compose down
```

## 📡 API Endpoints

**📚 Documentation interactive :** [Swagger UI](http://localhost:8080/swagger/) - Tester l'API depuis le navigateur

### Health Check
```bash
GET /health

curl http://localhost:8080/health
```

### Swagger UI (Documentation interactive)
```bash
# Ouvrir dans le navigateur
http://localhost:8080/swagger/

# Télécharger la spec OpenAPI
curl http://localhost:8080/swagger/doc.json
```

### Check Eligibility
```bash
# GET
GET /api/v1/eligibility?phone=257364

curl "http://localhost:8080/api/v1/eligibility?phone=257364"

# POST
POST /api/v1/eligibility
Content-Type: application/json
{
  "phone_number": "25.73.64"
}

curl -X POST http://localhost:8080/api/v1/eligibility \
  -H "Content-Type: application/json" \
  -d '{"phone_number":"25.73.64"}'
```

## 🎯 Exemple simple et complet

### Vérification d'éligibilité en une commande

```bash
# Commande complète avec HTTPie et jq
http --body GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber'
```

**Sortie :**
```json
{
  "status": "non-eligible",
  "available": false,
  "message": "Votre ligne n'est pas encore éligible à la fibre optique. La fibre n'est pas encore disponible à votre adresse."
}
```

### Mode verbose (voir requête + réponse HTTP complètes)

```bash
http -v GET :8080/api/v1/eligibility phone==257364
```

**Affiche :**
- ✅ Requête HTTP complète (headers, méthode, URL)
- ✅ Réponse HTTP complète (status code, headers)
- ✅ Corps de la réponse JSON formaté

### One-liner pour vérification rapide

```bash
# Format compact lisible
http --body GET :8080/api/v1/eligibility phone==257364 | \
  jq -r '"\(.data.phone_number) -> Fibre: \(.data.fiber.status) (disponible: \(.data.fiber.available))"'
```

**Sortie :**
```
257364 -> Fibre: non-eligible (disponible: false)
```

### Vérifier uniquement la disponibilité

```bash
# Retourne true ou false
http --body GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber.available'
```

**Sortie :**
```
false
```

---

## 🔥 Exemples avec HTTPie

[HTTPie](https://httpie.io/) est un client HTTP moderne et intuitif.

### Installation
```bash
# Ubuntu/Debian
sudo apt install httpie

# macOS
brew install httpie

# Fedora
sudo dnf install httpie
```

### Health Check (200 OK)
```bash
# Affiche headers + body (montre le code HTTP)
http GET :8080/health

# Uniquement les headers
http --print=h GET :8080/health
```

### Vérifier l'éligibilité (GET) - 200 OK
```bash
# Format standard (affiche HTTP/1.1 200 OK)
http GET :8080/api/v1/eligibility phone==257364

# Avec un numéro formaté
http GET :8080/api/v1/eligibility phone=="25.73.64"

# Mode verbose (voir requête + réponse complète)
http -v GET :8080/api/v1/eligibility phone==257364
```

### Vérifier l'éligibilité (POST) - 200 OK
```bash
# Format JSON
http POST :8080/api/v1/eligibility phone_number=257364

# Avec un numéro formaté
http POST :8080/api/v1/eligibility phone_number="25.73.64"
```

### Gestion des erreurs

**Paramètre manquant (400 Bad Request):**
```bash
http GET :8080/api/v1/eligibility
```

**Numéro invalide - trop court (400 Bad Request):**
```bash
http GET :8080/api/v1/eligibility phone==12345
```

**Numéro invalide - avec lettres (400 Bad Request):**
```bash
http GET :8080/api/v1/eligibility phone==ABC123
```

**Numéro introuvable (404 Not Found):**
```bash
http GET :8080/api/v1/eligibility phone==286320
```

**Réponse 404:**
```json
{
    "error": "not_found",
    "message": "Numéro introuvable. Contactez le 1000 si vous pensez qu'il s'agit d'une erreur."
}
```

### Options d'affichage HTTPie
```bash
# Afficher uniquement les headers (avec code HTTP)
http --print=h GET :8080/health

# Afficher uniquement le body
http --print=b GET :8080/api/v1/eligibility phone==257364

# Afficher headers + body (défaut, montre le code HTTP)
http --print=hb GET :8080/api/v1/eligibility phone==257364

# Mode verbose (requête + réponse complète)
http -v GET :8080/api/v1/eligibility phone==257364

# Tout afficher (H=req headers, B=req body, h=resp headers, b=resp body)
http --print=HhBb POST :8080/api/v1/eligibility phone_number=257364

# Sauvegarder la réponse dans un fichier
http GET :8080/api/v1/eligibility phone==257364 > result.json
```

### Codes HTTP de l'API

| Code HTTP | Description | Cas d'usage |
|-----------|-------------|-------------|
| `200 OK` | Succès | Numéro trouvé et vérifié (éligible ou non) |
| `400 Bad Request` | Erreur client | Paramètre manquant ou validation échouée |
| `404 Not Found` | Ressource introuvable | Numéro inexistant dans la base OPT |
| `405 Method Not Allowed` | Méthode invalide | Seuls GET et POST sont acceptés |
| `500 Internal Server Error` | Erreur serveur | Erreur interne de l'application |

### Tester plusieurs numéros
```bash
# Script bash pour tester plusieurs numéros
for phone in 257364 286320 "25.73.64"; do
  echo "Testing: $phone"
  http --body GET :8080/api/v1/eligibility phone==$phone | jq '.data.found, .data.fiber.status'
  echo "---"
done
```

## 🔧 Développement

```bash
# Installer les dépendances
go mod tidy

# Lancer en mode CLI
go run ./cmd/api 257364

# Lancer l'API
go run ./cmd/api api 8080

# Build
go build -o bin/opt-eligibility ./cmd/api
```

## 📄 Exemple de réponse JSON

```json
{
  "success": true,
  "data": {
    "phone_number": "257364",
    "checked_at": "2025-12-13T21:00:00Z",
    "found": true,
    "adsl": {
      "status": "non-eligible",
      "message": "L'offre souscrite sur votre ligne n'est pas compatible avec l'ADSL."
    },
    "fiber": {
      "status": "non-eligible",
      "available": false,
      "message": "Votre ligne n'est pas encore éligible à la fibre optique."
    },
    "contact_phone": "1016",
    "isp_providers": [
      {"name": "can'l", "url": "http://www.canl.nc/"},
      {"name": "InternetNC", "url": "http://www.internetnc.nc/"},
      {"name": "Lagoon", "url": "http://www.lagoon.nc/"},
      {"name": "MLS", "url": "http://www.mls.nc/"},
      {"name": "Nautile", "url": "http://www.nautile.nc/"}
    ]
  }
}
```

## 🛠️ Commandes Podman utiles

```bash
# Voir les images
podman images

# Voir les conteneurs en cours
podman ps

# Voir tous les conteneurs
podman ps -a

# Arrêter le conteneur
podman stop opt-eligibility-api

# Supprimer le conteneur
podman rm opt-eligibility-api

# Voir les logs
podman logs opt-eligibility-api

# Suivre les logs en temps réel
podman logs -f opt-eligibility-api
```

## 🏗️ Architecture

Le projet suit une architecture clean avec séparation des responsabilités :

- **`cmd/api`** : Point d'entrée de l'application (CLI et API)
- **`internal/api`** : Handlers HTTP et middleware (non exportable hors du projet)
- **`internal/models`** : Structures de données métier
- **`internal/scraper`** : Logique de scraping et parsing
- **`pkg/validator`** : Utilitaires réutilisables (validation)

Cette structure facilite :
- ✅ Les tests unitaires
- ✅ La maintenabilité
- ✅ L'évolution du code
- ✅ La réutilisation de composants

## 🎯 Taskfile - Automatisation

Le projet utilise [Task](https://taskfile.dev/) pour automatiser les tâches courantes.

### Installation de Task

```bash
# Linux/macOS avec Homebrew
brew install go-task/tap/go-task

# Ubuntu/Debian
sudo snap install task --classic

# Ou avec Go
go install github.com/go-task/task/v3/cmd/task@latest
```

### Tâches disponibles

```bash
# Voir toutes les tâches
task --list

# Build l'image (tâche par défaut)
task
# ou
task build

# Démarrer le conteneur API
task run

# Arrêter et supprimer le conteneur
task stop

# Redémarrer (stop + build + run)
task restart

# Voir les logs
task logs
task logs-follow

# Tester l'API
task test
task test-httpie

# Nettoyer tout
task clean

# Mode développement (local, sans conteneur)
task dev

# CLI local
task cli-local -- 257364
task cli-local -- "25.73.64" --json

# CLI dans le conteneur
task cli -- 257364

# Build binaire local
task build-binary

# Formater et vérifier le code
task fmt
task vet
task lint

# Podman Compose
task compose-up
task compose-down
task compose-logs

# Utilitaires
task ps        # Voir les conteneurs
task images    # Voir les images
task help      # Aide
```

### Exemples d'utilisation

```bash
# Workflow de développement
task                  # Build l'image
task run              # Démarre l'API
task test             # Teste les endpoints
task logs-follow      # Suit les logs

# Développement local (sans conteneur)
task dev              # Lance l'API en local
# Dans un autre terminal
task test             # Teste l'API

# CLI
task cli-local -- 257364              # Test local
task cli -- 257364                    # Test dans conteneur

# Nettoyage et rebuild
task clean            # Nettoie tout
task                  # Rebuild
task run              # Redémarre
```

### Variables d'environnement

Vous pouvez surcharger les variables :

```bash
# Changer le port
PORT=8082 task run

# Changer le nom de l'image
IMAGE_NAME=my-custom-name task build
```

## 🔍 Exemples avancés HTTPie + jq

### Extraire uniquement les informations Fibre

```bash
# Statut fibre uniquement
http GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber'

# Vérifier si la fibre est disponible
http GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber.available'

# Message d'éligibilité fibre
http GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber.message'

# Statut d'éligibilité fibre
http GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber.status'

# Combiner plusieurs informations
http GET :8080/api/v1/eligibility phone==257364 | jq '{
  numero: .data.phone_number,
  eligible_fibre: .data.fiber.available,
  statut: .data.fiber.status,
  message: .data.fiber.message
}'

# Format compact pour le statut fibre
http GET :8080/api/v1/eligibility phone==257364 | jq -r '
  "\(.data.phone_number): Fibre \(.data.fiber.status) (\(.data.fiber.available))"
'

# Tester plusieurs numéros et afficher que la fibre
for phone in 257364 286320; do
  echo "=== $phone ==="
  http --body GET :8080/api/v1/eligibility phone==$phone | jq '{
    numero: .data.phone_number,
    fibre_disponible: .data.fiber.available,
    statut: .data.fiber.status
  }'
done
```

### Exemples de sortie

**Informations complètes sur la fibre :**
```bash
$ http GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber'
```
```json
{
  "status": "non-eligible",
  "available": false,
  "message": "Votre ligne n'est pas encore éligible à la fibre optique. La fibre n'est pas encore disponible à votre adresse."
}
```

**Vérification rapide de disponibilité :**
```bash
$ http GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber.available'
false
```

**Format personnalisé :**
```bash
$ http GET :8080/api/v1/eligibility phone==257364 | jq -r '
  "\(.data.phone_number): Fibre \(.data.fiber.status) (\(.data.fiber.available))"
'
257364: Fibre non-eligible (false)
```

### Cas d'usage pratiques

**Script de vérification en masse :**
```bash
#!/bin/bash
# check_fiber.sh - Vérifier l'éligibilité fibre pour plusieurs numéros

echo "Numéro,Disponible,Statut,Contact" > fiber_check.csv

for phone in 257364 286320 254321; do
  result=$(http --body GET :8080/api/v1/eligibility phone==$phone 2>/dev/null)
  
  numero=$(echo "$result" | jq -r '.data.phone_number')
  disponible=$(echo "$result" | jq -r '.data.fiber.available')
  statut=$(echo "$result" | jq -r '.data.fiber.status')
  contact=$(echo "$result" | jq -r '.data.contact_phone')
  
  echo "$numero,$disponible,$statut,$contact" >> fiber_check.csv
done

cat fiber_check.csv
```

**Monitoring de l'API :**
```bash
# Vérifier que l'API répond et que la fibre est bien parsée
if http --check-status --timeout=5 GET :8080/health &>/dev/null; then
  result=$(http --body GET :8080/api/v1/eligibility phone==257364 | jq '.data.fiber')
  if [ ! -z "$result" ]; then
    echo "✅ API OK - Parsing fibre fonctionnel"
  else
    echo "❌ Erreur parsing fibre"
  fi
else
  echo "❌ API non disponible"
fi
```

### 📝 Script de vérification en masse

Un script `check_fiber.sh` est fourni pour vérifier plusieurs numéros :

```bash
# Vérifier les numéros par défaut
./check_fiber.sh

# Vérifier des numéros spécifiques
./check_fiber.sh 257364 286320 254321

# Changer l'URL de l'API
API_URL=http://localhost:8081 ./check_fiber.sh 257364

# Changer le fichier de sortie
OUTPUT_FILE=results.csv ./check_fiber.sh 257364 286320
```

**Exemple de sortie :**
```
🔍 Vérification d'éligibilité fibre OPT-NC
==========================================

📞 Numéros à vérifier: 257364 286320

Vérification 257364... ❌ Fibre non disponible (non-eligible)
Vérification 286320... ❌ Fibre non disponible (unknown)

📊 Résultats sauvegardés dans: fiber_check.csv

Numéro  Trouvé  Fibre Disponible  Statut        Contact
257364  true    false             non-eligible  1016
286320  true    false             unknown       N/A

✅ Vérification terminée
```

Le script génère un fichier CSV qui peut être importé dans Excel, Google Sheets, etc.

## 📋 Résumé des codes HTTP

L'API utilise les codes HTTP de manière sémantique :

```bash
# ✅ 200 OK - Numéro trouvé et vérifié
$ http --print=h GET :8080/api/v1/eligibility phone==257364 | grep HTTP
HTTP/1.1 200 OK

# ❌ 404 Not Found - Numéro introuvable dans la base OPT
$ http --print=h GET :8080/api/v1/eligibility phone==286320 | grep HTTP
HTTP/1.1 404 Not Found

# ❌ 400 Bad Request - Format de numéro invalide
$ http --print=h GET :8080/api/v1/eligibility phone==12345 | grep HTTP
HTTP/1.1 400 Bad Request
```

### Distinction importante

- **200 OK** : Le numéro existe dans la base OPT
  - ✅ Peut être éligible ou non-éligible à la fibre
  - ✅ Réponse valide avec toutes les informations
  
- **404 Not Found** : Le numéro n'existe pas dans la base OPT
  - ❌ Numéro inconnu ou erreur de saisie
  - ❌ Contacter le 1000 pour vérification

**Exemple de logique client :**
```bash
# Script bash avec gestion des codes HTTP
response=$(http --check-status GET :8080/api/v1/eligibility phone==257364 2>&1)

if [ $? -eq 0 ]; then
  echo "✅ Numéro trouvé, vérification éligibilité..."
  echo "$response" | jq '.data.fiber'
elif echo "$response" | grep -q "404"; then
  echo "❌ Numéro introuvable dans la base"
elif echo "$response" | grep -q "400"; then
  echo "⚠️  Format de numéro invalide"
fi
```

## 📚 Swagger / OpenAPI Documentation

L'API embarque **Swagger UI** pour une documentation interactive.

### Accéder à Swagger

```bash
# Démarrer l'API
task run

# Ouvrir dans le navigateur
http://localhost:8080/swagger/
```

Ou directement : **http://localhost:8080/swagger/**

### Fonctionnalités Swagger UI

- 📖 **Documentation complète** de tous les endpoints
- 🧪 **Test interactif** : Essayer l'API directement depuis le navigateur
- 📝 **Schémas** : Voir tous les modèles de données
- 🔍 **Exemples** : Requêtes et réponses d'exemple
- 📥 **Export** : Télécharger swagger.json ou swagger.yaml

### Régénérer la documentation

Si vous modifiez les annotations Swagger dans le code :

```bash
# Régénérer les docs
task swagger

# Ou manuellement
swag init -g cmd/api/main.go --output docs
```

### Fichiers générés

```
docs/
├── docs.go          # Documentation Go générée
├── swagger.json     # Spécification OpenAPI JSON
└── swagger.yaml     # Spécification OpenAPI YAML
```

### Annotations Swagger

La documentation est générée depuis les **annotations Go** dans le code :

```go
// @Summary Vérifier l'éligibilité à la fibre
// @Description Vérifie si un numéro est éligible
// @Tags eligibility
// @Param phone query string false "Numéro"
// @Success 200 {object} APISuccessResponse
// @Failure 404 {object} APIErrorResponse
// @Router /api/v1/eligibility [get]
func (s *Server) CheckEligibilityHandler(...)
```

### Exemple d'utilisation Swagger UI

1. Ouvrir http://localhost:8080/swagger/
2. Cliquer sur **GET /api/v1/eligibility**
3. Cliquer sur **Try it out**
4. Entrer un numéro (ex: 257364)
5. Cliquer sur **Execute**
6. Voir la réponse en temps réel

Swagger UI remplace avantageusement Postman pour tester l'API ! 🚀