---
comments: 3
id: 1511237
is_dev_challenge: false
published_at: '2023-07-05T08:47:07Z'
reactions: 0
reading_time_minutes: 2
tags:
- ai
- design
- marketing
- automation
title: 🧑‍🍳 From ${dessert.description} to dessert teaser w/ GenAI 🎬
url: https://dev.to/adriens/from-dessertdescription-to-dessert-teaser-w-genai-5gfd
---

## 🗣️ The pitch

I want to create a pipeline that take as

1. Inputs :
    - 🖹 A **raw description** of the dessert
    - 📷 A **photography**
2. Output :
    - 🎬 An impressive and inspiring video teaser

## 🎦 For the impatients

{% youtube gptgQwabSwY %}



## 🧑‍🍳 Creation recipe

1. Get the dessert description (see [`auptitcafe-sdk`](https://github.com/adriens/auptitcafe-sdk) `pypi` package)
2. Design a `PROMPT` that takes `${dessert.description}` as input
3. Get the script out of `PROMPT` injection from `ChatGPT`
4. Get a vocal speech `TTS` out of previously generated speech with `ElevenLABs`
5. Inject offical dessert photoshots and animate them with [leiapix](https://convert.leiapix.com/)
6. Create an avatar on Bluewillow
7. Create a covert artwork with MS Designer
8. Put it all together with shotcut
9. Publish the teasee on Youtube
10. Share the teaser with a nice [QR Code AI Art](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jyj1ow39zalp6ifpaxqy.png)

## 📜 `ChatGPT` Prompt 🇫🇷

> Imagine que tu es un chef pâtissier dans le restaurant "Au p'tit café", un grand restaurant français très apprécié des gourmets calédoniens.
> Ta mission est de me présenter le dessert signature du restaurant afin de le mettre en valeur au mieux.
> Le dessert signature (incontournable) du restaurant est le "`${dessert.description}`
> Tu me le présenteras afin de le rendre très désirable aux yeux de plus gourmands et gastronomes les plus avertis.
> Tu t'exprimeras dans un français impeccable digne d'un mojordome. 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mr23z1s7l566vg68xdlh.png)

## 🧰 Core tools

### 🪛 `auptitcafe-sdk`

The sdk to interact with restaurant's website : [`auptitcafe-sdk`](https://github.com/adriens/auptitcafe-sdk)

### 🤖 `ChatGPT`

For now ChatGPT, but implementable on others LLMs. Will subscribe openai API soon.

### 🎙️ ElevenLABs

[ElevenLABs](https://beta.elevenlabs.io/) The Text-to-Speeh, stable, API driven and high quality contents. Very easy as we don't have to chunk our input script.

### 🎬 LeiaPix

Discover [LeiaPix](https://convert.leiapix.com/) :

{% youtube 6aHMepbNkmE?t=469 %}

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/yq1xv2eqhn2ld5fgq4ni.png)

## 🧑‍🎨 Artistic QrCodes

For example use [`huggingface-projects/QR-code-AI-art-generator`](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator)


[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7b5au9ji061l9doksub7.png)](https://huggingface.co/spaces/huggingface-projects/QR-code-AI-art-generator)

## 💭 Pipeline time to market considerations

Most of these AI bricks make it possible to create content and produce original and automated professoinal looking storytellings.

I may now look forward to fully automate the whole process... also trying to rely on **nocode platoforms **([`make`](https://www.make.com/en), [`IFTTT`](https://ifttt.com/), [`zapier`](https://zapier.com/),...) to **make the creative process more affordable to non-programmers** to open this process to non-coders... and then make this more technically accessible to more content creators... or to reduce content creation time to market 😜.

## 🔭 Further about `AI`

Will AI steal our jobs ? Let's dive a little bit more about bibliography and the opportunities it opens.

### 📚 Book

{% twitter 1674550378317357056 %}

### 📺 Can AI create Art ?

{% twitter 1674733412513619968 %}