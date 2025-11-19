from pathlib import Path
import pandas as pd

from etl.utils.io import ensure_dir, save_json
from etl.utils.logging import get_logger

logger = get_logger("transform")


def run_transform(config: dict, batch_id: str) -> dict:
    """
    Transform step v2 : pour l'instant, on fait une transformation simple :
    - on lit tous les fichiers .parquet du bronze pour le batch donné
    - on applique éventuellement quelques nettoyages légers (optionnel)
    - on réécrit les données en silver
    """
    bronze_root = Path(config["paths"]["bronze"])
    silver_root = Path(config["paths"]["silver"])

    bronze_dir = bronze_root / f"batch={batch_id}"
    silver_dir = silver_root / f"batch={batch_id}"
    ensure_dir(silver_dir)

    if not bronze_dir.exists():
        raise FileNotFoundError(f"Bronze directory does not exist: {bronze_dir}")

    logger.info(f"Starting transform for batch_id={batch_id}")
    logger.info(f"Reading from bronze: {bronze_dir}")
    logger.info(f"Writing to silver:  {silver_dir}")

    stats = {"batch_id": batch_id, "tables": {}}

    # Parcourt tous les fichiers Parquet du bronze
    for parquet_file in bronze_dir.glob("*.parquet"):
        table_name = parquet_file.stem  # ex: buyer.parquet -> "buyer"
        logger.info(f"Loading table '{table_name}' from {parquet_file}")

        df = pd.read_parquet(parquet_file)

        # 👉 Ici tu peux éventuellement ajouter un peu de nettoyage générique
        # Exemple basique : retirer les lignes totalement vides
        df = df.dropna(how="all")

        out_path = silver_dir / f"{table_name}.parquet"
        df.to_parquet(out_path, index=False)
        logger.info(f"Saved transformed '{table_name}' -> {out_path} ({len(df)} rows)")

        stats["tables"][table_name] = {
            "rows": len(df),
            "bronze_path": str(parquet_file),
            "silver_path": str(out_path),
        }

    # Manifest pour la couche silver
    manifest_path = silver_dir / "manifest.json"
    total_rows = sum(v["rows"] for v in stats["tables"].values())
    save_json(
        manifest_path,
        {
            "batch_id": batch_id,
            "tables": list(stats["tables"].keys()),
            "rows_total": total_rows,
            "layer": "silver",
        },
    )
    logger.info(f"Silver manifest written to {manifest_path}")

    return {
        "batch_id": batch_id,
        "silver_dir": str(silver_dir),
        "rows_total": total_rows,
    }
