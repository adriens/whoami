---
name: schemacrawler-snapcraft
url: https://github.com/adriens/schemacrawler-snapcraft
description: "A first attempt to create a java snap package"
language: Shell
topics: []
stars: 4
created_at: 2018-11-01
updated_at: 2025-04-13
archived: false
has_readme: true
---

[![Build Status](https://travis-ci.org/adriens/schemacrawler-snapcraft.svg?branch=master)](https://travis-ci.org/adriens/schemacrawler-snapcraft)
[![Snap Status](https://build.snapcraft.io/badge/adriens/schemacrawler-snapcraft.svg)](https://build.snapcraft.io/user/adriens/schemacrawler-snapcraft)

```
vagrant up
vagrant ssh
# In the box that has been provosionned by docker
cd /snapcraft/
sudo docker run -v $(pwd):/my-snap snapcore/snapcraft sh -c "cd /my-snap && snapcraft"
# Manually install the snap
sudo snap install schemacrawler_0.1_amd64.snap --force-dangerous
```