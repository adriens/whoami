---
name: auptitcafe-sdk
url: https://github.com/adriens/auptitcafe-sdk
description: "😋 SDK Python pour accéder aux menus du restaurant \"Au p'tit café\" - Nouméa, Nouvelle-Calédonie"
language: Python
topics: [datascience, opendata-api, pypi-package, python, restaurant-menu, noumea, nouvelle-caledonie, menu]
stars: 1
created_at: 2023-05-07
updated_at: 2025-12-13
archived: false
has_readme: true
---

![PyPI - Implementation](https://img.shields.io/pypi/implementation/auptitcafe)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/auptitcafe)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/auptitcafe)
![PyPI - Format](https://img.shields.io/pypi/format/auptitcafe)
![PyPI](https://img.shields.io/pypi/v/auptitcafe)

# ❔ About

> Finally a Python package to make **getting Au p'it café's menus a piece of (cheese) cake.😅**

With this [package](https://pypi.org/project/auptitcafe/) you can:

- ✔️ Get [menus](http://auptitcafe.nc/menu/)
- ✔️ Get [takeways](http://auptitcafe.nc/a-emporter/)

... and get them as list of objects or `csv`.

👉 See it live on [Kaggle](https://www.kaggle.com/adriensales/au-p-tit-caf-pypi-package-intro) 👈


# 🔖 Social networks

- [Official website](http://auptitcafe.nc/)
- [TripAdvisor](https://www.tripadvisor.com/Restaurant_Review-g294130-d1952994-Reviews-Au_P_tit_Cafe-Noumea_Grand_Terre.html)
- [Instagram](https://www.instagram.com/auptitcafe.nc/?hl=en) 
- [Facebook](https://www.facebook.com/auptitcafe.nc/)
- [Google Maps](https://goo.gl/maps/4UcxegSnxMsE8qKs8)

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/iRSInif_Zwc/0.jpg)](https://www.youtube.com/watch?v=iRSInif_Zwc)

# 🤓 Nerd resources

- [🐍 `pypi`](https://pypi.org/project/auptitcafe/)
- [😋 Au p'tit café (pypi package intro on Kaggle) 🚀](https://www.kaggle.com/adriensales/au-p-tit-caf-pypi-package-intro)

# 🚀 Quickstart

For the impatients, here is a quick and ready to use code snippet:

```python
# Install the package
!pip install auptitcafe --upgrade

# Make some imports
from auptitcafe.menus import Menus
import pandas as pd

# Create the main utility instance
menu_instance = Menus()

# Dump menus as a csv file
menus = 'menus.csv'
menu_instance.to_csv(menus)

# Load menus in a panda dataframe
df = pd.read_csv(menus)
# Diplay dataframe
df
```

# Build it

```shell
poetry show --tree
```

```shell
poetry build
poetry install
```

## test

```shell
poetry run pytest
```
## Publish

```shell
poetry config pypi-token.pypi $PYPI_TOKEN
poetry publish
```