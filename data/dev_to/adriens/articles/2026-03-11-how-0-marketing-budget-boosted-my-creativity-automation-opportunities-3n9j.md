---
comments: 5
id: 3049555
is_dev_challenge: false
published_at: '2026-03-11T20:11:05Z'
reactions: 8
reading_time_minutes: 3
tags:
- automation
- marketing
- design
- showdev
title: 💸 How $0 marketing budget boosted my creativity & automation opportunities
url: https://dev.to/adriens/how-0-marketing-budget-boosted-my-creativity-automation-opportunities-3n9j
---

## 💡 Inception back in days

Years ago I watched the following [Netflix series](https://www.netflix.com/nc/title/80057883) : 

> A look beyond blueprints and computers into the art and science of design, showcasing great designers from every discipline whose work shapes our world.

{% youtube dmWeJVtv1lw %}

Then wrote a [dedicated article](https://www.linkedin.com/pulse/how-did-netflix-put-my-heart-brain-fire-abstract-art-design-sales/) : 

> How did Netflix put my heart & brain on fire with "Abstract: The Art of Design"​ S02

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1ipnf2n7291yvdbl8jfh.png)](https://www.linkedin.com/pulse/how-did-netflix-put-my-heart-brain-fire-abstract-art-design-sales/)

That brought me a lot of inspiration about : 

- The power of simple/pure designs
- Importance of typography
- How to manage color gradients
- How a minimalist design opens opportunities
- How playing with things makes us creative and productive ([Cas Holman](https://casholman.com/), founder of toy company)

## ⏳ About `geol` : the need for a logo

Then since last year we started to work on [`geol`](https://github.com/opt-nc/geol), and I started to feel the need to get a logo for example to : 

- Display in the terminal
- Show up in youtube thumbnails
- Give an identity to our [website](https://opt-nc.github.io/geol/) (we [built one w. Docusaurus](https://youtu.be/JHWafHI52D8))

So I filled an issue... to fix later.

## 🎨 How low marketing skills and budget boosted my creativity

{% twitter 1992068608395276623 %} 

## 🍿 Show me what it looks like

{% youtube iRfW13FleGE %}

## 📝 Inception and paper/pen drafts

To build a logo, you need to focus on what your product does at its very core.
In my case, I came to the conclusion that there were two core things: 

- **⏳ Pay a tribute** to the data source : [`endoflife.date`](https://endoflife.date/) API
- **🚦 Colors** which is the color identities, know when:
    - **🟢 We're ok** with a product,
    - **🟠 When we should start to take care**: time to plan
    - **🔴 When it's too late**: you're at risk

So finally, two dimensions : 

- 📐 Shape
- 🎨 Colors

It started to trigger my curiosity about geometric considerations, which could hence be described thanks to mathematical objects, **finally opening coding and automation opportunities.**

I started to draw and draw a lot of shapes, think about how to put colors, the benefits of a simple geometrical/mathematical vectorial approach while enjoying a coffee cup outdoor seating at a café, drafting ideas and charts w. the paper/pen strategy : 

{% twitter 2025338147153084787 %}

## ☝️ Put more constraints to be more productive

I really love the pattern that consists of putting more rules to be more creative and just:

> see what happens if...

Finally I got my own rules.

The logo should:

1. **Be perfectly described with a few mathematical** geometrical rules as possible (easier to code or to draw, even by a kid)
2. **Give sense to colors** and product lifecycle
3. **Pay a tribute to its core meaning** : the hourglass
4. **Fun with graph datascience**: it has to be both eulerian and hamiltoninan 
5. Be as light as possible

## 🚀 Pure code and automation

Once I found the solution came the coding part:

- Design the `svg` (and put placeholders inside them)
- Create a [`Taskfile`](https://taskfile.dev/) to automate a bunch of things (generate various formats from a single `task` command)
- Inject colors with code and automation
- Create automation tasks that build jpeg, png, animated & static gifs, webp, optimize jpeg... all built and delivered as output artefacts

So finally I came from a workflow on a paper to a fully automated makefile:

{% twitter 2030389652960710939 %}

## 🖼️ Benefits : the `100%` LaTeX cheatsheet

As a benefit I could produce a 100% LateX version of the logo ([see full demo](https://youtu.be/iRfW13FleGE?si=1A9q3YO6ZM8i_-T6&t=801))

{% twitter 1995616096351891548 %}

## 🔭 Further opportunities

What's exciting with a "simple logo" is that it makes it possible to use the mathematical vectorial description and inject it in many artistic artefacts

- 3d printing
- Pixelart
- T-Shirts
- Code driven animations
- Shaders
- Desktop Wallpapers

Who knows where creativy will take us 🤗