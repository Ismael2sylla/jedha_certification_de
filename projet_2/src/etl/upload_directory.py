import os
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID     = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION    = os.getenv("AWS_DEFAULT_REGION", "eu-west-3")

session = boto3.session.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
)

s3 = session.client("s3")

BUCKETS_BY_LAYER = {
    "raw":    "amazon-industry-insights-raw-data",
    "bronze": "amazon-industry-insights-bronze-data",
    "silver": "amazon-industry-insights-silver-data",
    "gold":   "amazon-industry-insights-gold-data",
}


def upload_directory(local_dir, bucket, prefix=""):
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, local_dir).replace("\\", "/")
            s3_key = f"{prefix}/{relative_path}" if prefix else relative_path

            print(f"Uploading {full_path} → s3://{bucket}/{s3_key}")
            s3.upload_file(full_path, bucket, s3_key)

    print("Upload complet ✔️")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True, help="Dossier local à uploader")
    parser.add_argument("--layer", required=True, choices=["raw", "bronze", "silver", "gold"])
    parser.add_argument("--prefix", default="", help="Préfixe S3 facultatif")
    args = parser.parse_args()

    bucket = BUCKETS_BY_LAYER[args.layer]

    upload_directory(args.dir, bucket, args.prefix)
