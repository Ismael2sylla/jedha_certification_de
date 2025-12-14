![Bannière Amazon Review Analysis](https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=80)

# ✨ **Plateforme de Gestion & Analyse des Avis Amazon – Projet Global**
### _De l'analyse stratégique au déploiement prototype – Un pipeline complet Data Engineering_
👤 **Auteur : Ismaël Sylla – Data Engineer**  

---

# 🚀 **Pitch du Projet Global**
Ce projet regroupe **4 blocs cohérents**, construisant une **plateforme de bout-en-bout** dédiée à l’analyse, la catégorisation et la valorisation des avis clients Amazon.  
L’objectif est de développer une chaîne complète : **stratégie, architecture, data pipeline, NLP, scoring, gouvernance, industrialisation et support utilisateur**, conforme au **référentiel RNCP Data Engineer**.

---

# 🧭 **Liens vers les 4 blocs du projet**
[![Bloc 1 – Analyse & Prototype](https://img.shields.io/badge/Bloc%201-Analyse%20%26%20Prototype-003366?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/tree/main/Bloc_1)

[![Bloc 2 – Data Engineering & Pipelines](https://img.shields.io/badge/Bloc%202-Data%20Engineering%20%26%20Pipelines-1f77b4?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/tree/main/Bloc_2)

[![Bloc 3 – Gestion RH & Organisation](https://img.shields.io/badge/Bloc%203-Gestion%20RH%20%26%20Organisation-f39c12?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/tree/main/Bloc_3)

[![Bloc 4 – Support, Budget & Gouvernance](https://img.shields.io/badge/Bloc%204-Support%20%26%20Gouvernance-27ae60?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/tree/main/Bloc_4)



---


# 🧩 **Compétences RNCP couvertes**
Le projet couvre les compétences du référentiel A1–A15, notamment :
- `C1–C8` : Analyse stratégique, veille, data mapping, prototype NLP
- `C9–C12` : Spécifications techniques & fonctionnelles
- `C20–C32` : Planning projet, budget, équipe, support, gouvernance

---

# 🧱 **Technologies utilisées**
Voici les principaux outils et technologies utilisés dans ce projet, accompagnés de leurs logos pour une lecture plus visuelle :

| Technologie | Icône | Description |
|------------|-------|-------------|
| **Python 3.11+** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="22"/> | Pandas, NumPy, SQLAlchemy, Transformers, NLTK |
| **AWS S3** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original.svg" width="22"/> | Stockage cloud des données brutes & transformées |
| **Snowflake** | <img src="https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg" width="22"/> | Data Warehouse analytique |
| **PostgreSQL / NeonDB** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="22"/> | Base relationnelle & stockage structuré |
| **MongoDB** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" width="22"/> | Base NoSQL semi-structurée |
| **Docker** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="22"/> | Conteneurisation & reproductibilité |
| **Airflow** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apacheairflow/apacheairflow-original.svg" width="22"/> | Orchestration de pipelines (préparé) |
| **NLP (VADER)** | <img src="https://cdn-icons-png.flaticon.com/512/3061/3061341.png" width="22"/> | Scoring de pertinence, sentiment analysis |
| **Streamlit** | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg" width="22"/> | Application web de visualisation interactive |






---

# 🧱 **Architecture Globale du Projet**
```
                ┌──────────────────────────────┐
                │        Sources de données     │
                │  APIs • SQL • Fichiers bruts  │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │     Ingestion & Nettoyage     │
                │   Python • Scripts ETL        │
                │   (Orchestration Airflow)     │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │        Data Lake AWS S3        │
                │            (RAW)               │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │   Stockage & Modélisation     │
                │ Snowflake • PostgreSQL        │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │   NLP & Scoring de Pertinence │
                │  Sentiment • Relevance Score  │
                │   (Jobs orchestrés Airflow)   │
                └───────────────┬──────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │   Exposition & Visualisation  │
                │ FastAPI • Streamlit (Web App) │
                └──────────────────────────────┘

```

---

# 📚 **Résumé des 4 blocs du projet**

---

# 🧠 **Cas d’usage métier détaillés**
Voici les principaux scénarios métiers que la plateforme permet d’adresser :

### 🔎 1. Détection automatique des avis critiques
Le scoring NLP permet d’identifier rapidement les avis négatifs à fort impact (longueur élevée, ton négatif, absence d’image, rating extrême).  
➡️ Priorisation pour les équipes support.

### 📦 2. Identification des défauts produit
En catégorisant les avis par thématique, le système repère les problèmes récurrents (qualité, livraison, emballage…).  
➡️ Aide les Product Managers à orienter les roadmaps.

### 🤝 3. Aide au support client
Grâce à une classification automatisée, les équipes support peuvent accéder :
- aux avis les plus critiques, 
- aux avis les plus complets, 
- aux causes probables d’insatisfaction.

➡️ Réduction du temps de traitement.

### 💡 4. Optimisation de la conversion
Mettre en avant les avis les plus pertinents améliore la confiance client et la conversion produit.  
➡️ Impact direct sur les ventes Amazon.

### 📊 5. Pilotage logistique
Les avis contenant des mentions sur la livraison peuvent être analysés en masse.  
➡️ Détection des zones géographiques problématiques.

---

# 🧱 **Schémas supplémentaires**

## 🔄 Data Flow complet du projet
```
Amazon → PostgreSQL → Airflow ETL → S3 Raw
      → Snowflake Silver/Gold → NLP Scoring
      → FastAPI → Streamlit

```

## 🧩 Pipeline NLP – Étapes
```
1. Nettoyage texte
2. Extraction features (longueur, mots clés, images…)
3. Analyse sentiment (VADER)
4. Détection rating extrême
5. Calcul relevance_score
6. Classification (Relevant / Irrelevant)
```

## 🗂 Modèle Data Lake – Bronze / Silver / Gold
```
Bronze : Données brutes (raw Amazon reviews)
Silver : Données nettoyées + enrichies (sentiment, features)
Gold : Données prêtes pour BI + scoring final
```

---

# 🛠️ **Stack technique détaillée par bloc**

## 🎯 Bloc 1 – Analyse & Prototype
- Python (NLP, scoring, analyse exploratoire)
- Seaborn / Matplotlib
- PostgreSQL (requêtes analytiques)
- Jupyter Notebook
- Méthodologie Design Thinking

## ⚙️ Bloc 2 – Data Engineering
- Python ETL
- psycopg2 / SQLAlchemy
- AWS S3 (Raw / Processed)
- Snowflake (DWH)
- Docker (environnements reproductibles)
- Airflow (structure d’orchestration)

## 🧑‍🤝‍🧑 Bloc 3 – RH & Organisation
- Matrice RACI
- Gestion des rituels projet
- Onboarding
- Gestion montée en compétence

## 🧾 Bloc 4 – Budget, Support & Gouvernance
- Matrice de risques
- Dashboard budget
- Documentation utilisateur
- Support niveau 1/2/3
- SLA & engagements

---

# 📚 **Résumé des 4 blocs du projet****

## 🎯 **Bloc 1 – Analyse Stratégique & Prototype NLP**
Ce premier bloc explore la vision business du projet Amazon Review Analysis : analyse stratégique, étude organisationnelle, cartographie des flux, priorisation des cas d’usage. 
Un prototype NLP est développé pour classifier et scorer la pertinence des avis sur la base de critères objectifs (longueur, sentiment, images, rating extrême).

📌 Contenu : SWOT, veille technologique & réglementaire, data mapping, scoring NLP, architecture cible.  
📎 Liens : Bloc 1 (voir plus haut)

---

## ⚙️ **Bloc 2 – Data Engineering & Pipelines**
Ce bloc couvre la construction du pipeline de données : ingestion depuis PostgreSQL, stockage S3, transformation Python, normalisation, et intégration dans Snowflake.  
Architecture orientée data lake / warehouse avec tables Bronze → Silver → Gold.

📌 Contenu : scripts ETL, connexions sécurisées, stockage cloud, optimisation, qualité.  
📎 Liens : Bloc 2

---

## 🧑‍🤝‍🧑 **Bloc 3 – Gestion RH & Structuration Équipe Projet**
Ce module traite de la gestion d'équipe dans un contexte Data/IT : rôles, responsabilités, matrice RACI, processus RH, plans de montée en compétences, inclusion.

📌 Contenu : fiches rôles, workflow RH, formations, rituels d'équipe.  
📎 Liens : Bloc 3

---

## 🧾 **Bloc 4 – Budget, Support & Gouvernance Projet**
Ce dernier module décrit la mise en œuvre complète du projet : planning, budget détaillé, matrice de risques, gestion RH, support utilisateur et documentation de déploiement.

📌 Contenu : budget prévisionnel, risques, support utilisateur, gouvernance, documentation finale.  
📎 Liens : Bloc 4

---

# 🧪 **Fonctionnalités Clés du Projet Global**
- Analyse stratégique & cadrage business
- Cartographie et sélection des données Amazon
- Prototype NLP de classification & scoring
- Pipeline ETL complet : PostgreSQL → S3 → Snowflake
- Structuration RH & organisation projet
- Modèles de support utilisateur
- Documentation complète & livrables RNCP

---

# 🔮 **Améliorations Futures**
- Industrialisation Airflow des pipelines
- Passage NLP à un modèle transformer fine-tuné
- Déploiement API du scoring (FastAPI)
- CI/CD GitHub Actions
- Automatisation cloud & monitoring
- Dashboard analytique temps réel

---

# 👤 **À propos de l’auteur**

**Ismaël Sylla** – Data Engineering Trainee / Data & Cloud Enthusiast

Actuellement en parcours de certification Data Engineering, avec un fort intérêt pour les pipelines de données, les architectures cloud, l’automatisation des traitements et l’exploitation analytique des données (NLP, scoring, visualisation).

Ce projet s’inscrit dans une démarche d’apprentissage orientée production, qualité des données et bonnes pratiques DataOps, avec pour objectif une montée en compétence progressive vers un rôle de Data Engineer.

### 🔗 Me suivre

💼 LinkedIn

🐙 GitHub

---

# 📘 **Conclusion Générale****
Ce projet global démontre une montée en compétence progressive et complète sur l’ensemble du cycle de vie data :
- cadrage stratégique,
- engineering & cloud,
- NLP & analyse avancée,
- gouvernance & support,
- pilotage projet.

Il offre une vision claire d’une **plateforme industrielle d’analyse d’avis clients**, pouvant être étendue à grande échelle et intégrée dans une architecture entreprise.

---

# 🙏 **Remerciements**
Un immense merci à toutes les personnes et organisations qui ont contribué à la réussite de ce projet et à mon évolution professionnelle :

- **📮 La Poste** — pour son accompagnement dans mon changement de carrière et la confiance accordée.  
- **🎓 Jedha** — pour une formation complète, exigeante et structurante, qui m’a permis d’acquérir des compétences solides en Data Engineering et en IA.  
- **👩‍💼 Corinne BARBAROUX** — ma manager, pour son soutien, ses conseils et son engagement dans mon développement professionnel.  

Merci à toutes celles et ceux qui m’ont encouragé, accompagné et inspiré tout au long de ce parcours. 🙏

---

# ⭐ **Si ce projet vous a inspiré, pensez à laisser une étoile sur le repository !**
Merci pour votre lecture 🙏

