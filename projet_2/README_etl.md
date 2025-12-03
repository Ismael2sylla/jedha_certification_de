# Amazon Review Analysis - Pipeline ETL

Pipeline ETL automatisé pour extraire, transformer et charger les
données d'avis Amazon depuis PostgreSQL vers S3, Snowflake et MongoDB.

🚀 Nouveau sur le projet ? Consultez QUICKSTART.md pour démarrer en 5
minutes !

------------------------------------------------------------------------

## Démarrage Rapide (3 étapes)

### 1. Démarrer les bases de données

``` bash
# PostgreSQL (contient les données source)
docker-compose -f docker-compose.postgres.yml up -d

# MongoDB (stocke les métadonnées du pipeline)
cd src_code
docker-compose -f docker-compose.mongodb.yml up -d
cd ..
```

> Attendre 1-2 minutes pour l'initialisation PostgreSQL lors du premier
> lancement.

------------------------------------------------------------------------

### 2. Configurer les credentials

``` bash
cd src_code
cp .env.example .env
# Modifier .env avec vos credentials AWS et Snowflake
```

------------------------------------------------------------------------

### 3. Lancer le pipeline

``` bash
cd src_code

# Option A : Pipeline complet
python scripts/pipeline.py --all

# Option B : Étape par étape
python scripts/extract_to_s3.py
python scripts/process_and_store.py
```

------------------------------------------------------------------------

## Architecture

    PostgreSQL (Docker) → AWS S3 (Data Lake) → Snowflake (Data Warehouse)
                                  ↓
                           MongoDB (Docker)

------------------------------------------------------------------------

## Structure du Projet

    project_2/
    ├── README.md
    ├── docker-compose.postgres.yml
    ├── .env.local
    ├── data/
    │   └── clean/
    ├── docker/postgres/init/
    └── src_code/
        ├── README.md
        ├── docker-compose.mongodb.yml
        ├── .env
        ├── scripts/
        │   ├── pipeline.py
        │   ├── extract_to_s3.py
        │   └── process_and_store.py
        └── config/

------------------------------------------------------------------------

## Commandes Utiles

### Gestion des conteneurs

``` bash
docker ps
docker-compose -f docker-compose.postgres.yml down
cd src_code && docker-compose -f docker-compose.mongodb.yml down
```

### Réinitialiser PostgreSQL

``` bash
docker-compose -f docker-compose.postgres.yml down -v
docker-compose -f docker-compose.postgres.yml up -d
```

### Vérifier les connexions

``` bash
# PostgreSQL
docker exec -it amazon_postgres_db psql -U admin -d amazon_db -c "SELECT COUNT(*) FROM product;"

# MongoDB
docker exec -it amazon-reviews-mongodb mongosh -u admin -p changeme --eval "db.adminCommand('ping')"
```

------------------------------------------------------------------------

## Données Disponibles

Le projet contient environ **1,7M d'enregistrements** répartis dans 25
tables :

-   130 766 clients\
-   42 858 produits\
-   222 644 commandes\
-   111 322 avis\
-   100 000 acheteurs

------------------------------------------------------------------------

## Tests de Qualité

``` bash
cd src_code
python tests/test_data_quality.py
python scripts/generate_quality_report.py
```

8 tests automatisés :

-   Connexion PostgreSQL\
-   Ratings valides (1--5)\
-   Détection doublons\
-   Champs obligatoires\
-   Prix positifs\
-   Textes non vides\
-   Types cohérents\
-   Intégrité référentielle

Rapports disponibles : `src_code/reports/`

------------------------------------------------------------------------

## Documentation Détaillée

-   `src_code/README.md`\
-   `CONFORMITE_ETL.md`\
-   `.env.example`

------------------------------------------------------------------------

## Technologies

  Domaine          Outil
  ---------------- --------------
  Source           PostgreSQL
  Data Lake        AWS S3
  Data Warehouse   Snowflake
  Logging          MongoDB
  ETL              Python 3.11+

------------------------------------------------------------------------

## À propos du projet

Projet réalisé dans le cadre du **Bootcamp Data Engineering Jedha**,
dans un contexte d'industrialisation d'un pipeline d'analyse d'avis
Amazon, en cohérence avec les standards modernes du Data Engineering et
mon parcours de reconversion vers un rôle de **Data Engineer**.
