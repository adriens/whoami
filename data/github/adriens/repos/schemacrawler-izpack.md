---
name: schemacrawler-izpack
url: https://github.com/adriens/schemacrawler-izpack
description: "Izpack installer for schemacrawler. Primary target is Windows."
language: HTML
topics: []
stars: 0
created_at: 2014-11-10
updated_at: 2016-04-15
archived: false
has_readme: true
---

[![Build Status](https://travis-ci.org/adriens/schemacrawler-izpack.svg?branch=master)](https://travis-ci.org/adriens/schemacrawler-izpack) [![Dependency Status](https://www.versioneye.com/user/projects/570ed124fcd19a0045440c30/badge.svg?style=flat)](https://www.versioneye.com/user/projects/570ed124fcd19a0045440c30)

Schemacrawler Izpack package builder
==========================================

About
------------------------------------------

The main purpose of this package is to build a nice to use Windows installer,
based on Izpack which bundles commonly drivers.

debian users may rather (as my self) the dedicated .deb installer (see https://github.com/adriens/schemacrawler-deb).

This installer is indeed designed to work on unix and windows systems, still my
efforts are for now focused on the Windows one.

Build
------------------------------------------

    git clone https://github.com/adriens/schemacrawler-izpack.git
    cd schemacrawler-izpack
    mvn install:install-file -Dfile=lib/sqlite-jdbc-3.7.8.jar -DgroupId=org.xerial -DartifactId=sqlite-jdbc -Dversion=3.7.8 -Dpackaging=jar
    mvn clean site package

This is it : the installer has been built (as well as documentation site un target/site/index.html).


Install from command line (with GUI)
------------------------------------------

`java -jar target/schemacrawler-lzpack-${version}`

Install from command line (no GUI, console only)
------------------------------------------

`java -jar target/schemacrawler-lzpack-${version} -console`


Install from Graphical environment
------------------------------------------

Just double-click schemacrawler-lzpack-${version}.jar`

Install from text console
------------------------------------------

`java -jar target/schemacrawler-lzpack-${version} -console`


Uninstall
------------------------------------------

Run the Izpack generated uninstaller in Uninstaller directory.


TODO
------------------------------------------

Ensure mac has minimal support.