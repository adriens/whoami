---
name: emploi-nc-app
url: https://github.com/adriens/emploi-nc-app
description: "Application mobile Emploi.nc"
language: Dart
topics: []
stars: 0
created_at: 2020-03-17
updated_at: 2025-09-25
archived: true
has_readme: true
---

# emploi-nc-app

## Description

Application mobile Emploi.nc disponible sur le [Play Store](https://play.google.com/store/apps/details?id=com.github.adriens.nc.emploi&hl=fr).

Nom de l'application: `Offres Emplois Calédonie`

## Utilisation

Création d'une classe app_config.dart pour configurer la clès de l'api :

```dart
const apiKey = "Votre clef";

class AppConfig {
}
```

## Publication

Compilation avec la version du SDK Flutter : [`Flutter (Channel stable, 1.20.2)`](https://flutter.dev/docs/get-started/install)

1. Être en possession du fichier `.jks`

2. Suivre les instructions à partir de l'étape [Reference the keystore from the app](https://flutter.dev/docs/deployment/android#reference-the-keystore-from-the-app)


```shell
flutter pub get
flutter build apk
flutter build appbundle
```

3. Transmettre le fichier présent dans le répertoire `{ project folder }\build\app\outputs\bundle\release\*.aab`