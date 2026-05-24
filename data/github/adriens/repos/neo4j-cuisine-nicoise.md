---
name: neo4j-cuisine-nicoise
url: https://github.com/adriens/neo4j-cuisine-nicoise
description: "Graphe neo4j des recettes et ingrédients de la cuisine niçoise"
language: 
topics: [neo4j, recipes, cypher, recettes, cuisine, graph]
stars: 0
created_at: 2017-09-12
updated_at: 2017-09-13
archived: false
has_readme: true
---

# WARNING

This is a work in progress.

# neo4j-cuisine-nicoise

Graphe neo4j des recettes et ingrédients de la cuisine niçoise. Ce fichier est à charger via ```cypher-shell```. Ce fichier est fait pour
s'entraîner à faire des requêtes cypher et voir un peu comment la cuisine niçoise s'articule autour d'ingrédients clés.

# Ressources

Official tutorial : https://neo4j.com/docs/developer-manual/current/cypher/clauses/match/#match-with-labels

Le livre de référence qui me suit depuis de nombreuses année :

![La bonne cuisine du Comté de Nice, Jacques Médecin](img/couverture-livre.jpg "La bonne cuisine du Comté de Nice, Jacques Médecin, éd. SOLAR ISBN 2-263-02613-4")


# Requêtes utilitaires

Lister les noeuds orphelins (on ne doit pas en avoir) :

```
MATCH (n) WHERE NOT (n)--() RETURN COUNT(n);
```

# Nombre total de recettes

```
MATCH (r:Recette)
RETURN count(*);
```

# Nombre total d'ingrédients

```
MATCH (i:Ingredient)
RETURN count(*);
```

# Requêtes exemples

Supprimer les ingrédients peu intéressants : sel et poivre :

```
// Efface le sel
MATCH (ingredient:Ingredient{ nom: 'Sel' })
DETACH DELETE ingredient;
```

```
// Efface le poivre
MATCH (ingredient:Ingredient{ nom: 'Poivre' })
DETACH DELETE ingredient;
```


Les dix ingrédients les plus référencés dans les recette (plus intéressant dans ```cypher-shell```) :

```
MATCH (n)-[r:INGREDIENT_DE]->(s:Recette)
WITH n as Ingredient, count(r) as nombre
RETURN Ingredient , nombre
ORDER BY nombre DESC
LIMIT 10;
```

Les ingrédients et leur catégories :

```
MATCH (m:Categorie_Alimentaire )-[r]-(n:Ingredient)
RETURN n,m,r;
```

Les top 3 des catégories alimentaires les plus référencées (celles auxquelles un maximum d'ingrédient sont liés) (plus intéressant dans ```cypher-shell```) :

```
MATCH (n:Ingredient)-[r]->(m:Categorie_Alimentaire)
RETURN m.nom as Categorie, COUNT(*) AS nombre
ORDER BY nombre DESC
LIMIT 10;
```

Les ingrédients des 3 catégories d'aliment les plus fournies :

```
MATCH (n:Ingredient)-[r]->(m:Categorie_Alimentaire)
with m as cat, COUNT(*) AS count
ORDER BY count DESC
LIMIT 3
// on a le top 3 des catégories d'aliments les plus grosses
// on sort les relations et les ingrédients liés
match (i:Ingredient)-[r]->(cat)
return i,r,cat;
```



Fréquence de tous les légumes de toutes les recettes

```
MATCH (n:Ingredient)-[r]->(m:Recette)
where (n)-[:EST_DE_FAMILLE]-({ nom: 'Légume' })
with n , count(*) as count
order by count desc
return n.nom, count;
```

Fréquence des catégories alimentaires dans les recettes :

```
MATCH (n:Ingredient)-[r]->(m:Recette)
//where (n)-[:EST_DE_FAMILLE]-({ nom: 'Légume' })
with n , count(*) as count
order by count desc
match (n)-[:EST_DE_FAMILLE]->(c:Categorie_Alimentaire)
with c, count(*) as count
return  c.nom as categorie, count as nombre
order by nombre desc;
```



Les recettes dont rien ne provient des animaux :

```

```



Les 5 légumes les plus utilisés :

```

```


Les plats centraux de la cuisine niçoise (ie. ceux utilisant les ingrédient centraux) :


```

```


Le nombre de fois que deux ingrédients distincts se retrouvent dans une même recette :

```
MATCH (n:Ingredient)-[r:INGREDIENT_DE]->(m:Recette)<-[s:INGREDIENT_DE]-(o:Ingredient)
WITH n as i1, o as i2, count(r) as nombre
where i1.nom = 'Ail' and i1.nom <> o.nom
return i1.nom, i2.nom, nombre 
//order by i1.nom, i2.nom
order by nombre desc
```