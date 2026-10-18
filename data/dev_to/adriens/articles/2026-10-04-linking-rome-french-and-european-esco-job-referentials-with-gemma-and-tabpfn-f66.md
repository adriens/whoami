---
comments: 2
id: 4797503
is_dev_challenge: true
published_at: '2026-10-04T21:11:30Z'
reactions: 3
reading_time_minutes: 3
tags:
- devchallenge
- weekendchallenge
- hf26challenge
- ai
title: 🔗 Linking ROME French and European ESCO job referentials with Gemma and TabPFN
url: https://dev.to/adriens/linking-rome-french-and-european-esco-job-referentials-with-gemma-and-tabpfn-f66
---

*This is a submission for the [Hacktoberfest Weekend Challenge: Build for a Friend](https://dev.to/challenges/hacktoberfest-weekend-2026-10-01)*

## What I Built


I built a while set of resources to link together job and skills referentials : 

- [ROME](https://www.francetravail.fr/employeur/vos-recrutements/le-rome-et-les-fiches-metiers.html) which is the french one
- [ESCO](https://esco.ec.europa.eu/en) which is the European one

**👉 I needed these links as an interoperable dataset to help my students from [IAE MIAGE](https://iae.unc.nc/formations/portail-miage/) ([UNC](https://www.unc.nc/) - University of New-Caledonia).**

They take part to the HackAVP a hackathon that takes place here un New-Caledonia, dedicated to job offers and interoperability, Open Data, and public Open Innovation:

{% twitter 2098146788800970947 %}

By linking these two referentials, it makes it possible to enrich and better understand skills of a job offer...so the apply process should benefit from a quality bump thanks to enriched ESCO semantic (which is much richer than ROME one from my point of view).


 
## 📑 Demo

I did not yet have time to make a video on this schedule as my Kaggle notebooks took hours of GPU to produce the data.

<!-- Share a deployed link or a video demo. -->

Here is the notebook that computes the links : 

- [Rapprochement ROME v4 ESCO 1.2.1](https://www.kaggle.com/code/adriensales/rapprochement-rome-v4-esco-1-2-1)

... which produces and shares data into a dataset : 

- [ROME ESCO mapping](https://www.kaggle.com/datasets/adriensales/rome-esco-mapping)

... then produced a dedicated analysis Notebook : 

- [ROME ESCO mapping analysis](https://www.kaggle.com/code/adriensales/rome-esco-mapping-analysis)

## Code

To achieve this work, I needed a lot of data, here it is : 

- [github.com/adriens/odata-esco](https://github.com/adriens/odata-esco) which takes ESCO csv exports and builds a duckdb database on top of it to make data as smart and usable as possible
- [Kaggle ESCO v1.2.1 dataset](https://www.kaggle.com/datasets/adriensales/esco-v1-2-1) : the previous duckdb ESCO database as a Kaggle dataset 
- [Kaggle loader ROME v4](https://www.kaggle.com/code/adriensales/rome-v4-base-duckdb)  base DuckDB to prepare the Rome v4 dataset
- [Kaggle Rome v4 Dataset](https://www.kaggle.com/datasets/adriensales/rome-v4) dataset
- [Rapprochement ROME v4 ESCO 1.2.1](https://www.kaggle.com/code/adriensales/rapprochement-rome-v4-esco-1-2-1)
 : The mapping Notebook
- [ROME ESCO mapping Dataset](https://www.kaggle.com/datasets/adriensales/rome-esco-mapping)
- [ROME ESCO mapping analysis](https://www.kaggle.com/code/adriensales/rome-esco-mapping-analysis) : some analysis on the resulting Kaggle dataset

## 🧰 How I Built It

I built everything on Kaggle, on my GPU free plan: 

I only used Open models on Kaggle : 

- [EmbeddingGemma](https://www.kaggle.com/models/google/embeddinggemma/Transformers/embeddinggemma-300m/1)
- [gemma-4-e4b-it](https://www.kaggle.com/models/google/gemma-4/Transformers/gemma-4-e4b-it/1)
- [gemma-4-12b-it](https://www.kaggle.com/models/google/gemma-4/Transformers/gemma-4-12b-it/2)
- [gemma-4-31b-it-qat-q4_0-gguf](https://www.kaggle.com/models/google/gemma-4/Gguf/gemma-4-31b-it-qat-q4_0-gguf/2)
- [hf-model/BAAI/bge-reranker-v2-m3](https://www.kaggle.com/refs/hf-model/BAAI/bge-reranker-v2-m3)

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/rsate3abr9wybpha97nb.png)


## 🤗 Why Does Open Innovation Matter?

Open Innovation matters for a living democracy, to spread knowledge, skills and efficience of public services.

This is why I spend so much effort on this topic, like reading books, producing prototypes and teaching it to students to show that it works for real, in real life and has a tremendous impact on our society and freedome, especially when linked to Open Source software and Open Data.

And if the result or data does not really fit your needs or don't really match your expectations... you can do your own.

At last, it brings transparency... which is central by many concerns. This is why I wanted to link french referential with the european one.

## 🏆 Prize Categories

- Best Use of TabPFN
- Best Use of Gemma

## 📷 Screenshots


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/odeuhvkj5bfntca8g7ab.png)


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/notuznc3x1z0vavst7r2.png)

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/q3d6e4nern9y5gt6x8js.png)

###  When Gemma disagrees with TabPFN, be carefu

> Precision of the model's first choice, split by whether Gemma E4B picked the same ESCO occupation. The black tick is the model alone, all cases together.

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/o6jl1nt9mkfht0jn92kf.png)


![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/7m47xd0xn9d7rm26eugd.png)

### Coverage by job family

![Image description](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/mcfly6pmoce39ewhksrs.png)




