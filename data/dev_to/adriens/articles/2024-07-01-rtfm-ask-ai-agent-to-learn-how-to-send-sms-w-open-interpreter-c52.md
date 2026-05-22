---
comments: 5
id: 1897464
is_dev_challenge: false
published_at: '2024-07-01T22:07:14Z'
reactions: 3
reading_time_minutes: 2
tags:
- nocode
- ai
- showdev
- tutorial
title: '🗣️🦾📲🤓 RTFM : ask AI agent to learn how to send sms w. open-interpreter'
url: https://dev.to/adriens/rtfm-ask-ai-agent-to-learn-how-to-send-sms-w-open-interpreter-c52
---

## 💭 About

How many times did someone ask you : 

> _"How do you..."_

... and how many times did you make the [RTFM (Read the Fucking Manual)](https://en.wikipedia.org/wiki/RTFM) joke ?

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/u0k334ro41v9z0imgpzj.png)

👉 Well that's all this blog post is all about, we're going to:

1. **🎁 Provide a `cli` tool that behaves like all other tools** to an AI assistant
2. **🦥 Ask it to learn by himself** how to use it
3. **🚀 Make it do the job** ... locally !

To achieve this we will use : 

- **🤖 A core `LLM` engine** : `gpt-4`
- **💻 A locally running assistant** that is able to create an action plan to achieve a goal : [Open Interpreter](https://www.openinterpreter.com/)

## 🎯 What we'll do

This time, thanks to a custom tool I created last week-end : 

{% embed https://dev.to/adriens/mobitag-go-hackathon-2024-06-22-week-end-2n16 %}

and ask the **AI Assistant to discover the tool and send a custom sms** with a custom content to myself with it.

## 🧑‍🏫 Teach him how to use the tool

{% youtube 9BTJ2sCbTbg %}

## 🤣 Funniest `sms`

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/cq1pdh5oyligk9ywghkl.png)

## 🔭 Perspectives

The same way we used the `--help` pattern for `cli` tool, we can use the [OpenAPI](https://swagger.io/specification/) to tell an AI how to use an API as a tool.
But keep in mind : the better the documentation, the easier and better integration will be... at almost 0 effort (which is our target to scale automation).

Below some examples of how to achieve this on various frameworks & services :

## 🤓 For coders : 

- [🦙 LlamaIndex](https://www.llamaindex.ai/) : [OpenAPI Tool](https://llamahub.ai/l/tools/llama-index-tools-openapi?from=all)
- [🦜 Langchain](https://www.langchain.com/) : [OpenAPI tool](https://python.langchain.com/v0.2/docs/integrations/toolkits/openapi/)

## ⏱️ `< 5'` demo : build & deploy conversational agents (non-coders)

Least but not last, for non coders [Google Vertex AI Agent Builder](https://cloud.google.com/dialogflow/vertex/docs/concept/tools) to **build and deploy Agents ... within 5 minutes** : 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/chc4hgfc9ujkzzsvcmjk.png)](https://youtu.be/0QbUYfTRJEY?si=lVbF-8ssL_8zq6ZF&t=547)