---
name: Nodred-Modbus
url: https://github.com/adriens/Nodred-Modbus
description: "Serveur nodered modbus KNX"
language: Python
topics: []
stars: 0
created_at: 2025-08-04
updated_at: 2025-08-04
archived: false
has_readme: true
---

# 🔌 Supervision KNX + Modbus — Dockerisé avec Node-RED

Ce projet contient tout le nécessaire pour déployer une solution de supervision énergétique via **Node-RED**, **Modbus TCP**, et **KNX IP**, avec un serveur Modbus Python intégré.

Développé pour un déploiement simple dans une VM Dockerisée.

---

## 📁 Contenu du dépôt

| Fichier               | Description                                               |
|----------------------|-----------------------------------------------------------|
| `Dockerfile`         | Image Docker complète (Node.js, Node-RED, Python, etc.)   |
| `start.sh`           | Script de démarrage des services                          |
| `modbus_server.py`   | Serveur Modbus TCP en Python (pymodbus)                   |
| `requirements.txt`   | Dépendances Python requises                               |
| `flows.json`         | Flows Node-RED préconfigurés (KNX + Modbus)               |
| `README.md`          | Documentation d’installation                              |
| *(optionnel)* `docker-compose.yml` | Pour lancer via Docker Compose             |

---

## 🧰 Prérequis

- Docker installé : https://docs.docker.com/get-docker/
- Connexion réseau vers les équipements suivants :
  - Passerelle KNX (port 3671 UDP)
  - Passerelle climatisation GREE (Modbus TCP, port 502)
  - Superviseur TOPKAPI (Modbus TCP, port 1502)

---

## 🚀 Installation manuelle (via Docker CLI)

1. Cloner ce dépôt :

```bash
git clone https://github.com/SEMEP-NC/Nodred-Modbus.git
cd Nodred-Modbus