# 📘 **Amazon Review Analysis – Phase 1**  
### _Strategic Analysis • Ideation • Data Scoping • Prototype • Tech Specs_  
👤 **Auteur : Ismaël Sylla**  
📦 **Projet : Analyse des avis produits Amazon**

---

# 📑 **📚 Table des Matières**

## 🔗 Liens des repositories
[![Step 1 – Analyse stratégique](https://img.shields.io/badge/Step%201-Analyse%20stratégique-003366?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/Docs/phase%201%20-%20rapport%20analyse%20strat%C3%A9gique.pdf)

[![Step 2 – Idéation & besoins](https://img.shields.io/badge/Step%202-Idéation%20%26%20besoins-1f77b4?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/Docs/Phase%202%20-%20identification%20besoins.pdf)

[![Step 3 – Veille technologique & réglementaire](https://img.shields.io/badge/Step%203-Veille%20tech%20%26%20réglementaire-f39c12?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/Docs/phase%203%20-%20veille%20r%C3%A9glementaire_technologique.pdf)

[![Step 4 – Cartographie des données](https://img.shields.io/badge/Step%204-Cartographie%20des%20données-8e44ad?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/Docs/phase%204%20-%20selection%20donnees%20cartographie%20opportunites.pdf)

[![Step 5 – Prototype & scoring](https://img.shields.io/badge/Step%205-Prototype%20%26%20scoring-c0392b?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/src/Phase5%20-%20Prototype.ipynb)

[![Step 6 – Spécifications techniques](https://img.shields.io/badge/Step%206-Spécifications%20techniques-2c3e50?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/Docs/Phase%206%20-%20Sp%C3%A9cifications%20techniques.pdf)

[![Step 7 – Présentation finale](https://img.shields.io/badge/Step%207-Présentation%20finale-27ae60?style=for-the-badge)](https://github.com/Ismael2sylla/jedha_certification_de/blob/main/Bloc_1/Docs/Phase%207-%20Presentation.pdf)



---

# 🚀 Step 1 – Analyse stratégique
### 🔍 Contexte Amazon
Amazon repose sur un écosystème complet (Marketplace, AWS, Advertising, Logistics). Les avis clients constituent un pilier essentiel de la conversion et de la recommandation.

### 🧭 SWOT
- **Forces** : logistique, IA avancée, large catalogue  
- **Faiblesses** : faux avis, dépendance vendeurs tiers  
- **Opportunités** : IA/LLM, insights client  
- **Menaces** : RGPD, AI Act, concurrence  

### 🔄 Cycle de vie d’un avis
1. Publication  
2. Collecte  
3. Stockage Data Lake  
4. NLP + scoring  
5. Intégration DW  
6. Modération  
7. Reporting  

---

# 💡 Step 2 – Idéation & besoins utilisateurs
### 🎨 Méthode : Design Thinking
- Empathize / Observe  
- Define  
- Ideate  
- Prototype  

### 👥 Personas clés
- Responsable Produit  
- Data Analyst  
- Support Client  

### 🔥 Problématique centrale
> Comment classer automatiquement les avis clients et identifier les plus pertinents à grande échelle ?

### ⭐ Cas d’usage priorisés
1. Analyse de satisfaction  
2. Détection de faux avis  
3. Identification défauts produits  
4. Alertes logistiques  
5. Dashboards thématiques  

---

# 🛡 Step 3 – Veille technologique & réglementaire
### 🧪 Technologies analysées
- NLP/LLM : BERT, mDeBERTa, GPT  
- AWS : S3, Glue, Redshift, SageMaker  
- MLOps : Airflow, MLflow  
- BI : Power BI  

### ⚖ Réglementations
- RGPD  
- AI Act  
- CCPA  
- CNIL  

🔐 Impacts : anonymisation, traçabilité, explicabilité, human-in-the-loop.

---

# 🗂 Step 4 – Sélection & cartographie des données
### 📦 Tables essentielles
| Table | Rôle | Volumétrie | Données |
|-------|-------|------------|---------|
| REVIEW | Avis | 111k | Texte, note, titre |
| PRODUCT_REVIEWS | Mapping | 111k | Associations |
| PRODUCT | Produit | 42k | Nom, prix, desc |
| CATEGORY | Catégorie | 2 | Labels |
| REVIEW_IMAGES | Images | 119k | Photos |

### 🔗 Relations
- BUYER → REVIEW (1:N)  
- REVIEW → PRODUCT (N:N)  
- PRODUCT → CATEGORY (N:1)

---

# 🧪 Step 5 – Prototype : Identification des reviews pertinentes
### 🎯 Objectif
Développer un système de scoring permettant d’identifier automatiquement les reviews les plus pertinentes.

### 🧩 Critères du scoring (pondérés)
- Longueur du texte : **30%**  
- Présence d’images : **20%**  
- Achat vérifié : **10%**  
- Rating extrême : **15%**  
- Sentiment VADER : **25%**  

### 📊 Insights clés
- 76.4% des reviews = **5★**  
- 31.6% contiennent une image  
- Longueur médiane = **44 caractères**  
- Reviews négatives plus longues → plus informatives

### 🧮 Formule du relevance_score
```
relevance_score = (
    0.30 * text_length_score +
    0.20 * has_image +
    0.10 * has_orders +
    0.15 * is_extreme_rating +
    0.25 * keyword_score
) * 100
```

### 🧪 Tests fonctionnels
Tests implémentés pour vérifier :
- text_length_score  
- sentiment_score  
- extreme_rating  
- relevance_score  

### ⚠ Limitations
- Reviews très courtes → bruit NLP  
- has_orders peu discriminant  
- Scoring trop strict (>80 = 96% irrelevant)  

### 🚀 Améliorations proposées
#### Court terme
- Filtrer textes <30 caractères  
- Ajuster pondérations  
- Étendre l’échantillon  

#### Moyen terme
- Fine-tuning modèle NLP  
- Embeddings contextuels  
- GPU batch processing  

#### Long terme
- Modèle multitâches  
- Détection fake reviews  
- Clustering thématique dynamique  

---

# ⚙ Step 6 – Spécifications techniques & fonctionnelles
### 🎯 Objectifs
- Pipeline ingestion + nettoyage  
- NLP + scoring  
- Dashboards Power BI  
- Règles de qualité de données  

### 🏗 Architecture
```
PostgreSQL
   ↓ Airflow (Batch)
S3 Raw → Clean
   ↓
Python NLP + Scoring
   ↓
Data Warehouse
   ↓
Streamlit
```

---

# 🧩 Synthèse globale
| Axe | Résultat |
|------|----------|
| Stratégie | Analyse Amazon + SWOT |
| Besoins | Personas + cas d’usage |
| Veille | Tech + règlementaire |
| Données | Cartographie + dictionnaire |
| Prototype | Relevance scoring + tests |
| Specs | Architecture + contraintes |

➡️ La Phase 2 pourra industrialiser le pipeline Airflow + S3 + DW et intégrer un modèle NLP avancé.

