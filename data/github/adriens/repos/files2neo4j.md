---
name: files2neo4j
url: https://github.com/adriens/files2neo4j
description: "Dummy tool to generate a neo4j graph database from a a directory"
language: Java
topics: []
stars: 0
created_at: 2016-08-23
updated_at: 2016-08-23
archived: false
has_readme: true
---

# files2neo4j
Dummy tool to generate a neo4j graph database from a a directory

# Howto

Generate the output neo4j database.

Configure the NEO4J_HOME/conf/neo4j.conf

Example :

```
#*****************************************************************
# Neo4j configuration
#*****************************************************************

# The name of the database to mount
dbms.active_database=filesReport.db

# Paths of directories in the installation.
dbms.directories.data=/home/salad74/neo4j/
```

Take care to generate the output neo4j database
in ```/home/salad74/neo4j/databases/filesReport.db``` otherwise it not be taken in
account by bneo4j.

Stop the neo4j process
Run the report
Start the neo4j
Enjoy with browser