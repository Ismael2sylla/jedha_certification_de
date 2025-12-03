# Step 1 — Architecture Documentation Design
## Projet : Amazon Industry Insights — ETL Reviews

---

# **1. Introduction**
Le Step 1 définit l’architecture complète du pipeline Amazon Reviews. Cette étape pose les bases du système : nature des données, ingestion, compatibilité, procédures de transformation, stockage, conformité légale.

---

# **2. Détermination des données de référence**
Les données sources (Amazon Reviews) comprennent :
- ID produit
- ID utilisateur
- Review textuelle
- Rating (1 à 5)
- Review title
- Date
- Langue
- Votes helpful
- Métadonnées marketplace

### **Caractéristiques**
- Données hétérogènes (CSV/JSON/Parquet)
- Variabilité des champs
- Volume massif -> besoin de Data Lake
- Reviews textuelles -> besoin de nettoyage & typage

### **Schéma de référence (simplifié)**
| Attribut | Type | Unicité | Notes |
|---------|------|---------|-------|
| review_id | string | unique | identifiant de la review |
| product_id | string | clé | pour jointures |
| user_id | string | non unique | anonymisation possible |
| rating | int | 1-5 | contrôle qualité |
| review_body | text | variable | nécessite nettoyage NLP |
| review_date | date | normalisation ISO |

---

# **3. Sélection & Extraction des données**
### Objectifs
- Garantir l’arrivée contrôlée des données brutes
- Vérifier conformité des formats
- Standardiser l’ingestion

### Processus
1. Identification source (local, S3, API)
2. Vérification format
3. Extraction
4. Ingestion dans RAW (S3)
5. Trace des opérations

### Sécurisation
- Vérification hash optionnelle
- Logs d’ingestion
- Contrôles d’encodage

---

# **4. Compatibilité des données**
### Problèmes observés
- Encodages différents
- Types incohérents
- Formats multiples de dates
- Ratings invalides
- Champs manquants

### Solutions
- Normalisation bronze
- Définition d’un schéma Spark strict
- Validation avec Great Expectations
- Conversion en Parquet pour Silver & Gold

---

# **5. Gestion des données rejetées (Rejected Zone)**
### Cas typiques
- Rating hors bornes
- JSON corrompu
- Valeurs critiques manquantes
- Type incompatible

### Pipeline de rejet
- Stockage dans `rejected/YYYY/MM/DD/batch=.../`
- Log détaillé des erreurs
- Reporting automatique

---

# **6. Proposition de stockage massif : Data Lake S3**
La solution retenue est un **Data Lake AWS S3**, structuré en quatre layers.

### Pourquoi S3 ?
- Massivement scalable
- Compatible Spark / Airflow / EMR / Athena
- Économique
- Durable (11 9s)
- Versioning & encryption possibles

---

# **7. Structure des données (RAW → BRONZE → SILVER → GOLD)**
## **7.1 RAW Layer**
- Données brutes sans traitement
- Archivage légal
- Formats variés

## **7.2 BRONZE Layer**
- Données nettoyées
- Typage correct
- Dates normalisées
- Suppression des colonnes inutiles

## **7.3 SILVER Layer**
- Données enrichies
- Jointures (produits, utilisateurs, reviews)
- Déduplication
- Standardisation avancée

## **7.4 GOLD Layer**
- Tables finales BI
- Agrégations & KPIs
- Prêtes pour dashboards

### Exemple d’arborescence
```
raw/source=amazon/batch=uuid/reviews.json
bronze/batch=uuid/reviews_clean.parquet
silver/batch=uuid/reviews_enriched.parquet
gold/fact_reviews.parquet
gold/dim_products.parquet
```

---

# **8. Étapes de nettoyage et transformation**
### Nettoyage (Bronze)
- Trim
- Type casting
- Normalisation des dates
- Suppression doublons

### Transformation (Silver)
- Jointures
- Feature engineering
- Calcul helpful ratio

### GOLD
- Agrégations
- KPIs principaux
- Tables analytiques

---

# **9. Conformité réglementaire (RGPD / CCPA)**
### Obligations
- Protection des PII
- Anonymisation des user_id
- Conservation limitée
- Log des traitements

### Mesures
- SHA256 pour user_id
- Suppression données inutiles
- Encryption S3 optionnelle
- Versioning possible

---

# **10. Résumé du Step 1**
| Livrable | Statut |
|----------|--------|
| Définition données | ✔️ |
| Analyse compatibilité | ✔️ |
| Architecture Data Lake | ✔️ |
| Data Dictionary | ✔️ |
| Procédures ingestion | ✔️ |
| Nettoyage Bronze | ✔️ |
| Transformation Silver | ✔️ |
| Design Gold | ✔️ |
| Conformité RGPD/CCPA | ✔️ |

---


