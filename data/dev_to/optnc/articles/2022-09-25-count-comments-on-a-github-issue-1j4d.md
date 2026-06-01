---
comments: 4
id: 1122823
is_dev_challenge: false
published_at: '2022-09-25T20:23:02Z'
reactions: 12
reading_time_minutes: 1
tags:
- github
- productivity
- tutorial
- tooling
title: 📊 Count comments on a GitHub issue 🎫
url: https://dev.to/optnc/count-comments-on-a-github-issue-1j4d
---

## ☝️ Why counting comments matters ?

There are two type issues with a lot of comments : 

1️⃣ The ones that are popular, then getting a lot of feedback 🤗
2️⃣ The ones that have a lot of comments because we struggle to fix them efficiently 😱

👉 In both cases, performing report on them can be helpful to monitor your `RUN` performances.

## ❔ Count with API calls

☝️ There actually is no native [`gh issue`](https://cli.github.com/manual/gh_issue) command to count issues on a specific command...

👉 but [`gh api`](https://cli.github.com/manual/gh_api)...

> _"Makes an authenticated `HTTP` request to the GitHub API and prints the response."_

```shell
gh api <endpoint> [flags]
```

💡 This short post is documenting how easy it is to count comments on a given issue.

## 🤓 Snippet

```shell
gh api -X GET \
  -H "Accept: application/vnd.github.v3+json" \
  -F per_page=100 \
  /repos/YOUR_ORGA/REPO/issues/ISSUEID/comments | \
  jq '. | length'
```


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/phorj3zhmgpmwrs077b0.png)