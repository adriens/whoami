---
comments: 4
id: 2823283
is_dev_challenge: false
published_at: '2025-09-08T04:02:44Z'
reactions: 2
reading_time_minutes: 2
tags:
- devops
- ci
- database
- productivity
title: 🛡️ Data quality, SQL, duckdb and http_client on CI🦆
url: https://dev.to/adriens/data-quality-sql-duckdb-and-httpclient-on-ci-22
---

## 💭 CI, `duckdb` et and data protection

To efficiently yet effortlessly manage data quality, we created a GitHub Action to install `duckdb` : 

{% embed https://dev.to/optnc/effortless-data-quality-wduckdb-on-github-2mkb %}

... but recently I had to face an another challenge : as part of our CI, I had the need to validate data... that were relying on web resources.

I needed to **be sure that a GitHub Account was really existing** (for example to avoid typos) as part of our CI.

In this very short article, I'll show how to use DuckDB with the [`http_client`](https://duckdb.org/community_extensions/extensions/http_client.html) extension to verify GitHub handles stored in a table, **for example to lint data as part of a CI pipeline** thanks to [GitHub Duckdb Action](https://github.com/marketplace/actions/duckdb-setup)... and do the job with a very simple `SQL` script and [`CHECK` constraints](https://duckdb.org/docs/stable/sql/constraints.html#check-constraint).

## 🍿 For impatients

{% youtube I6ai5ttKVp8 %}

## 🔖 Resources

- https://github.com/Query-farm/duckdb-extension-httpclient
- https://duckdb.org/community_extensions/extensions/http_client.html
- https://github.com/marketplace/actions/duckdb-setup


## 🕹️ Do the job with `SQL`

First install extension:

```sql
INSTALL http_client FROM community;
LOAD http_client;
```

Then create a table with some example data:

```sql
create or replace table person_gh_member
(
  sam_accountname varchar primary key,
  gh_member varchar not null
);

-- insert rows
INSERT INTO person_gh_member (sam_accountname, gh_member)
values
('adriens', 'adriens'), 
('jdoe', 'johndoe'), 
('asmith', 'annasmithRRRRR');
```

Finally, run a query to check the status of each GitHub handle:

```sql
create or replace view v_person_gh_status as
    select 
    sam_accountname,
    gh_member,
    'https://github.com/' || gh_member as gh_url,
    cast(http_get(gh_url).status as integer) as http_gh_status
    from person_gh_member;
    --where gh_status <> 200;

from v_person_gh_status;
```

Now, to lint, we can add a check to see if any status is not 200:

```sql
from v_person_gh_status
    where http_gh_status <> 200;
```

```sql
create or replace table lint_gh_handle(
    gh_handle varchar primary key,
    gh_url varchar not null unique check (gh_url like 'https://github.com/%'),
    gh_status integer check (gh_status = 200)
);

insert into lint_gh_handle(
            gh_handle,
            gh_url,
            gh_status)
select
    gh_member,
    'https://github.com/' || gh_member as gh_url,
    cast(http_get(gh_url).status as integer) as gh_status
from person_gh_member;
```

