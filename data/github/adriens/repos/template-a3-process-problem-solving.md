---
name: template-a3-process-problem-solving
url: https://github.com/adriens/template-a3-process-problem-solving
description: "A markdown ePub template to help around \"A3 Process and Problem Solving\""
language: CSS
topics: []
stars: 0
created_at: 2023-10-29
updated_at: 2023-10-30
archived: false
has_readme: true
---

[![xc compatible](https://xcfile.dev/badge.svg)](https://xcfile.dev)

# ❔ About

The aim of this repo is to provide a set of ready-to-use markdown files, packaged in a way
anyone can build and share an ePub version with no or no effort.

# 🤗 Project philosphy

The idea behind this project is to: 

> **put together collaborative A3 LEAN tool and `git` collaborative together**

on a same automtable pipeline (w/ issues, pull requests, release automation, issues, discussions) all on a same
and highly integrable platform.

# 🚀 Getting started

1. Install [`pandoc`](https://pandoc.org/installing.html)
2. Install [`xc`](https://xcfile.dev/getting-started/#installation)
3. [Create a repo from this template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
4. Go the directory of the repo
5. Modify some `markdowns` with your team
6. Run `xc` to enjoy ready to use tasks
7. Build the `ePub`
8. Enjoy Team work

# 🦥 Getting started vor very lazy nerds

In this section, you'll be able to create your own repo from scratch and prepare a lot of resources.

## 🏁 Prerequisites

First, install the proper [`gh-milestone`](https://github.com/valeriobelli/gh-milestone) gh extension:

```sh
# https://github.com/valeriobelli/gh-milestone
gh extension install valeriobelli/gh-milestone
```

... then customize your env:

```sh
echo -n "Please enter your TARGET_OWNER: "
read TARGET_OWNER
echo "TARGET_OWNER: $TARGET_OWNER"
```

```sh
echo -n "Please enter your TARGET_REPO: "
read TARGET_REPO
echo "TARGET_REPO: $TARGET_REPO"
```

You're ready to go

## 🚀 Feed your repo

Just run the following script as is:

```sh
# Create and locally clone repo
gh repo create $TARGET_OWNER/$TARGET_REPO --template adriens/template-a3-process-problem-solving --private --clone
cd $TARGET_REPO
```

Now, prepare the repo

```sh
# Initialize the repo w/ issues, labels, milestones...
xc feed
```
## Tasks

### feed
Prepare labels, milestones and standard issues.

```shell
# Setup a but more the repo
# Add topics for better indexations
gh repo edit --add-topic lean
gh repo edit --add-topic problem-solving

gh repo edit --description "A3 lean tool repo"
gh repo edit --enable-discussions
gh repo edit --enable-wiki=false

# Create dedicated milestone so you get a completion staus
gh milestone create --title Plan --description "Initial phase of planning and identifying solutions in a continuous improvement process."
gh milestone create --title Do --description "Implementation or execution of the plan formulated in the "Plan" phase, where actions are taken according to the plan to address the identified problem or to implement the proposed changes or improvements."
gh milestone create --title Check --description "assessing and evaluating the results of the implemented actions (Do phase) against the initially set objectives and expected outcomes to determine if the desired improvements have been achieved and to gather data for decision-making in the subsequent phases."
gh milestone create --title Act --description "Implementing changes based on the results of the "Check" phase, where adjustments and improvements are made to processes or systems, solidifying the cycle of continuous improvement."

# Create labels : one label per phase
gh label create "PDCA:Plan" --description "Planning phase" --color "d4c5f9"
gh label create "PDCA:Do" --description "Execution phase" --color "d4c5f9"
gh label create "PDCA:Check" --description "Evaluation phase" --color "d4c5f9"
gh label create "PDCA:Act" --description "Standardization phase" --color "d4c5f9"
gh label create "Gemba" --description "Gemba" --color "d4c5f9"

# Create and assign issues
# https://cli.github.com/manual/gh_issue_create

gh issue create --title "1️⃣ Problem Identification" --body "Determining and clearly defining the problem or improvement opportunity." --label "PDCA:Plan" --milestone "Plan"
gh issue pin 1

gh issue create --title "2️⃣ Analysis" --body "Find root cause analysis, and a thorough understanding of the problem" --label "PDCA:Plan" --milestone "Plan"
gh issue create --title "3️⃣ Solution Development" --body "he solution development phase in the A3 format includes generating ideas and possible solutions, as well as planning the steps to be taken."  --label "PDCA:Do" --milestone "Do"
gh issue create --title "4️⃣ Solution Implementation" --body "Where the planned actions are executed to solve the identified problem." --label "PDCA:Do" --milestone "Do"
gh issue create --title "5️⃣ Results Verification" --body "The obtained results are evaluated after implementing the solutions to determine if the problem has been resolved as expected." --label "PDCA:Check" --milestone "Check"
gh issue create --title "6️⃣ Standardization and Follow-up" --body "At this stage, learnings are consolidated, corrective actions are established, and processes are put in place to maintain and improve the changes." --label "PDCA:Act" --milestone "Act"
gh issue pin 6

gh issue create --title "📅 Setup a due date for each Milestone" --body "Setup a due date for each milestone" --label "PDCA:Plan" --milestone "Plan"
gh issue pin 7

gh issue create --title "🔂 Hansei : Reinvest what we learned on other problems" --body "Identify other problems that could benefit of this solution" --label "PDCA:Act" --milestone "Act"
```

### epub
Build the epub version of the A3.

```shell
pandoc --toc\
    --metadata title="A3 LEAN Tool"\
    title.yml\
    01_background.md\
    02_current_conditions.md\
    03_target_conditions.md\
    04_analysis.md\
    05_proposed_countermeasures_implementation_verification_plan.md\
    06_follow_up_plan.md\
    07_result_checks.md\
    08_standardization_and_next_steps.md\
    09_bibliography.md\
    -o A3_Lean_Tool.epub
```

### docx
Build the docx version of the A3.

```shell
pandoc --toc\
    --metadata title="A3 LEAN Tool"\
    title.yml\
    01_background.md\
    02_current_conditions.md\
    03_target_conditions.md\
    04_analysis.md\
    05_proposed_countermeasures_implementation_verification_plan.md\
    06_follow_up_plan.md\
    07_result_checks.md\
    08_standardization_and_next_steps.md\
    09_bibliography.md\
    -o A3_Lean_Tool.docx
```

### view
Open the repo in the web browser.

```shell
gh repo view --web
```