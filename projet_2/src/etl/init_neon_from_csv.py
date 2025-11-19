import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# 1. Charger les variables d'environnement (NEON_DB_URL)
load_dotenv()

DB_URL = os.getenv("NEON_DB_URL")
if not DB_URL:
    raise RuntimeError("NEON_DB_URL is not set in your .env")

# 2. Créer l'engine SQLAlchemy vers Neon
engine = create_engine(DB_URL)

# 3. Dossier où sont tes CSV (à adapter si besoin)
# Ici : dossier "data" à la racine du projet (même niveau que "etl", "config", etc.)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
# 1er choix : etl/sql/data  (ton vrai dossier)
candidate1 = PROJECT_ROOT / "etl" / "sql" / "data"
# 2e choix : data à la racine (au cas où tu changes d'avis plus tard)
candidate2 = PROJECT_ROOT / "data"

if candidate1.exists():
    DATA_DIR = candidate1
elif candidate2.exists():
    DATA_DIR = candidate2
else:
    raise RuntimeError(f"Aucun dossier data trouvé : {candidate1} ni {candidate2}")

print(f"Using DATA_DIR = {DATA_DIR}")

# 4. Liste des tables / fichiers attendus
TABLES = [
    "buyer","carrier","cart","cart_items","category","customer",
    "customer_payment","customer_shipping","daily_deals","discount",
    "orders","payment_details","product","product_images",
    "product_reviews","returns","review","review_images",
    "seller","seller_products","seller_reviews","shipment",
    "shipping_details","subscription","wishlist_item",
]


def main():
    print(f"Using DATA_DIR = {DATA_DIR}")
    if not DATA_DIR.exists():
        raise FileNotFoundError(f"DATA_DIR {DATA_DIR} does not exist")

    with engine.begin() as conn:
        # 1) Créer le schéma amazon s'il n'existe pas
        conn.execute(text('CREATE SCHEMA IF NOT EXISTS amazon;'))
        conn.execute(text('SET search_path TO amazon, public;'))
        print("[OK] Schema 'amazon' ready")

        # 2) Pour chaque table, lire le CSV et pousser dans Neon
        for table in TABLES:
            csv_path = DATA_DIR / f"{table}.csv"
            if not csv_path.exists():
                print(f"⚠️ CSV not found for table '{table}' -> {csv_path}, skipping")
                continue

            print(f"→ Loading {csv_path} into table amazon.{table} ...")
            df = pd.read_csv(csv_path)
            # Si les fichiers sont gros tu peux mettre chunksize, mais pour le projet ça devrait aller

            # if_exists="replace" : on recrée la table à chaque fois (simple pour dev)
            df.to_sql(table, conn, schema="amazon", if_exists="replace", index=False)
            print(f"[OK] Table {table} created/filled with {len(df)} rows")

    print("✅ Neon initialised from local CSVs.")


if __name__ == "__main__":
    main()
