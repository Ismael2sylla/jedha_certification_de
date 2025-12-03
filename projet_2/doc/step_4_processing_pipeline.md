# Step 4 — Data Processing Pipeline
## Projet : Amazon Industry Insights — ETL Reviews

---

# **1. Introduction**
Le Step 4 consiste à **mettre en place le pipeline de transformation** qui va traiter les données ingérées dans le Data Lake (RAW → BRONZE → SILVER → GOLD) en utilisant des outils de traitement massif (PySpark, Airflow, Pandas, ou framework choisi).

L’objectif : transformer des données brutes Amazon Reviews en tables proprement structurées, prêtes pour l’analyse et la BI.

Ce document présente :
- la logique de transformation,
- les scripts du pipeline,
- les contrôles qualité,
- les règles métier appliquées,
- les outputs produits par chaque couche.

---

# **2. Architecture du Pipeline de Traitement**
Le pipeline suit un schéma standard Data Engineering à 4 niveaux :

```
RAW → BRONZE → SILVER → GOLD
```

### **Technologies utilisées**
- Python / PySpark (processing)
- AWS S3 (stockage)
- Airflow (orchestration)
- Pandas (tests complémentaires)
- Great Expectations (optionnel)

---

# **3. Traitements RAW → BRONZE**
### 🎯 Objectif : **Nettoyage, validation minimale, typage cohérent**

### **Opérations effectuées :**
- Conversion en Parquet (optimisation stockage)
- Correction des types (int, float, string)
- Conversion dates en format ISO (`yyyy-MM-dd`)
- Nettoyage des valeurs vides (`null`, "")
- Uniformisation du casing (lowercase sur certains champs)
- Suppression des colonnes inutiles

### **Exemple de schéma BRONZE**
```
review_id: string
product_id: string
user_id: string
rating: int
review_body: string
review_date: date
language: string
helpful_votes: int
```

### **Logique de validation**
- Rating ∈ [1,5]
- review_body non vide
- Dates valides
- product_id non nul

Les lignes rejetées sont envoyées dans :
```
rejected/raw_to_bronze/YYYY/MM/DD/batch=<UUID>/
```

---

# **4. Traitements BRONZE → SILVER**
### 🎯 Objectif : enrichissement, normalisation métier, jointures

### **Transformations appliquées :**
- Jointure avec table produits (si fournie)
- Extraction de la longueur du texte : `review_length`
- Feature engineering :
  - nombre de mots
  - détection langue (fallback)
- Calcul métriques :
  - `helpful_ratio = helpful_votes / max(1, total_votes)`
- Déduplication stricte sur `review_id`
- Normalisation catégories : `category_normalized`

### **Schéma SILVER (exemple)**
```
review_id
product_id
product_title
user_id
rating
review_body
review_length
language
helpful_ratio
review_date
category_normalized
```

---

# **5. Traitements SILVER → GOLD**
### 🎯 Objectif : construire des tables analytiques prêtes pour BI

### **Tables GOLD produites :**

#### **1. fact_reviews**
- Grain : une review
- Champs clés : rating, helpful_ratio, category, date
- Utilisation : dashboards analyse sentiment, qualité produit

#### **2. dim_products**
- Dictionnaire produits
- Champs clés : titre, price, marketplace, catégorie

#### **3. dim_dates**
- Table calendrier (optionnelle)
- Pour faciliter l’analyse temporelle

### **Agrégations appliquées :**
- Rating moyen par produit
- Rating moyen par catégorie
- Nombre de reviews par mois
- Score utilité moyen

### **Exemples de KPIs générés**
- `avg_rating_per_category`
- `reviews_volume_daily`
- `usefulness_score`

---

# **6. Scripts de transformation (pseudo-code)**

## **Raw → Bronze (PySpark)**
```python
df_raw = spark.read.json(raw_path)

df_bronze = (df_raw
    .withColumn("rating", col("rating").cast("int"))
    .withColumn("review_date", to_date(col("review_date")))
    .filter(col("rating").between(1,5))
    .filter(col("review_body").isNotNull())
)

df_bronze.write.mode("overwrite").parquet(bronze_path)
```

## **Bronze → Silver**
```python
df_silver = (df_bronze
    .withColumn("review_length", length(col("review_body")))
    .groupBy("product_id")
)
```

## **Silver → Gold**
```python
df_fact = df_silver.select(...)

df_fact.write.mode("overwrite").parquet(gold_fact_path)
```

---

# **7. Orchestration (Airflow)**
Le pipeline est orchestré par Airflow via un DAG comportant :
- task 1 : ingestion RAW
- task 2 : processing RAW → BRONZE
- task 3 : validation
- task 4 : BRONZE → SILVER
- task 5 : SILVER → GOLD
- task 6 : upload S3 final
- task 7 : reporting/logging

### Exemple de structure DAG
```
start
  → ingest_raw
  → raw_to_bronze
  → bronze_validation
  → bronze_to_silver
  → silver_to_gold
  → notify_completion
end
```

---

# **8. Tests qualité (Great Expectations / Pandas)**
### Tests appliqués :
- rating entre 1 et 5
- body non null
- product_id non vide
- format date valide
- aucune duplication

### Résultats :
✔️ pipeline validé  
✔️ taux d’erreur maîtrisé  
✔️ données GOLD conformes pour BI

---

# **9. Conclusion**
Le Step 4 est considéré comme : **validé** ✔️

L’ensemble du pipeline de transformation RAW → BRONZE → SILVER → GOLD est :
- fonctionnel,
- documenté,
- reproductible,
- compatible avec Airflow,
- prêt pour la suite (Step 5 : orchestration complète et industrialisation).

---



