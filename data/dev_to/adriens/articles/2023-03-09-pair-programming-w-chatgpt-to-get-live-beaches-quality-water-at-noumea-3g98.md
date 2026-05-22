---
comments: 2
id: 1371039
is_dev_challenge: false
published_at: '2023-03-09T20:43:46Z'
reactions: 1
reading_time_minutes: 2
tags:
- gratitude
title: 🤖 Pair-programming w. ChatGPT to get live Beaches quality Water at Nouméa🏖️
url: https://dev.to/adriens/pair-programming-w-chatgpt-to-get-live-beaches-quality-water-at-noumea-3g98
---

## ❔ About

I wanted to go to the beach at [Nouméa, New Caledonia](https://fr.wikipedia.org/wiki/Noum%C3%A9a). ... and wanted to know:

🗺️ Where are the beaches
🧫 Their water quality

💡 So I asked myself if...

> [`ChatGPT`](https://openai.com/blog/chatgpt/) could help with doing that with a Python script for automation tasks.

{% youtube 9MG3p9J4flk %}


## 🎤 What you'll learn

👉 In this **short post** you'll discover how I could co-author a script with `ChatGPT` from scratch 🙀. 

## 🍿 Demo time (`< 7'`)

{% youtube M6awjGe7sMk %}

## 🐍 Original Source code

```python
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# Make a GET request to the webpage
url = 'https://www.noumea.nc/noumea-pratique/salubrite-publique/qualite-eaux-baignade'
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table element containing the beach data by class name
beach_table = soup.find('table', class_='table')

# Extract the beach names and flag colors from the table
beach_data = []
for row in beach_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    beach_name = columns[0].get_text().strip()
    flag_color = columns[1].find('img')['alt']
    beach_data.append((beach_name, flag_color))

# Print the beach data
for beach in beach_data:
    print(beach[0] + ': ' + beach[1])
```

## 🍿 Opportunties

As I showed this work to my girlfriend, she asked : 

> _"You got the beaches status in text... now what ? Why is it cool ?"_

To answer the question, I told here that it makes it possible to contribute to build Smartcities, to create _"programs for robots"_ (eg. `API`) can help making cool things like [`@BotCagou`
](https://twitter.com/BotCagou):

{% twitter 1111161336996814848 %}

Below are some works I did thanks to API on this topic : a twiiter BOT : 

{% youtube 6WqrF-Zf_yc%}

{% youtube uOH1cjQVtIQ %}

## 📑 Resources

Below a collection of innovations I did thanks to the API I built once a while:

{% embed https://www.linkedin.com/pulse/open-data-public-apis-founding-together-collaborative-adrien-sales/ %}

{% embed https://www.linkedin.com/pulse/air-eau-la-convergence-des-%C3%A9l%C3%A9ments-via-les-%C3%A0-lanse-vata-adrien-sales/ %}

{% embed https://www.linkedin.com/pulse/building-smartcities-how-i-started-from-scratch-website-adrien-sales/ %}

{% embed https://www.linkedin.com/pulse/let-twitter-bots-tell-you-when-can-go-swim-adrien-sales/ %}

{% embed https://www.linkedin.com/pulse/geekbeach-get-water-quality-straight-outta-svg-badges-adrien-sales/ %}