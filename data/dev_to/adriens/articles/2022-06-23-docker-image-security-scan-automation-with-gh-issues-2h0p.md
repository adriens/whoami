---
comments: 8
id: 1100251
is_dev_challenge: false
published_at: '2022-06-23T21:47:55Z'
reactions: 7
reading_time_minutes: 3
tags:
- docker
- devops
- infosec
- devsecops
title: 🎟️ Docker image security scan automation with GH issues
url: https://dev.to/optnc/docker-image-security-scan-automation-with-gh-issues-2h0p
---

## ☝️ Context

Docker image security is an ever increasing trend. But more than a trend, not achieving a proper pipeline around images security can lead to disasters.

To achieve that we adopted the following strategy : 

- Rely on highly securely maintained images
- Paying attention to dependency management

Dependency management is managed thanks to DependaBot, and it'as available almost "Out of the Box".

**For docker imaged there is some more work.**

👉 In this short post you'll see how we implemented a repo-centric and CI driven efficient approach.

## 📝 Implementation

For docker image scan, we rely on the [Container Scan (GitHub Action)](https://github.com/marketplace/actions/anchore-container-scan) maintained by [Anchore](https://anchore.com/).

> Then we wrapped some CI around it so we can monitor security as part of our daily activities.

### ⏰ Schedule scans

First, we have scheduled scans. Below our code to scan the `latest` tag : 

```yaml
name: 🛡️ Scan Docker image latest 🐳

on:
  schedule: ## Schedule the job to run at a particular time.
    - cron:  '0 1 * * 1' ## every monday at 1:00AM
```

### 💥 Use `severity-cutoff`

Next, we need our scheduled task to fail if a critical vulnerability has been discovered.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kyimhrwa1qhhabmzv82t.png)

Find below `severity-cutoff` implementation : 

```yaml
jobs:
  scan:
    name: 🛡️ Scan image latest
    runs-on: ubuntu-latest
    steps:
      - uses: anchore/scan-action@v3
        id: scan
        with:
         image: optnc/domaine-nc-api:latest
         fail-build: true
         severity-cutoff: critical
```

### 🎫 Create (or update) issue

Next we want to create an issue in case of Scan Action failure (meaning that a `critical` security issue has been found).

What we want is to get properly tagged issues so we can manage them as part of our daily tasks and produce reporting.

Therefore we : 

- Setup some [labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) (so it makes filtering easier), eg : `security`, `docker-scan'`
- Get the ref to the latest opened issue that matches these specific label **so issues are updated instead of getting tons of issues targetting the same issue everyday**
- Get the scan report and put it in the issue **so all elements are available at a single place**

Find the code below :

```yaml
 - name: Create/Update an issue of vulnerabilities 🛡️ that have been detected
        if: ${{ failure() }}
        uses: actions/github-script@v6
        with:
          debug: true
          script: |
            const { owner, repo } = context.repo;
            const labels = ['security', 'docker-scan', 'Alert : Docker image scan'];
            
            // récupération de l'id de la dernière issue (si existante)
            const existingIssue = (await github.paginate(github.rest.issues.listForRepo.endpoint.merge({
              owner, repo, state: 'open',labels
            }))).filter(i => i.title.indexOf('Docker image security scan') !== -1)[0];
            
            // création ou modification de l'issue
            const body = `Workflow failed for commit ${{github.sha}}.        
            
            Following vulnerabilities have been detected :
            \`\`\`
            ${{ steps.scan_report.outputs.report }}
            \`\`\`
                `;
            
            if (existingIssue) {
              github.rest.issues.update({ owner, repo, issue_number: existingIssue.number, body });
            } else {
              github.rest.issues.create({
                owner, repo,
                title : '🛡️ Docker image security scan failed 🛡️',
                body,
                labels
              });
            }
```

### 👮 Enjoy a clean issue

Then you are setup to get very useful issue from your CI :

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8t6z0cf9kdv6s8e8gzyi.png)

### 🎀 Bonus 

Pay good attention to the fact that issue is related to commit which is really useful to follow how the security flaw may have been introduced too : 

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/98cxoz8oyok6zfzvsxgz.png)


## 🔖 Resources

-  [`Anchore Container Scan` on GitHub marketplace](https://github.com/marketplace/actions/anchore-container-scan)
- [`Anchore Container Scan` sourcecode on GitHub](https://github.com/anchore/scan-action)

{% embed https://dev.to/optnc/bench-and-choose-java-8-docker-images-with-anchoregrype-4fg8 %}