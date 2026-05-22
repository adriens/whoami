---
duration_seconds: 919
id: 5Sra-Yqn_Xs
likes: 2
published_at: '2025-02-22'
tags: []
title: Analyse post Emeutes 2024 avec emploi.gouv.nc depuis le terminal avec duckdb
  et parquet
url: https://youtu.be/5Sra-Yqn_Xs
views: 44
---

- 00:00 : Intro & context
- 02:15 : About the parquet export on data.gouv.nc
- 03:06 : Enjoying the parquet file with duckdb and build something
- 09:00 : Pivoting data with duckdb
- 11:59 : Doing data analysis
- 13:51 : Conclusion

#SQL  below:

```sql
create or replace view report as
    select
        substring(numero, 1, 7) as year_month,
        typecontrat,
        count(*) as nb_offres
    from 'historique_emploi_gouv_nc.parquet'
    where
        year_month like '2024%' or
        year_month like '2025%'
    group by all
    order by year_month desc;

pivot report
on typecontrat
using sum(nb_offres)
order by year_month desc;
```