import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from etl.utils.logging import get_logger
from etl.utils.io import ensure_dir, new_batch_id, save_json

logger = get_logger("extract")

# Tables réelles dans le schéma "amazon"
DEFAULT_TABLES = [
    "buyer", "carrier", "cart", "cart_items", "category", "customer",
    "customer_payment", "customer_shipping", "daily_deals", "discount",
    "orders", "payment_details", "product", "product_images",
    "product_reviews", "returns", "review", "review_images",
    "seller", "seller_products", "seller_reviews", "shipment",
    "shipping_details", "subscription", "wishlist_item"
]


def _build_engine_from_config(conn_cfg: dict):
    load_dotenv()

    # priorité à l’URL fournie via url_env
    url_env_key = conn_cfg.get("url_env")
    if url_env_key:
        db_url = os.getenv(url_env_key)
        if not db_url:
            raise RuntimeError(f"Env var {url_env_key} is not set")

        engine = create_engine(db_url)

        # test rapide
        with engine.connect() as _:
            pass

        return engine

    # Si un jour tu veux gérer d'autres types de config (conn_str, etc.)
    raise RuntimeError("No valid DB connection config found (expected 'url_env').")


def run_extract(config: dict, tables=DEFAULT_TABLES) -> dict:
    batch_id = new_batch_id()
    out_dir = Path(config["paths"]["bronze"]) / f"batch={batch_id}"
    ensure_dir(out_dir)

    # 🔴 ICI : on suppose que config["sources"]["transactional_db"] existe
    conn_cfg = config["sources"]["transactional_db"]
    schema = conn_cfg.get("schema")

    engine = _build_engine_from_config(conn_cfg)

    stats = {"batch_id": batch_id, "tables": {}}
    try:
        with engine.connect() as conn:
            # Fixe le search_path pour éviter d’avoir à préfixer toutes les tables
            if schema:
                conn.execute(text(f'SET search_path TO "{schema}", public;'))

            for t in tables:
                df = pd.read_sql(text(f"SELECT * FROM {t};"), conn)
                out_path = out_dir / f"{t}.parquet"
                df.to_parquet(out_path, index=False)
                stats["tables"][t] = {"rows": len(df), "path": str(out_path)}
                logger.info(f"Exported {t}: {len(df)} rows → {out_path}")
    finally:
        engine.dispose()

    save_json(out_dir / "manifest.json", {
        "batch_id": batch_id,
        "tables": list(stats["tables"].keys()),
        "rows_total": sum(v["rows"] for v in stats["tables"].values()),
    })
    return {"batch_id": batch_id, "bronze_dir": str(out_dir)}
