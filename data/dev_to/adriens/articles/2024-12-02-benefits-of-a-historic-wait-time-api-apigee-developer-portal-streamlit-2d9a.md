---
comments: 7
id: 2127410
is_dev_challenge: false
published_at: '2024-12-02T20:16:29Z'
reactions: 0
reading_time_minutes: 3
tags:
- datascience
- ux
- python
- api
title: '📊 Benefits of a historic wait time API: apigee developer portal & Streamlit'
url: https://dev.to/adriens/benefits-of-a-historic-wait-time-api-apigee-developer-portal-streamlit-2d9a
---

## 🤔 Where we come from

We previously did release waiting time and offices as open data and APIs:

{% youtube Y5PWxaxz1_E %}

... yet we were only able to give the current waiting time snapshot:


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kmc52814w37bbs0w92y9.png)](https://www.opt.nc/service/l-opt-pres-de-chez-moi-trouver-une-agence)

Last year, while projecting myself as a customer, I found that it would be useful to

1. **💾 Keep the historical data** of waiting time in an database : we chose Opensearch to be able to get nice looking dashboards as quick as possible
2. **🎀 Serve the data **as a nice looking API
3. **🛒 Share the API** on our portal developer on APIGEE 
4. **➿ Quickly build a first prototype** on top of the API with students to get feedbacks (and give some bug bounties)  so we could build a develper friendly API

**👉 This post is all about this last this adventure with students.**

## 🎯 The pitch

Essentially as a PO, what I wanted was to be able, from a web interface to

- Pick any office
- Be able to browse the historical data of the current day

... and this is what we got:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jperwy1ct3bsz6ilxdny.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ca9ia1w94g7gaifqgd7d.png)


## 🍿 For impatients

{% youtube C3yKrT0Z-mg %}

## 💰 Benefits of historical wait time data

There are a lot of benefits and potential that come with wait time, both : 

- For the customer
- For enterprise


### 🤗 Customer : trends benefits

- While the current wait time gives you a snapshot, historical data gives you trends that make it possible for you to know if queuing is currently getting better or worst
- Makes it possible to the customer to choose the best time to come to the office (see [_"Crowdsourcing Feature Lets iPhone Users Determine Best Time to Cross U.S. Border"_](https://today.ucsd.edu/story/crowdsourcing_feature_lets_iphone_users_determine_best_time_to_cross_us_b))


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dy6c3t3uyzm78ar075yk.png)](https://today.ucsd.edu/story/crowdsourcing_feature_lets_iphone_users_determine_best_time_to_cross_us_b)

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wzj4z988endruab4c2ys.png)](https://today.ucsd.edu/story/crowdsourcing_feature_lets_iphone_users_determine_best_time_to_cross_us_b)


### 🏢 Enterprise benefits and data-driven strategy

eg, from the service provider perspective, the main goal is to both:

- **📉 Minimize customers wait time** to smoother Customer Experience (which also relies on digitalization and self service)
- **📈 Maximize service throughput** : serve as much customers as possible with as less people a possible waiting in the office

So sharing live and historical wait time trends has a major impact and **opens tremendous opportunities**, see below some real life examples:

- Share historic data as ready to use open datasets to make Open Innovation possible
- Smart Wait Estimates: [Increase customer satisfaction with accurate wait time quotes](https://www.waitlist.me/features/smart-wait-estimates/)
- The Disney World case : [Predicting Disney World Wait Times with Neural Networks](https://www.andrewmunsell.com/blog/predicting-disney-world-wait-times-neural-networks) : _"In general, you can predict what sorts of wait times to expect based on the day of the week and the season-- September, for example, tends to have fairly low attendance due to kids going back to school"_
    - Publicly share trends : [Disney Magic Kingdom queue time statistics](https://queue-times.com/parks/6/stats)
    - [Disney Magic Kingdom crowd calendar](https://queue-times.com/parks/6/calendar)
    - [Disney Magic Kingdom live queue times](https://queue-times.com/parks/6/queue_times)
- US Customs and [Border Protection Airport Wait Times](https://awt.cbp.gov/)
- Government of Canada: [Historical Border Wait Times – Land Mode](https://open.canada.ca/data/en/dataset/000fe5aa-1d77-42d1-bfe7-458c51dacfef) 

## 🔖 Resources

- [API on Developer Portal](https://apigee-optnc-prd-api.apigee.io/)
- [Docker image](https://hub.docker.com/r/optnc/opt-temps-attente-agences-api)
- [API documentation](https://opt-nc.github.io/opt-temps-attente-agences-api/)
- [Slideshow](https://adriens.github.io/temps-attente-streamlit/)
- [Source code](https://github.com/adriens/temps-attente-streamlit)

## 🧑‍🎓 More about University partnership

{% youtube yOAKC5cTDc8 %}