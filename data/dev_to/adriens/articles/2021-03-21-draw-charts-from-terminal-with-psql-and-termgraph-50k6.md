---
comments: 0
id: 640194
is_dev_challenge: false
published_at: '2021-03-21T20:08:34Z'
reactions: 4
reading_time_minutes: 1
tags:
- postgres
- analytics
- bash
title: Draw charts from terminal with psql and termgraph
url: https://dev.to/adriens/draw-charts-from-terminal-with-psql-and-termgraph-50k6
---

:bulb: Open Data and charting in terminal

As a big fan of both Open Data, PostgreSQL, terminal tricks and data analysis, I wondered what kind of story I could tell on these topics.

Since one year now I feed an Open Data repo with COVID-19 from New-Caledonia :

{% github adriens/covid19-action-plan-nc %}

To "celebrate" this full year of daily datas, I decided to implement something cool around it and thought about the following scenario :

:point_right: The plan

1. Git clone the Open Data COVID cases I feed everyday
2. Load the csv data in the PostgreSQL table with the `COPY` statement
3. Prepare some ready to use reporting views
4. Dump these views as `csv` files
5. Produce charts from the command line, **for the command line** with the help of a great and cool tool called `termgraph` :

{% github mkaz/termgraph %}

Also, to make it available even for non technical people.

I decided to implement it on [Katacoda](https://www.katacoda.com/devops-labs/courses/postgresql/covid-psql), so everyone can enjoy it from any web browser and look like a kind of `hacker` :sunglasses:

:cinema: Demo

{% youtube kXwSfVa1yBA %}



