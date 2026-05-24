---
name: odata-eaux-baignade-noumea
url: https://github.com/adriens/odata-eaux-baignade-noumea
description: "Experience Open Data de la qualité des eaux de baignade à Nouméa, Nouvelle-calédonie"
language: 
topics: [csv, csv-files, datascience, duckdb, kaggle, newcaledonia, noumea, nouvelle-caledonie, opendata, python]
stars: 0
created_at: 2023-03-09
updated_at: 2023-06-17
archived: false
has_readme: true
---

# ❔ About

See https://www.kaggle.com/code/adriensales/la-qualit-des-eaux-de-baignade-noum-a

# ⚡ For impatients

Just run the following script in any shell and enjoy:

```shell
#!/bin/sh
# Diplay latest flags
sh <(curl https://tea.xyz) +duckdb.org \
duckdb << EOF
INSTALL httpfs;
LOAD httpfs;
select plage,
    flag_color,
    case 
        when (flag_color = 'BLUE')      THEN '🟦'
        when (flag_color = 'YELLOW')    THEN '🟨'
        when (flag_color = 'RED')       THEN '🟥'
    end as flag_color
from read_csv_auto('https://bit.ly/3ZCJ1X5') as latest;
EOF

```


# 🦆 `DuckDb` hacks

First, install duckdb (`brew install duckdb`) or [`install_duckdb.sh`](https://gist.github.com/adriens/74a2fd8adc6fd508d970bc1cb2419395)

```sql
INSTALL httpfs;
LOAD httpfs;
.prompt "🦆 🏖️  > "
select * 
from 'https://raw.githubusercontent.com/adriens/odata-eaux-baignade-noumea/main/data/latest.csv';
```

```sql
INSTALL httpfs;
LOAD httpfs;
.prompt "🦆 🏖️  > "
select *
from 'https://raw.githubusercontent.com/adriens/odata-eaux-baignade-noumea/main/data/historic.csv';
```

You can also use (nicer) short urls : 

```shell
duckdb << EOF
-- historic
INSTALL httpfs;
LOAD httpfs;
select *
from
read_csv_auto('https://bit.ly/3mAUIPr') as historic;
EOF
```

```shell
duckdb << EOF
-- historic
INSTALL httpfs;
LOAD httpfs;
select *
from read_csv_auto('https://bit.ly/3ZCJ1X5') as latest;
EOF
```
## Tasks

Below some [`xc`](https://xcfile.dev/) ready tasks. 
Just type `xc`.

### latest
Print the latest status of all beaches

```shell
#!/bin/sh
# Diplay latest flags
sh <(curl https://tea.xyz) +duckdb.org \
duckdb << EOF
INSTALL httpfs;
LOAD httpfs;
select plage,
    flag_color,
    case 
        when (flag_color = 'BLUE')      THEN '🟦'
        when (flag_color = 'YELLOW')    THEN '🟨'
        when (flag_color = 'RED')       THEN '🟥'
    end as flag_color
from read_csv_auto('https://bit.ly/3ZCJ1X5') as latest;
EOF

```

### last-20
Print the 20 last status of all beaches

```shell
#!/bin/sh
# Print the 20 last status of all beaches
sh <(curl https://tea.xyz) +duckdb.org \
duckdb << EOF
INSTALL httpfs;
LOAD httpfs;
select date, plage,
    case 
        when (flag_color = 'BLUE')      THEN '🟦'
        when (flag_color = 'YELLOW')    THEN '🟨'
        when (flag_color = 'RED')       THEN '🟥'
    end as flag
from
read_csv_auto('https://bit.ly/3mAUIPr')
order by date desc
limit 10;
EOF
```

### baignade-autorisee

cf [Dates d'interdiction d'activités nautiques à Nouméa](https://www.nouvellecaledonie.travel/interdiction-activites-nautiques-noumea/)

```shell
#!/bin/sh
sh <(curl https://tea.xyz) +duckdb.org \
duckdb << EOF
INSTALL httpfs;
LOAD httpfs;
select
    case
        when count(*) > 0 then '👎'
        else '👍'
    end is_baignade_autorisee
from read_csv_auto('https://bit.ly/3JJCZhJ')
where
    current_date >= date_debut and
    current_date <= date_fin;
EOF
```