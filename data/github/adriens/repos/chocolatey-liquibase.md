---
name: chocolatey-liquibase
url: https://github.com/adriens/chocolatey-liquibase
description: "Liquibase Chocolatey package sources"
language: 
topics: [liquibase, chocolatey, db, database, change-management, windows, devops, devops-tools]
stars: 0
created_at: 2019-02-16
updated_at: 2023-07-17
archived: false
has_readme: true
---

[![Build status](https://ci.appveyor.com/api/projects/status/3avdga24cmxict48?svg=true)](https://ci.appveyor.com/project/adriens/chocolatey-liquibase)
[![Chocolatey](https://img.shields.io/chocolatey/v/liquibase.svg)](https://chocolatey.org/packages/liquibase)
[![Chocolatey](https://img.shields.io/chocolatey/dt/liquibase.svg)](https://chocolatey.org/packages/liquibase)


# Liquibase chocolatey package

The aim of this project is to make the release process of liquibase package as easy and fast as possible so it will stay as close as possible from Liquibase release pipe.

## Continous build

1. Update Liquibase version in `liquibase.properties`
2. Run `ant make`
3. Try local install : `choco install -fdv liquibase.nuspec`
4. Run liquibase : `liquibase --version` then `liquibase --help`
5. You are done : make a Pull Request (all required files have been generated
with all requireds fields, including checksums) : ***tools and `nuspec` only***