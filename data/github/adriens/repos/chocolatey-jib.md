---
name: chocolatey-jib
url: https://github.com/adriens/chocolatey-jib
description: "Chocolatey package for Jib CLI"
language: 
topics: []
stars: 0
created_at: 2021-04-04
updated_at: 2021-11-14
archived: false
has_readme: true
---

[![Build status](https://ci.appveyor.com/api/projects/status/uucur42l1y8ybige?svg=true)](https://ci.appveyor.com/project/adriens/chocolatey-jib)

[![Chocolatey](https://img.shields.io/chocolatey/v/jib.svg)](https://chocolatey.org/packages/jib)
[![Chocolatey](https://img.shields.io/chocolatey/dt/jib.svg)](https://chocolatey.org/packages/jib)


# chocolatey-jib

[Chocolatey](https://chocolatey.org)  package source to install [Jib CLI](https://github.com/GoogleContainerTools/jib/tree/master/jib-cli). More details about this project on this [medium article](https://medium.com/curiosity-driven-development/how-to-dockerize-a-spring-boot-app-with-googles-jib-53dcac56a2e1).

# Prerequisite

Have [chocolatey](https://chocolatey.org/) [properly installed](https://chocolatey.org/install) and web access.


# Install from choco repo

To install `Jib CLI`, simply run, with ```Administrator``` privileges :

```
choco install jib
```

Uninstall package :

```
choco uninstall jib
```


# Build and install commands

With ```Administrator privileges```, run a ```cmd``` shell.

Uninstall package :

```
choco uninstall jib
```

Manually build and install the package from the source :

```
choco install -fdv jib.nuspec
```

Push the package to central [package repository](https://chocolatey.org/packages) : check prepared `ant` tasks.

# For developers

For developers, take a look at the ```ant``` build tasks used to automate package compile and build.

Upgrade process:

1. Upgrade verion un properties file
2. `ant make`
3. Install locally `choco install -fdv jib.nuspec`
4. Test command line `jib --version`