import pandas as pd
from pathlib import Path
from etl.utils.logging import get_logger
from etl.utils.io import ensure_dir, save_json

logger = get_logger("model")

KEEP_CANDIDATES = [
    "review_id", "product_id", "customer_id",
    "star_rating", "helpful_votes", "helpful_votes_norm",
    "sentiment_proxy", "lexical_diversity", "recency_decay",
    "relevance_score", "review_date"
]

def run_model(config: dict, batch_id: str) -> dict:
    silver_dir = Path(config["paths"]["silver"]) / f"batch={batch_id}"
    gold_dir = Path(config["paths"]["gold"]) / f"batch={batch_id}"
    ensure_dir(gold_dir)

    # On charge le vrai fichier généré par le Transform
    review_file = silver_dir / "review.parquet"
    if not review_file.exists():
        raise FileNotFoundError(
            f"❌ review.parquet introuvable dans {silver_dir}. "
            f"Les fichiers disponibles sont : {list(silver_dir.glob('*.parquet'))}"
        )

    rv = pd.read_parquet(review_file)

    # On garde uniquement les colonnes présentes
    keep = [c for c in KEEP_CANDIDATES if c in rv.columns]
    fact = rv[keep].copy()

    out = gold_dir / "fact_reviews.parquet"
    fact.to_parquet(out, index=False)

    save_json(
        gold_dir / "stats.json",
        {"batch_id": batch_id, "gold_rows": len(fact)}
    )

    logger.info(f"Gold écrit : {out} ({len(fact)} lignes)")
    return {"gold_dir": str(gold_dir), "rows": len(fact)}
