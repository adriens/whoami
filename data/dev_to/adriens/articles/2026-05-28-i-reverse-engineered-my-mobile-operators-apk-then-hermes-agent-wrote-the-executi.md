---
comments: 2
id: 3767131
is_dev_challenge: true
published_at: '2026-05-28T23:01:45Z'
reactions: 0
reading_time_minutes: 5
tags:
- hermesagentchallenge
- devchallenge
- agents
- datascience
title: ⚚ I reverse-engineered my mobile operator's APK — then Hermes Agent wrote the
  executive report
url: https://dev.to/adriens/i-reverse-engineered-my-mobile-operators-apk-then-hermes-agent-wrote-the-executive-report-2j3o
---

*This is a submission for the [Hermes Agent Challenge](https://dev.to/challenges/hermes-agent-2026-05-15): Write About Hermes Agent*

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5s4ragmo9l44h9n03ugp.png)

{% twitter 2059698327235805258 %}

## 🍿 Demo

{% youtube Zw-lfNFA0fQ %}

## 📸 Screenshots

Just check how amazing these reports look like!

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/h35idkeksm06uvxqopw9.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4ggs9a2sbj4p1xmqe7p1.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ku8badzwm9b1aewey8vw.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9f0a1bal7o4n17fpjzcn.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d3559l8zh7mjwy1gc1ok.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ibzai5n6shn80b2xpcni.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5bb2u5qzo6tv9yo7982o.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vq7ccs37sz474pk7h3yi.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xl7wt2yzvp7pyhj1s9o6.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/phb10ou2plkwtqdnkns2.png)









# Building a Multi-Stakeholder API Monitoring Report with Hermes Agent

"Just generate a PDF" — famous last words. What started as a simple request turned into something much bigger: a full monitoring stack for my mobile operator, built evenings and weekends, culminating in a 17-page professional report that would have taken a full week to build manually. Total cost with Hermes Agent: **$19.57**.

---

## 🏝️ The Backstory: A Stack No One Else Has

I'm Adrien, a developer in New Caledonia. OPT-NC's Helia mobile service has an app — but no public API, no CLI, nothing on any marketplace. So I **reverse-engineered the APK**, extracted the private HTTP calls, and rebuilt them in a **Go CLI** that snapshots voice, data, and SMS consumption every 5 minutes into a local **DuckDB** database.

Then I built **KDE Plasma widgets** in Python/PyQt that read from DuckDB and display live on my desktop — mirroring the official app's data, but with history, trends, burn rate, and alerts. Plus a **system tray icon** showing live API status at a glance.

The official app shows you *now*. My stack shows you *now, history, trends, and alerts.*

**No other Helia customer has this.** That's the breakthrough.

---

## 🎯 The Problem Hermes Agent Solved

All this data was sitting in DuckDB. The question was: *how do I present it to people who don't speak SQL?*

Three completely different audiences: the **CEO** who needs a 30-second summary screenshot-ready for PowerPoint, the **CIO** who wants ROI in euros and SLA compliance, and the **Network Admin** who needs actionable tickets with specific hours and error patterns.

---

## 🎭 The Role-Playing Game That Became the Design Document

Before writing a single line of code, I asked Hermes Agent to do something unusual: **simulate a full team meeting** with 7 personas — CEO, CIO, network admin, developers, and marketing.

It produced a full transcript. Each persona argued their case:
- The **CIO**: *"I need ROI in euros, not percentages."*
- The **CEO**: *"I need the 30-second version I can project tomorrow morning."*
- The **Network Admin**: *"Give me Jira tickets with specific hours, not a dashboard."*

That transcript became the design document. Every page of the report was written against a specific person's stated need. No guessing. No generic output.

---

## ⚡ What Hermes Agent Built in ~1 Hour

**It started with the data.** No assumptions — it queried the schema and immediately caught something: average latency was 2,534ms but the median was 204ms. Bimodal distribution. That single insight shaped every chart.

**It extracted brand colors from the website** before writing a single line of LaTeX. Hermes Agent opened Helia's site, pulled the magenta/pink gradient from the SVG logo, and used it consistently across every chart, table, and tcolorbox. Small detail. Big difference.

**Then it built everything:**
- 4 Python scripts: latency distributions, timeout heatmap, sparkline, 4-panel executive chart
- Full XeLaTeX report with TikZ progress bars and brand-colored boxes
- A French accent fixer script baked into the pipeline

One message: *"update with fresh data"* — triggered 8+ tool calls automatically: DuckDB → diff → scripts → charts → LaTeX → 2× compile → verify.

---

## 📊 The Charts It Produced (Without Being Asked)

I asked for charts. I didn't ask for *this*:

**Latency distribution** — median/mean/P95 lines labeled, shaded fast vs slow zones, annotated arrow pointing to the long tail: *"Queue longue (timeout ~12s) (~40% des pings)"*. Log-scale version revealing the true bimodal structure: two peaks at ~80ms and ~4s.

**4-panel executive dashboard** — availability gauge (87.2% vs 99.5% SLA), latency (2534ms vs 500ms — *"5.1x trop lent"*), timeout rate (*"1 requête sur 8 échoue"*), composite SLA score per metric. **Score global: 65%. Verdict: RED.**

**Timeout heatmap** — all 18 timeouts concentrated on Wednesday evening 19h–22h. The rest of the week: clean. Instant actionable insight for the network admin.

All in Helia brand colors. All annotated. None of it explicitly requested.

---

## 📋 The Executive Summary: Fits in One Slide

Page 3 of the report is designed to be screenshotted directly into PowerPoint. Verdict box at the top (red), plain-language translation (*"1 call in 8 fails"*), business impact in euros, top 3 problems with responsible parties. The CEO gets it in 30 seconds.

---

## 🧠 What I Learned

**Orchestration is the real superpower.** I asked for a PDF. It fetched brand colors, queried the DB, wrote Python scripts, compiled LaTeX — all unprompted.

**Iteration is the default.** The first charts were basic. The final ones have annotated thresholds, color-coded data points, and statistical summaries. That's the loop.

**Skills are the real ROI.** Everything got distilled into a reusable `~/.claude/skills/reporting-latex/` skill. Next similar project starts at 80%, not zero.

---

## 💰 The Cost

**[Qwen3.7-Max](https://openrouter.ai/qwen/qwen3.7-max) via OpenRouter.** Alibaba's flagship agentic model, built for long-horizon autonomous execution.

**326 requests. 61.4M tokens. $19.57. ~1 hour. vs a full week manually.**

---

## 🖥️ What's Next

The next step: **run it all locally**. I'm currently eyeing an [Apple Mac Studio M4 Max](https://www.ldlc.com/fiche/PB00675416.html) — 16-core CPU, 40-core GPU, 64 Go unified memory. New Caledonia is 20,000km from everything; local inference just makes sense. Zero API costs, zero latency to the cloud, full control.

With 64GB unified memory, I'd be able to run:
- **Qwen3-Coder-Next** — purpose-built for agentic coding, 70%+ on SWE-bench, needs 46GB RAM ✅
- **Qwen3.5-35B-A3B** — the 2026 community default for local inference, ~80 tok/s via MLX ✅
- **Qwen3.6-27B** — optimized specifically for agentic coding workflows ✅

The same class of model as Qwen3.7-Max on OpenRouter — locally, for free, forever. A fully local Hermes Agent stack.

*From $19.57 on OpenRouter to owning the hardware. That's the roadmap. 🇳🇨*

---

The pattern: **monitor → query → visualize → compose → translate**. The *translate* step — turning a percentile into a story a CEO can act on — is where Hermes Agent earns its keep.

---

*Have you used Hermes Agent for multi-tool orchestration? Curious how your experience compares.*