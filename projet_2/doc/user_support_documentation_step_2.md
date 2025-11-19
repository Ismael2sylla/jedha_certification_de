# Step 2 – User Support Documentation
*(Draft complet, prêt à livrer – Guide technique + procédures opérationnelles + SLA + monitoring + troubleshooting)*

---

# 1. Introduction
Ce document constitue le **dossier d’accompagnement utilisateur et opérateur** pour le système d’analyse des avis Amazon. Il fournit :
- une documentation technique complète,
- les procédures opérationnelles journée/semaine/mois,
- un plan de support avec SLA,
- les tableaux de bord de supervision,
- les runbooks de résolution incidents,
- les schémas d’architecture et de flux.

Il est conçu pour :
- les **Data Engineers**,
- les **Data Scientists**,
- les **Administrateurs**,
- les **Analystes métiers**.

---

# 2. Technical Architecture Guide

## 2.1. Architecture globale
Le système complet comporte :
- **NeonDB** : base de données hébergeant les tables sources.
- **ETL Pipeline (Python)** : extract → transform → model.
- **Stockage Data Lake (local)** : bronze / silver / gold.
- **Environnement Python virtualisé** : `.venv` + dépendances.
- **Configuration externe** : `config.yaml` + `.env`.

### 2.2. Diagramme des flux
*(Insérer ici un schéma logique simple : DB → Extract → Bronze → Transform → Silver → Model → Gold → API/Analystes)*

---

# 3. Documentation des Composants

## 3.1. NeonDB (PostgreSQL)
- Type : PostgreSQL serverless (Neon)
- Schéma : `amazon`
- Tables : buyer, customer, product, review, review_images, etc.
- Authentification : variable `NEON_DB_URL`

## 3.2. Extract Layer (Bronze)
### Description
Extraction complète de toutes les tables transactionnelles vers des fichiers **Parquet**.

### Commande d'exécution
```
python -m etl.pipeline --extract
```

### Output
```
data/bronze/batch=<id>/<table>.parquet
```

## 3.3. Transform Layer (Silver)
- Nettoyage
- Harmonisation des colonnes
- Normalisation des types
- Jointures nécessaires

Commande :
```
python -m etl.pipeline --transform --batch-id=<id>
```

## 3.4. Model Layer (Gold)
- Génération d’un score de pertinence
- Sélection de colonnes business-ready
- Export en `fact_reviews.parquet`

Commande :
```
python -m etl.pipeline --model --batch-id=<id>
```

---

# 4. Operational Procedures Manual

## 4.1. Procédures quotidiennes
| Tâche | Description | Responsable |
|-------|-------------|-------------|
| Vérifier logs ETL | S’assurer qu’aucune erreur n’a eu lieu | Data Engineer |
| Monitor DB | Vérifier utilisation CPU/RAM | Admin |
| Vérifier gold | S’assurer que le parquet final est généré | Data Engineer |

## 4.2. Procédures hebdomadaires
- Analyse des performances ETL
- Vérification de la croissance des données
- Nettoyage des anciens batches (>30 jours si nécessaire)

## 4.3. Procédures mensuelles
- Test de restauration NeonDB
- Vérification intégrité schema
- Audit sécurité (RBAC, permissions)

---

# 5. User Support Plan (SLA)

## 5.1. Accès au système
- Authentification via `.env`
- Droits définis par RBAC (analyst, scientist, engineer, admin)

## 5.2. Niveaux de service (SLA)
| Élément | Objectif | Détail |
|---------|----------|--------|
| Disponibilité DB | **99.9%** | Garanties NeonDB |
| Disponibilité ETL | **99%** | Pipeline accessible et exécutable |
| Temps d’exécution ETL | < **2 minutes** | Extraction + transformation + modèle |
| Restauration DB | < **30 min** | PITR Neon |

## 5.3. Support & Escalation
### Niveau 1 – Analystes
- Lecture gold
- Signaler anomalies

### Niveau 2 – Data Engineer
- Relancer pipeline
- Déboguer transformations

### Niveau 3 – Administrateur
- Problèmes de base de données
- Évolutions majeures

---

# 6. Monitoring & Observabilité

## 6.1. Outils recommandés
- **Grafana + Prometheus** (optionnel)
- **Logs Python** : `etl/utils/logging.py`
- **Fichiers `manifest.json`** bronze/silver/gold

## 6.2. Métriques à collecter
| Type | Métrique | Description |
|------|----------|-------------|
| Performance | temps_pipeline | durée extract/transform/model |
| Qualité | rows_bronze/silver/gold | vérification cohérence |
| Système | Neon load | charge CPU/IO sur cluster |

## 6.3. Dashboards recommandés
- Pipeline latency
- Volume des datasets
- Succès/échec par étape
- Score distribution fact_reviews

## 6.4. Alerting
- Pipeline failed → alerte immédiate
- Gold manquant → criticité haute
- DB unreachable → criticité haute

---

# 7. Troubleshooting & Runbooks

## 7.1. Incident : “relation table not found”
**Cause** : tables non initialisées ou mauvais `search_path`.
**Solution** :
1. Vérifier schéma dans Neon
2. Relancer init CSV :
```
python -m etl.init_neon_from_csv
```

## 7.2. Incident : “FileNotFoundError parquet”
**Cause** : batch incomplet ou mauvais ID.
**Solution** :
1. Lister les batches dans `data/bronze`
2. Relancer pipeline complet

## 7.3. Incident : Connexion DB impossible
**Cause** : mauvais `.env`, SSL Neon, ou offline.
**Solution** :
- Vérifier `NEON_DB_URL`
- Regénérer token Neon si besoin

## 7.4. Incident : pipeline crash step model
**Cause** : colonnes manquantes
**Solution** :
1. Inspecter silver
2. Vérifier `KEEP_CANDIDATES`

---

# 8. Annexes
- Structure du fichier `config.yaml`
- Structure du `.env`
- Exemples complets de commandes
- Exemples d’APIs (optionnel si intégration mockup)

---

# 9. Conclusion
Cette documentation d’accompagnement fournit toutes les informations nécessaires pour :
- exécuter, comprendre, maintenir et dépanner le système,
- opérer la pipeline en production,
- surveiller les performances et garantir la stabilité,
- assurer le support auprès des utilisateurs.

Elle sert de base aux équipes Data Engineering, Data Science et aux administrateurs système dans l’exploitation du système Amazon Reviews.

---

*(Fin du livrable Step 2 – User Support Documentation)*

