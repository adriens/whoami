---
comments: 12
id: 1470573
is_dev_challenge: false
published_at: '2023-05-24T21:37:33Z'
reactions: 0
reading_time_minutes: 2
tags:
- python
- datascience
- showdev
- automation
title: 🐼 Restaurant menu, as data 😋
url: https://dev.to/adriens/restaurant-menu-as-data-1gpn
---

## ❔ About

At Nouméa, I have a kind of "fétiche" restaurant called [_"Au p'tit café"_](http://auptitcafe.nc/)

They :

- 👐 Are **very kind people** : I love spend time there (at least once a week)
- 🧑‍🍳 Have awesome **creative and tasty menus**
- Have a unique management approach and have implemented a **`4.5` days work week**:

{% embed https://www.dnc.nc/au-ptit-cafe-une-semaine-de-quatre-jours-et-demi/ %}

{% twitter 1658658716298903552 %}

What is very convenient is that their website  describes very well its menus for the week, with a core philosophy:

- 🤏 **Few** menus
- ☝️ Focused on **high quality** and fresh food

I do often go and read their website:

{% embed http://auptitcafe.nc/menu/ %}

## 🤔 Inception

... and was wondering if I could build something "nerdy" around it...(for example play with it from my terminal 🤓)

## 💡 The idea

As I did never create a Python package, I finally decided to : 

1. **Create & release a dedicated [`poetry`](https://python-poetry.org/) package** that would get the menus data... so anyone could have fun with it (with a very few set of lines of code)
2. Get the **menu's datas** as [`pandas`](https://pandas.pydata.org/) dataframe... and `csv`

## 💭 Why Python ?

As Python is very widely used to create many things like:

- 🦜 Create [`langchain`](https://github.com/hwchase17/langchain) tools to build applications with `LLMs` through composability so _**we could chat with menus**_ ... for example with the [CSV Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html#csv-agent)
- 🤪 Any other **crazy and fun stuff (with GPU)** on [Kaggle](https://www.kaggle.com/adriensales) or [Google Colab'](https://research.google.com/colaboratory/faq.html)
- ⚡ Learn to create API with [`FastAPI`](https://fastapi.tiangolo.com/lo/) on top of this SDK
- 🤗 Play with [Hugging Face Transformers Agent](https://huggingface.co/docs/transformers/main/transformers_agents#transformers-agent)

## 🤓 Do it

I finally created the package : 

{% embed https://github.com/adriens/auptitcafe-sdk %}

... then released it on `pypi`:

{% embed https://pypi.org/project/auptitcafe/ %}

Finally, it became as easy as follows to get menus as data:

```python
# Install the package
!pip install auptitcafe

# Make some imports
from auptitcafe.menus import Menus
import pandas as pd

# Create the main utility instance
menu_instance = Menus()

# Dump menus as a csv file
menus = 'menus.csv'
menu_instance.to_csv(menus)

# Load menus in a pandas dataframe
df = pd.read_csv(menus)
# Diplay dataframe
df
# Be creative with dataframe 
```

## 🕹️ Enjoy the data on Kaggle

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0g9b76a4do31fsycqax7.png)](https://www.kaggle.com/code/adriensales/au-p-tit-caf-pypi-package-intro/notebook)

## 🍿 Demo

{% youtube Fy4o0Sfq7eg %}

## 📑 Resources

- [`adriens/auptitcafe-sdk`](https://github.com/adriens/auptitcafe-sdk)
- [`auptitcafe` on `pypi`](https://pypi.org/project/auptitcafe/)
- ["Au p'tit café" website](http://auptitcafe.nc/menu/)
- [Package demo on Kaggle](https://www.kaggle.com/code/adriensales/au-p-tit-caf-pypi-package?)
- ["Au p'tit café" on Tripadvisor](https://www.tripadvisor.fr/Restaurant_Review-g294130-d1952994-Reviews-Au_P_tit_Cafe-Noumea_Grand_Terre.html)