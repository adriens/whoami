---
comments: 2
id: 1954332
is_dev_challenge: false
published_at: '2024-08-19T20:56:16Z'
reactions: 2
reading_time_minutes: 3
tags:
- database
- postgres
- dataengineering
- tutorial
title: 🦆 💏 🐘 Let PostgreSQL & duckdb "sql" together
url: https://dev.to/adriens/let-postgresql-duckdb-sql-together-183o
---

## ❔ About

So you're both a - maybe early - PostgreSQL fan... and a recent `duckdb` adopter.
You like both databases for their **strengths and ecosystems**... and wonder how it would be

> possible to seamlessly send data from/to each other databases... without having to code anything, I mean **nothing more that playing  `sql shell` commands in a terminal**

: no Python, no Java,...

👉 Well this is exactly what I will talk about in this post thanks to :

- [PostgreSQL Import](https://duckdb.org/docs/guides/database_integration/postgres.html)
- [PostgreSQL Extension](https://duckdb.org/docs/extensions/postgres.html)
- [Querying Postgres Tables Directly From DuckDB](https://duckdb.org/2022/09/30/postgres-scanner.html)

## 🤔 ... but why this post ?

The 3 main reasons of this article and why to pull/put from `PostgreSQL`/`duckdb` at this point are : 

|                    |  `DuckDB`         | `PostgreSQL`        |
| -------------------| ----------------- | ------------------- |
| **Database Model** | Columnar database | Relational database |
| **License**        | MIT               | BSD like            |
| **Serverless**     | Yes               | No                  |        


## 🎯 What we'll do

We will, only from terminal : 

1. **🐋 Install & boot** a containerized PostgreSQL database (with Podman)
2. **🐘  Create** a database
3. **🔁 Create and feed** a little table
4. **🪄 Read the `psql` table** from `duckdb`
5. **🗜️ Export the `psql` table** to a parquet file
6. **🔬 Inspect `parquet`** file with [`parquet-cli`](https://github.com/chhantyal/parquet-cli)

Also we will do the **reverse move** : 

1. Create a table in PostgreSQL from within `duckdb`
2. Test table contents from `sql`

## 🍿 Demo

{% youtube 2TX8xjZkrz8 %}

## 📜 `shell` scripts

Install & boot a PostgreSQL instance:

```shell
export PGPASSWORD=mysecretpassword

# Boot a postgresql instance
podman run --name postgres -e POSTGRES_PASSWORD=$PGPASSWORD -d\
    -p 5432:5432 docker.io/library/postgres

# Check container status
podman ps -a
```

Install `psql` so we can reach PostgrSQL from outside the contenair:

```shell
# Install `psql` on the host so the database can be accessed
# from outside de container
sudo apt install -y postgresql-client
```

Now, create some PostgreSQL objects:

```shell
# Create a demo database
psql -h localhost -p 5432 -U postgres -c "CREATE DATABASE demo;"

# Create a table
psql -h localhost -p 5432 -U postgres -d demo\
    -c "CREATE table customers(id varchar primary key);"

# Feed the PostgreSQL table with some data
psql -h localhost -p 5432 -U postgres -d demo\
    -c "insert into customers values \
    ('Duffy duck'),\
    ('Daisy Duck'),\
    ('Donald Duck'),\
    ('Ludwig Von Drake');"
```

Install `duckdb` :

```shell
# (Quick and dirty) duckdb install
wget https://github.com/duckdb/duckdb/releases/download/v1.0.0/duckdb_cli-linux-amd64.zip
unzip duckdb_cli-linux-amd64.zip
cp duckdb /usr/bin/
rm duckdb duckdb_cli-linux-amd64.zip
```

Now do the fun stuff...

### Reach PostgreSQL database from `duckdb`

Let's reach postgres database from `duckdb` : 

```shell
duckdb -c "ATTACH 'dbname=demo user=postgres password=mysecretpassword host=127.0.0.1'\
    AS db (TYPE POSTGRES, READ_ONLY);
show all tables;
select * from db.customers;
COPY db.customers TO 'db.customers.parquet' (FORMAT PARQUET);"
```

... then check the output `parquet` file:

```shell
ls -ltr
file db.customers.parquet
```

... and read the resulting `parquet` file from `duckdb` : 

```shell
duckdb -c "select * from 'db.customers.parquet';"
```

Test resulting `parquet` file with `parquet-cli` : 

```shell
pip install parquet-cli
parq -h

parq db.customers.parquet --count
parq db.customers.parquet --head
parq db.customers.parquet --tail
```

### `duckdb` ➡️ `PostgreSQL`

Let's:

1. **_"Attach"_** the remote PostgreSQL instance from `duckdb` runtime
2. **Create** a table
3. **Feed** the table
4. **Select** table contents from `psql`

```shell
duckdb -c "ATTACH 'dbname=demo user=postgres password=mysecretpassword host=127.0.0.1'\
    AS db (TYPE POSTGRES);\
    create table db.heroes(name varchar primary key);\
    insert into db.heroes values\
        ('Dumbo'),\
        ('Man-Elephant'),\
        ('Tantra'),\
        ('Elephant Man'),\
        ('The Elephantmen'),\
        ('Mammomax') ;
"

psql -h localhost -p 5432 -U postgres -d demo\
    -c "select * from heroes;"
```

## ⚖️ More about `DuckDB` vs `PostgreSQL`

See below this very synthetic breakdown from [influxdata](https://www.influxdata.com/comparison/duckdb-vs-postgres/): 

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/3yh5w8ns34jycsayxdxe.png)](https://www.influxdata.com/comparison/duckdb-vs-postgres/)
