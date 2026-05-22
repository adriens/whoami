---
comments: 9
id: 1981288
is_dev_challenge: false
published_at: '2024-11-25T20:57:55Z'
reactions: 1
reading_time_minutes: 6
tags:
- ai
- datascience
- database
- dataengineering
title: '🕵️ OSINT: link company acronyms to Standard Occupation Classification w. Open
  Source LLMs'
url: https://dev.to/adriens/osint-link-company-acronyms-to-standard-occupation-classification-w-open-source-llms-5c6o
---

## 🧑‍🎓 `OSINT`: _"What is Open-Source Intelligence?"_

According to [sans.org](https://www.sans.org/blog/what-is-open-source-intelligence/) :

> _"Open-Source Intelligence (OSINT) is defined as intelligence produced by collecting, evaluating and analyzing publicly available information with the purpose of answering a specific intelligence question."_

In this post, I'll show you an experiment I made.

My main goal is to show how **apparently naive data can lead to valuable intelligence** and help discover new kind of information at scale and see what kind of strategic insights we can get out of it.

> _"[...] information does not equal intelligence. Without giving meaning to the data we collect, open-source findings are considered raw data. It is only once this information is looked at from a critical thinking mindset and analyzed that it becomes intelligence."_

At last we'll focus on

> _"[...] finding meaningful information that is applicable to the intelligence question and being able to provide actionable intelligence[...]."_

## 🔁 Intelligence cycle

We'll implement (and share source code on Kaggle) a full _"Intelligence cycle"_, based on Open Data in input and delivering a brand new enhanced and structured Open Data dataset, whith a - [`ollama`](https://ollama.com/) based approach - GenAI processing step in the middle... **and all the code and used [LLMs publicly](https://ollama.com/search) available.**

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/34glrbuz8xrue7aaz5ty.png)](https://osintteam.blog/the-osint-cycle-getting-familiar-with-the-process-of-data-collection-and-analysis-day3-of-6f53fcdb4234)


## 🍿 For impatients

{% youtube aIzcgofPRf4 %}


## 💭 About Standard Occupation Classifications

The [SOC system ](https://kb.lightcast.io/en/articles/7136419-us-standard-occupation-classification-soc)categorizes jobs in a standardized way to:

- **Help** governments and organizations track employment trends
- **Understand** skill needs
- **Shape** workforce policies

By using a consistent framework, SOC data makes it easier to compare job markets, plan training programs, and respond to shifts in the economy, benefiting both policymakers and employers.

So... **a lot of strategic insights that made me want to attach them to other datasets.**

## 🇫🇷 About the French `ROME` code

In France, the `ROME` (_Répertoire Opérationnel des Métiers et des Emplois_) system does something similar, classifying jobs like "Développeur Informatique" (Software Developer) under specific categories to match skills with job needs and support workforce planning. See [🗂️ Codes ROME database](https://www.kaggle.com/datasets/adriensales/codes-romes-database/data) for more.

## 🤔 About acronyms

Any enterprise has a set of acronyms. I find them very useful as in a way... they are a way to discover point of interests of activities.
Also, when you're a new recrutee, you may need to get the reference to understand common jargon, documents and colleagues in meetings (which was my case).

[OPT-NC](https://www.opt.nc/) publicly shared its acronyms as an Open Data dataset : 

**Tweet de teasing**

In general an acronym has:

- **A very few letters** (let's say `SaaS` for example)
- **A sentence** that explains the meaning which is very specific

So a collection of them **embeds a lot of information, especially when they are specific to your activities.**

## 💡 The idea : delegate to `LLM`

**Being able to put relationships between _acronyms_ and jobs classification should (that's my hypothesis) give insights about activities.**

☝️ But with an ever increasing amount of acronyms & activities... it would be **much much more interesting to delegate relationship creation to a LLM.**

## 🎯 Our goal

In output, we want a traditional well **structured classical database** with integrity constraints: **a ready to use `duckdb` database (and `csv`) that links acronyms and activity codes.**

Here is the way I'll give a try to `OSINT`:

1. **Preparation** : Transform existing open data to well structured datasets
2. **Collection** : Make all required datasets within a single Notebook 
3. **Processing** : Build relationships thanks to LLM and structured outputs
4. **Analysis** : Do some reporting on output data with simple `SQL` and dataviz
5. **Dissimination** : Deliver the output data as a Kaggle `duckdb` dataset

## 🦾 All about relationship automation

The main idea of this prototype is to delegate the hard stuff to LLM **thanks to its core knowledge** :

- No RAG
- No dedicated fine-tuned LLM
- No [Pydantic](https://docs.pydantic.dev/latest/) to ensure well structured outputs

👉 Here, we'll just focus on just **pure prompting over out-of-the-box LLMs.**

1. **Import the acronyms** dataset [📘 Lexique des acronymes de l’OPT-NC](https://www.kaggle.com/datasets/optnouvellecaldonie/lexique-des-acronymes-de-lopt-nc)
2. **Import the SOC/ROME** codes dataset [🗂️ Codes ROME database](https://www.kaggle.com/datasets/adriensales/codes-romes-database)
3. **Build a customized `ollama` model** with a dedicated `PROMPT` to get structured output `json` : [OPT-NC : Acronymes genai augmentés](https://www.kaggle.com/code/adriensales/opt-nc-acronymes-genai-augment-s)
4. **For each acronym, get a collection of `json`** matching SOC/ROME codes from this custom model
5. **LOAD `json` into a staging table** in `duckdb`
6. **Check & remove hallucinations** : check integrity between generated SOC codes and the reference database
7. Share the generated data as a dataset : [OPT-NC acronyms Enhanced by Open Source AI](https://www.kaggle.com/datasets/adriensales/ai-enhanced-opt-nc-acronyms)
8. **Enjoy generated knowledge**: perform some analysis on the the output database, see Kaggle [Notebook OPT-NC acronyms genai exploration](https://www.kaggle.com/code/adriensales/opt-nc-acronyms-genai-exploration)

## ⚖️ Accuracy ratio and LLMs benchmark

With this approach, it is then possible to switch and benchmark various LLMs just by changing a parameter and wait for the Notebook to finish on Kaggle:


| LLM     |Hallucinated ROME Codes|Valid ROME Codes|Duration|
| ---     | ---                   | ---            | ---    |
|`reflection`  | 25               | 127            | 3h47'  |
|`llama3.1:70b`| 31               | 137            | 4h05'  |
|`llama3.1:8b` | 71               | 40             | 4'     |
|`nemotron`    | 41               | 194            | 06h08' |
|`qwen2.5:72b` | 52               | 146            | 06h15' |
|`nous-hermes2-mixtral:8x7b` | 7  | 23             | 08h53' |
|`llama3.3`    | 24               | 199            | 5h 54m |

Next, we can compute the "Accuracy ratio: (valid codes) / (valid codes + hallucinated codes)" :

| LLM                         | Hallucinated Codes | Valid Codes | Accuracy Ratio (%) |
|-----------------------------|--------------------|-------------|---------------------|
| **llama3.3**                | 24                 | 199         | **89.24%**          |
| **nemotron**                | 41                 | 194         | 82.55%              |
| **qwen2.5:72b**             | 52                 | 146         | 73.74%              |
| **llama3.1:70b**            | 31                 | 137         | 81.55%              |
| **reflection**              | 25                 | 127         | 83.55%              |
| **llama3.1:8b**             | 71                 | 40          | **36.04%**          |
| **nous-hermes2-mixtral:8x7b** | 7                 | 23          | 76.67%              |


As my goal is to get as much ROME codes as possible, here are the two best LLMs in my case:

1. 🥇 [`llama3.3:70B`](https://ollama.com/library/llama3.3): This model outperforms others with 199 valid codes and the highest accuracy ratio (89.24%). It strikes an excellent balance between extracting the largest number of valid codes and minimizing hallucinations, making it the top performer for this task. 
2. 🥈 [Nemotron](https://build.nvidia.com/nvidia/llama-3_1-nemotron-70b-instruct) ([`nvidia/Llama-3.1-Nemotron-70B-Instruct`](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct)) : lose behind, this model delivers 194 valid codes and a strong accuracy ratio (82.55%). It's particularly well-suited for tasks requiring comprehensive coverage and moderate control over hallucinations
3. 🥉 [`qwen2.5:72b`](https://ollama.com/library/qwen2.5:72b): hile it ranks third with 146 valid codes, its accuracy ratio (73.74%) is lower than the top two. This model is effective but generates more hallucinated outputs, which might require post-processing.

## 💰 Benefits

For example, [it is then possible to drill down](https://www.kaggle.com/code/adriensales/opt-nc-acronyms-genai-exploration) into categories:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/krjgzqh4pb61oarjnf8e.png)](https://www.kaggle.com/code/adriensales/opt-nc-acronyms-genai-exploration)

## 📑 Resources : Notebooks and datasets

- 🦾 Notebook that links acronyms to ROME codes : [OPT-NC : Acronymes genai augmentés](https://www.kaggle.com/code/adriensales/opt-nc-acronymes-genai-augment-s)
- 📚 Dataset [OPT-NC acronyms Enhanced by Open Source AI](https://www.kaggle.com/datasets/adriensales/ai-enhanced-opt-nc-acronyms/data)
- 📊 Analysis Notebook : [OPT-NC acronyms genai exploration](https://www.kaggle.com/code/adriensales/opt-nc-acronyms-genai-exploration)

Core datasets:

- [🗂️ Codes ROME database](https://www.kaggle.com/datasets/adriensales/codes-romes-database/data)
- [📘 Lexique des acronymes de l’OPT-NC](https://www.kaggle.com/datasets/optnouvellecaldonie/lexique-des-acronymes-de-lopt-nc)

## 📚 Related resources about AI and HRs 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rzw8596karatxgsn75nj.png)

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/s3zm96qgdpujuo0jqm2q.png)](https://www.fonction-publique.gouv.fr/files/files/Publications/Publications%20DGAFP/2024/guide-strategie-usage-intelligence-artificielle.pdf)