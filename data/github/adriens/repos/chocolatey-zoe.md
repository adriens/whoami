---
name: chocolatey-zoe
url: https://github.com/adriens/chocolatey-zoe
description: "Chocolatey package for Zoe (the Kafka cli)"
language: 
topics: []
stars: 0
created_at: 2021-07-17
updated_at: 2021-11-05
archived: false
has_readme: true
---

[![Build status](https://ci.appveyor.com/api/projects/status/9q0etvjntfvth34b?svg=true)](https://ci.appveyor.com/project/adriens/chocolatey-zoe)
[![Chocolatey](https://img.shields.io/chocolatey/v/zoe.svg)](https://chocolatey.org/packages/zoe)
[![Chocolatey](https://img.shields.io/chocolatey/dt/zoe.svg)](https://chocolatey.org/packages/zoe)


# chocolatey-zoe

[Chocolatey](https://chocolatey.org) package source to install [zoe](https://adevinta.github.io/zoe/).

# About Zoe

Zoe is a command line tool to interact with kafka in an easy and intuitive way. Wanna see this in action ? check out
this demo...

[![demo](https://asciinema.org/a/vSDNcUUaMMBkWxCSDD8u3s0No.svg)](https://asciinema.org/a/vSDNcUUaMMBkWxCSDD8u3s0No?speed=2.5&rows=35)

# Zoe resources

Here are the resources that made me adopt Zoe... and write a [chocolatey package](https://community.chocolatey.org/packages/zoe/) to help Windows collaborators install it easier :

- [Dedicated Medium article](https://medium.com/adevinta-tech-blog/zoe-the-kafka-cli-for-humans-3e01584d0d3f)
- The [Dedicated KataCoda Course](https://www.katacoda.com/wlezzar/courses/zoe)
- Of course [official GH repo](https://github.com/adevinta/zoe)
- [Zoe's Official website](https://adevinta.github.io/zoe/)

Hopefully you'll enjoy this tools as much as I do.


# Zoe install on Windows

Now, the install process on windows is as easy as :

```
sdk install java
choco install zoe
```

# Prerequisite

Have [chocolatey](https://chocolatey.org/) [properly installed](https://chocolatey.org/install) and web access.


# Install from choco repo

To install schemacrawler, simply run, with ```Administrator``` privileges :

```
choco install zoe
```

Uninstall package :

```
choco uninstall zoe
```




# Build and install commands

With ```Administrator privileges```, run a ```cmd``` shell.

Uninstall package :

```
choco uninstall zoe
```

Manually build and install the package from the source :

```
choco install -fdv zoe.nuspec
```

Push the package to central [package repository](https://chocolatey.org/packages) : check prepared `ant` tasks.

# For developers

For developers, take a look at the ```ant``` build tasks used to automate package compile and build.

Upgrade process:

1. Upgrade verion un properties file
2. `ant make`
3. Install locally `choco install -fdv zoe.nuspec`
4. Test command line `zoe --version`

# For maintainers

**NB : Ths section explains how to release new zoe versions.**

The whole chocolatey process has been automated, hence, releaing a new version requires very vew efforts :

1. Change targte version in `zoe.properties`
2. Push the commit to the master branch to see if it builds the right way : [check Appveyor](https://ci.appveyor.com/project/adriens/chocolatey-zoe) badge for that
3. To push the release to chocolatey, simply create a release on this GH repo and wait for [AppVeyor](https://ci.appveyor.com/project/adriens/chocolatey-zoe) to end
4. Let chocolatey moderation do the job, and update the progress on the [release pipe project](https://github.com/adriens/chocolatey-zoe/projects/1)
5. On each choco moderation step, {keep the issue up-to-date](https://github.com/adriens/chocolatey-zoe/issues/2) so you keep track of the moderation processs