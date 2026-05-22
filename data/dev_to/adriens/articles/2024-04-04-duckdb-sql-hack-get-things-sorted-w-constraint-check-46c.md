---
comments: 2
id: 1806819
is_dev_challenge: false
published_at: '2024-04-04T21:03:50Z'
reactions: 2
reading_time_minutes: 3
tags:
- sql
- programming
- database
- productivity
title: '🪄 DuckDB sql hack : get things SORTED w/ constraint CHECK'
url: https://dev.to/adriens/duckdb-sql-hack-get-things-sorted-w-constraint-check-46c
---

## 🪝 Intro

Ever wanted to get that kind on constraint on a table :

```sql
CREATE TABLE sensor_data(
   ts TIMESTAMP,
   measurement INTEGER,
   ...,
   SORTED(ts)
);
```

Well, it turns out this topic has a dedicated discussion:

[![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/94kmoc5azbdqcdi95n23.png)](https://github.com/duckdb/duckdb/discussions/8444)

For now it's not implemented...yet. But we have a lot of use cases out there.

**Let's see how to achieve this in pure `sql`... and why it would be so useful.**

## 🍿 Demo

{% youtube kfePcOUojeY %}

## 🤔 (A bit of) Context

We are currently using `duckdb` on GitHub Actions (see [`opt-nc/setup-duckdb-action`](https://github.com/marketplace/actions/duckdb-setup)) as it's a very convenient and efficient way to check data quality with `sql` as part of our CI... **with very very few efforts**, see below:

{% embed https://dev.to/optnc/effortless-data-quality-wduckdb-on-github-2mkb %}

**☝️ Recently, we also felt the need to keep a `csv` file sorted according to a given column to keep it as clean as possible** and letting people make Pull Requests... and, most important :  **delegating the CI the role to explain the end user why the data he wants to put cannot be merged.**

We did not want any human in the loop to moderate contributors and explain how the data should be provided to get the PR merged. In particular in the context of we use [GH auto-merge](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) to 

> "[...] increase development velocity by enabling auto-merge for a pull request so that the pull request will merge automatically when all merge requirements are met."

**👉 This productivity hack is all about achieving that in pure `sql`**... and take profit of:

- `duckdb` columnar storage format (see [Exploring DuckDB and the Columnar Advantage](https://medium.com/@zujkanovic/exploring-duckdb-and-the-columnar-advantage-f7beb8cbf478) for more)
- [`CHECK` constraint](https://duckdb.org/docs/sql/constraints.html#check-constraint)

**ℹ️ Notice that this hack can be applied on very large volumes of data.**
 
## 🪄 `sql` tricks


```sql
-----------------------------------------------------------
--
-- Check if a table column is sorted w/ integrity check
--
-----------------------------------------------------------

-- Create a table with a column that is not sorted
-- Feed some random stuff
-- The real target table
create or replace table demo_sort (text varchar);

insert into demo_sort values ('DuckDb');
insert into demo_sort values ('duckdb');
insert into demo_sort values ('Duckdb');
insert into demo_sort values ('DUCKDB');
insert into demo_sort values ('duckDB');
insert into demo_sort values ('DUCKdb');
insert into demo_sort values ('DuckDB');

-- Check the resulting table
from demo_sort;


-- Prepare test environment
CREATE SEQUENCE seq_original START 1;
CREATE SEQUENCE seq_sorted START 1;

create or replace temp table orig_table as
    select nextval('seq_original') as index,
text from demo_sort;

create or replace temp table sorted_table as
    select nextval('seq_sorted') as index,
    text
    from (select text from demo_sort order by text);

-- Check the resulting tables
from orig_table;
from sorted_table;

-- Create the table that compares the sorted and original tables columns
create or replace temp table test_table(orig_text varchar,
                                    orig_index integer,
                                    sorted_index integer
                                    -- the magic part XD
                                    check(orig_index = sorted_index)
                                    );
-- Populate the comparison table
insert into test_table
    select 
        orig_table.text as orig_text,
        orig_table.index as orig_index,
        sorted_table.index as sorted_index,
    from
        orig_table,
        sorted_table
    where
        orig_table.text = sorted_table.text
    order by orig_table.index;

-- Enjoy the resulting "Constraint Error: CHECK constraint failed: test_table"
```

## 🔖 Resources

- [`opt-nc/setup-duckdb-action`](https://github.com/marketplace/actions/duckdb-setup)
- [🪄 DuckDB sql hack : get things SORTED (jupysql)](https://www.kaggle.com/code/adriensales/duckdb-sql-hack-get-things-sorted-jupysql/notebook)
- [Automatically merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request)
- [Exploring DuckDB and the Columnar Advantage](https://medium.com/@zujkanovic/exploring-duckdb-and-the-columnar-advantage-f7beb8cbf478)
- [Why DuckDB](https://duckdb.org/why_duckdb.html)