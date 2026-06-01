---
comments: 7
id: 1212516
is_dev_challenge: false
published_at: '2022-10-10T20:25:55Z'
reactions: 2
reading_time_minutes: 2
tags:
- tutorial
- productivity
- kafka
- linux
title: ⌨️ Pipe xlsx files into/from Kafka... From cli with (k)cat 🙀
url: https://dev.to/optnc/pipe-xlsx-files-intofrom-kafka-from-cli-with-kcat-plp
---

## 🪝 Teaser

What you'll discover in this post is how we could, within a [dedicated KillerCoda scenario](https://killercoda.com/opt-labs/course/kafka/kcat) :

- Literally `pipe` data to and from Kafka, from (and to) any file, with the `|` operator
- Visualize data on a cool web interface on [Redpanda Console](https://github.com/redpanda-data/console)

## 🍒 on the 🍰

We'll play with real life data from [isee.nc](https://www.isee.nc/component/phocadownload/category/10-ridet) :

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xir0qhy83naa4tkepqbj.png)](https://www.isee.nc/component/phocadownload/category/10-ridet?download=2027:liste-etablissements)


☝️ Now... to fully enjoy this post, please be sure to really 

> 👉 deeply understand what `pipe` is, how and why it was created... and all the amazing opportunities it opened since its early ages.

## 🪄 Intro : Unix Pipeline 🦸‍♂️

Spend 5' to deeply understand how and why the `|` was created and **why it still matters (a lot) today**.

{% youtube bKzonnwoR2I %}

## 🧰 Tools (and Philosophy) 🏺

Now, you can jump start in the demo where we'll do everything from the terminal thanks to all these amazing, [`UNIX` Philosophic](https://en.wikipedia.org/wiki/Unix_philosophy) single-purposed tools : 

- [`cURL`](https://en.wikipedia.org/wiki/CURL)
- [`pipe`](https://en.wikipedia.org/wiki/Pipeline_(Unix))
- [`kcat`](https://github.com/edenhill/kcat)
- [`xls2csv`](https://github.com/xevo/xls2csv)
- [`jq`](https://stedolan.github.io/jq/)
- [`tail`](https://en.wikipedia.org/wiki/Tail_(Unix))
- [`head`](https://en.wikipedia.org/wiki/Head_(Unix))
- [`cut`](https://en.wikipedia.org/wiki/Cut_(Unix))
- [`comm`](https://en.wikipedia.org/wiki/Comm)
- [`sort`](https://en.wikipedia.org/wiki/Sort_(Unix))
- [`column`](https://man7.org/linux/man-pages/man1/column.1.html)
- [`sed`](https://en.wikipedia.org/wiki/Sed)
- [`awk`](https://en.wikipedia.org/wiki/AWK)
- [`wc`](https://en.wikipedia.org/wiki/Wc_(Unix))

## 🍿 Full demo

{% youtube t_UhRhLU2II %}

## 🔖 Resources

- [Dedicated Killercoda scenario](https://killercoda.com/opt-labs/course/kafka/kcat)