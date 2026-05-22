---
comments: 10
id: 1726068
is_dev_challenge: false
published_at: '2024-02-14T07:15:10Z'
reactions: 3
reading_time_minutes: 2
tags:
- ai
- python
- tutorial
- showdev
title: 🪄 Put magic in your Notebook w/ Jupyter-AI
url: https://dev.to/adriens/put-magic-in-your-notebook-w-jupyter-ai-3co4
---

## ❔ About

I recently saw this tweet on my thread:

{% twitter 1686773501049327616 %}

👉 Quite immediately I was excited to give it a try.

Sometimes, you may need to **seamlessly call various AI inferences... so it may look like en embedded pair-programming that keeps your notebook clean**, compact, smart and still highly understandable** so people (including yourself) can focus on the storytelling.

## 🪝 Teaser

This notebook is dedicated to a **(not so) short** [`jupyterlab/jupyter-ai`](https://github.com/jupyterlab/jupyter-ai) unboxing **so anyone can enjoy this kind of magic (and much much more)**:

```python
%%ai gpt4 -f markdown
Write a haiku about Python.
```

.. and get the output in the next cell:

```
Python code so clean,
Logic flowing like a stream,
In data, we glean.
```

## 🧙 Tricks you don't want to miss
 
... and many other cool tricks like:

- [**↔️ Deal with input and output variables**](https://youtu.be/VPJZLKKg4vM?si=_DHOC40S8IXcn_uo&t=777) (aka. `PROMPT` templates)
- [**𝕏 Write nice looking `LaTeX`**](https://youtu.be/VPJZLKKg4vM?si=Sh3OjBk66ZQgueTJ&t=919) like formulae
- [**🐍 Code generation**](https://youtu.be/VPJZLKKg4vM?si=coyLvyTYaOQptuVz&t=1055)... and execution
- [**📊 Dataviz**](https://youtu.be/VPJZLKKg4vM?si=w7GbCTY_674uftEy&t=1530) by plotting data
- [**🗣️ 🤖 Chat** with a dataframe](https://youtu.be/VPJZLKKg4vM?si=F98PYNkbf8Z51T-u&t=1232)
- [🌟 **📜 Restaurant customer experience** ](https://youtu.be/VPJZLKKg4vM?si=cfOQXIPZ0AEffIfo&t=1797)disruption

## 🍿 Demo time

{% youtube VPJZLKKg4vM %}

## 🔖 Resources

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vlejjg26b4kujhk5pegh.png)](https://www.kaggle.com/adriensales/jupyter-ai-magic/)

- [`jupyterlab/jupyter-ai`](https://github.com/jupyterlab/jupyter-ai)
- https://jupyter-ai.readthedocs.io/en/latest/
- [Jupyter AI supported on Kaggle](https://github.com/jupyterlab/jupyter-ai/pull/577)
- [Interpolating in prompts](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#interpolating-in-prompts)
- [Formatting the output](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#formatting-the-output)
- [The `%ai` and `%%ai` magic commands](https://jupyter-ai.readthedocs.io/en/latest/users/index.html#the-ai-and-ai-magic-commands)