# Partie 2 — ETL Amazon Reviews (Personnalisé)

Config branchée à ta base locale `amazon_mock` (readonly_user).

## Démarrage
```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python etl/pipeline.py --run-all
```
- Exécution planifiée (Airflow) : voir `airflow/dags/amazon_reviews_etl_pythonoperator.py`
