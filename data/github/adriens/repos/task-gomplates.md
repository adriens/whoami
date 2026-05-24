---
name: task-gomplates
url: https://github.com/adriens/task-gomplates
description: "Ready-to-use gomplate templates to use around `Task` `yaml` files"
language: 
topics: [automation, documentation, golang, gomplate, markdown, mermaid, mermaid-diagrams, mermaidjs, template]
stars: 1
created_at: 2025-11-12
updated_at: 2026-03-09
archived: false
has_readme: true
---

[![Build with Taskfile.dev](https://img.shields.io/badge/build%20with-Taskfile.dev-blue?logo=task)](https://taskfile.dev/)

# ❔ About

Ready-to-use template to use around `Task` `yaml` files


## Generate a Markdown/ Mermaid Report from a Taskfile with gomplate

Download the template:

```sh
curl -o task-to-md-mermaid.gomplate \
	https://raw.githubusercontent.com/adriens/task-gomplates/main/tmpl/task-to-md-mermaid.gomplate
```

Generate the Markdown report

Use gomplate to transform the Taskfile into Markdown:

```sh
gomplate -f task-to-md-mermaid.gomplate -d tasks=Taskfile.yml > Taskfile.md
```

- `-f`: specifies the template file to use
- `-d tasks=Taskfile.yml`: loads `Taskfile.yml` as a datasource named `tasks`
- `> Taskfile.md`: writes the output to the Markdown file

---

You can then open `Taskfile.md` in a Markdown editor that supports Mermaid to view the diagram and the task table.

# 🕹️ Give it  a try

Let's generate the documentaton of the build of Task website : 

I gave it a try on your [taskfile (website)](https://github.com/go-task/task/blob/main/website/Taskfile.yml) : 

1. **Download the Taskfile and the template file**

```sh
# Download the Taskfile
curl -L https://github.com/go-task/task/raw/main/website/Taskfile.yml \
	-o Taskfile.yml

# Download the gomplate template
curl -L \
  https://github.com/adriens/task-gomplates/raw/main/tmpl/task-to-md-mermaid.gomplate \
  -o task-to-md-mermaid.gomplate
```


2. **Generate the Markdown Documentation**

```sh
gomplate -f task-to-md-mermaid.gomplate -d tasks=Taskfile.yml > Taskfile.md
```

3. **🙌 Enjoy**

Open the markdown in a GH issue.