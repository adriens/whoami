---
name: chocolatey-ytt
url: https://github.com/adriens/chocolatey-ytt
description: "Chocolatey package source code for ytt"
language: PowerShell
topics: [k8s, yaml, yml, templates, templating, configuration, lint, testing, kubernetes, chocolatey]
stars: 1
created_at: 2020-11-14
updated_at: 2021-11-20
archived: false
has_readme: true
---

[![Build status](https://ci.appveyor.com/api/projects/status/bx5ilrwq7i59t0ob?svg=true)](https://ci.appveyor.com/project/adriens/chocolatey-ytt)
[![Chocolatey](https://img.shields.io/chocolatey/v/ytt.svg)](https://chocolatey.org/packages/ytt)
[![Chocolatey](https://img.shields.io/chocolatey/dt/ytt.svg)](https://chocolatey.org/packages/ytt)

![Twitter Follow](https://img.shields.io/twitter/follow/carvel_dev?label=Follow%20Carvel.dev&style=social)

![Project banner](choco-ytt-banner.png)


# Usage

To install `ytt` and get an optimal experience on windows, just:

- [x] :cinema:[Discover `ytt` in video](https://youtu.be/KbB5tI_g3bo)
- [x] Follow classic choco [instructions](https://chocolatey.org/packages/ytt/) to install/upgrade
- [x] Install [ytt VS Code extension](https://marketplace.visualstudio.com/items?itemName=ewrenn.vscode-ytt)
- [x] :newspaper: Follow [carvel.dev on Twitter (formerly k14s)](https://twitter.com/carvel_dev)
- [x] :star: Star and follow [k14s organization and repos](https://github.com/vmware-tanzu/carvel)
- [x] :book: Read the [VMWare Tanzu article that introduces k14s aka. Kubernetes Tools](https://tanzu.vmware.com/content/blog/introducing-k14s-kubernetes-tools-simple-and-composable-tools-for-application-deployment) why ytt has been created
- [x] :rocket:Discover [VMWare Open Source Program Office](http://vmware.github.io/)
- [x] :smiley_cat: Enjoy

# For developers only section

## Build locally

```
git clone https://github.com/adriens/chocolatey-ytt.git
cd chocolatey-ytt
ant make
```