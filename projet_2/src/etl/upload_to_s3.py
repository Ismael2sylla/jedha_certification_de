#!/usr/bin/env python

import os
import argparse
from datetime import datetime

from dotenv import load_dotenv
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# --------------------------
# 1) Charger les variables .env
# --------------------------
# .env doit être dans le même dossier que ce script
load_dotenv()

AWS_ACCESS_KEY_ID     = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION    = os.getenv("AWS_DEFAULT_REGION", "eu-west-3")

if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    raise ValueError("❌ Variables AWS_ACCESS_KEY_ID ou AWS_SECRET_ACCESS_KEY manquantes dans .env")

# --------------------------
# 2) Définir les buckets par layer
# --------------------------
BUCKETS_BY_LAYER = {
    "raw":    "amazon-industry-insights-dev-raw-euw3",
    "bronze": "amazon-industry-insights-dev-bronze-euw3",
    "silver": "amazon-industry-insights-dev-silver-euw3",
    "gold":   "amazon-industry-insights-dev-gold-euw3",
}

# --------------------------
# 3) Créer le client S3
# --------------------------
session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
)
s3 = session.client("s3")


def build_s3_key(local_path: str, prefix: str | None = None) -> str:
    """
    Construit la clé S3 (chemin dans le bucket).

    - Si prefix est fourni → on l'utilise (ex: 'reviews/amazon/en')
    - Sinon → chemin par date: YYYY/MM/DD/nom_fichier
    """
    filename = os.path.basename(local_path)

    if prefix:
        prefix = prefix.strip().strip("/")
        return f"{prefix}/{filename}"

    today = datetime.utcnow()
    date_prefix = today.strftime("%Y/%m/%d")
    return f"{date_prefix}/{filename}"


def upload_file(local_path: str, layer: str, prefix: str | None = None):
    """
    Upload un fichier local vers le bucket correspondant à la layer.
    """
    if layer not in BUCKETS_BY_LAYER:
        raise ValueError(f"Layer inconnue: {layer}. Utilise: raw, bronze, silver, gold.")

    bucket_name = BUCKETS_BY_LAYER[layer]

    if not os.path.isfile(local_path):
        raise FileNotFoundError(f"❌ Fichier local introuvable: {local_path}")

    s3_key = build_s3_key(local_path, prefix)

    print(f"[INFO] Upload de '{local_path}' vers 's3://{bucket_name}/{s3_key}' ...")

    try:
        s3.upload_file(
            Filename=local_path,
            Bucket=bucket_name,
            Key=s3_key
        )
        print("✅ Upload terminé.")
        print(f"[RESULT] Fichier disponible à: s3://{bucket_name}/{s3_key}")
    except NoCredentialsError:
        print("❌ Pas de credentials AWS valides. Vérifie ton .env.")
        raise
    except ClientError as e:
        print(f"❌ Erreur AWS lors de l'upload: {e}")
        raise


def parse_args():
    parser = argparse.ArgumentParser(
        description="Upload d'un fichier vers un bucket S3 (layers raw/bronze/silver/gold)."
    )
    parser.add_argument(
        "--file", "-f",
        required=True,
        help="Chemin du fichier local à uploader (ex: data/mon_fichier.csv)"
    )
    parser.add_argument(
        "--layer", "-l",
        required=True,
        choices=["raw", "bronze", "silver", "gold"],
        help="Layer S3 cible: raw, bronze, silver ou gold."
    )
    parser.add_argument(
        "--prefix", "-p",
        required=False,
        default=None,
        help="Préfixe S3 optionnel (dossier virtuel), ex: 'reviews/amazon/en'. "
             "Si non fourni, on utilise YYYY/MM/DD."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    upload_file(args.file, args.layer, args.prefix)


if __name__ == "__main__":
    main()
