---
name: ollama-models
url: https://github.com/adriens/ollama-models
description: "A collection of ready to use ollama models"
language: 
topics: [ai, chatbot, devops, llm, ollama]
stars: 18
created_at: 2023-12-27
updated_at: 2026-01-20
archived: false
has_readme: true
---

# ❔ About

This aim of this repo is to provide ready to use collection of [`ollama` model files](https://github.com/jmorganca/ollama#customize-a-model)
so **anyone can play or fork them.**

# 🔖 Resources

- [:octocat: `ollama`](https://github.com/jmorganca/ollama)
- [🦙 `ollama` models library](https://ollama.ai/library)
- [`ehartford/dolphin-system-messages`](https://github.com/ehartford/dolphin-system-messages)
- https://github.com/ehartford/dolphin-system-messages/issues/1



# 💭  Famous quotes

## :trollface:`evilops`

> "Deploying on a Friday is the epitome of irresponsibility and laziness."

> ["It's like playing a game of Russian Roulette with a machine gun.[...] Drop that worthless table and create a new one with the primary key as an integer. [...]
Always remember, buddy: DBA rules the world! Or at least the database. 😂🐾 "](https://dev.to/adriens/comment/2cc91)

# 🚀 Getting started

Below an example on how to locally run `evliops`:

```sh
# Build model
ollama create evilops -f ./models/evilops 
# Look for model
ollama list | grep evilops
# Use model
ollama run evilops "Should I deploy on friday?"
```