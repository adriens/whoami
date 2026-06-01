---
comments: 8
id: 1115450
is_dev_challenge: false
published_at: '2022-06-30T09:27:33Z'
reactions: 4
reading_time_minutes: 2
tags:
- api
- javascript
- webdev
- showdev
title: 🎨 From waiting time metrics to Generative art
url: https://dev.to/optnc/from-waiting-time-metrics-to-generative-art-2d6d
---

## ❔ Context

Recenlty we have published an API dedicated to waiting time in our (Post)-offices.

👉 See previous episode of the series.


To put in evidence the potential of that API we created an original [`P5*js`](https://p5js.org/) based artwork datavizualization experience around that API.

In this post you'll discover what we could achieve... and if you like it to run it by yourself.

## 🎫 Core real world data display

In our agencies, here is how we display the data to customers :

{% youtube A1MLiBJON2Y %}

## ⌨️ Install artwork

The install process is really straight forward : 

First, clone the repo : 

```shell
git clone https://github.com/opt-nc/generative-art-temps-attente.git
cd generative-art-temps-attente
```

Then boot the solution : 

```shell
docker-compose up -d
docker-compose ps
```

That's it : you can now enjoy the datavisualization.

## 🎨 Enjoy artworks

Many kind of visualizations have been created. See below to discover them.

### 🌌 Orbit

First the default one.

Notice that rotation speed is based on the waiting time.

```
firefox http://localhost
```

### 🌌 Orbit light version

Then a lightest version of the previous one :

```
firefox http://localhost/orbit.min.html
```

### ⛹️ Jumpers

In this visualization each ball is a Post-Office, and the higher a ball is bouncing, the higher waiting queue are important.

```
firefox http://localhost/jumpers.html
```

### 🕳️ Gravity

Then this one where interactions are driven by gravity and speed.
Notice that each ball's mass is relying on the waiting time :

```
firefox http://localhost/gravity.html
```

### 🍿 Live demo

Below a live demo from scratch :

{% youtube 4vmKVhHkdhI %}

## 🙏 Acknowledgements

All that work would have not been possible without talents and highly engaged team members : 

- 👧 [Emilie Bossart](https://www.linkedin.com/in/meilie389/) : first API version
- 👨 [Guillaume Bertherat](https://www.linkedin.com/in/guillaume-bertherat-3b7a071b3/) : visualizations creator
- 🧔‍♂️ [Daniel Santos](https://www.linkedin.com/in/daniel-santos-dev-fullstack/) : enhancements on the API and docker image publish automation

## 🔖 Resources

### 🤓 Source code

{% github opt-nc/generative-art-temps-attente %}

### 🛍️ API on RapidAPI.com

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ua5grlbcbutaktou9y8r.png)](https://rapidapi.com/opt-nc-opt-nc-default/api/temps-attente-en-agence/details)