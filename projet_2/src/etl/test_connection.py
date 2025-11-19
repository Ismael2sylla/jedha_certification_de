import os
import sys

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

def test_pg_connection():
    load_dotenv()

    # si un chemin de config est passé, on l’affiche juste pour info
    if len(sys.argv) > 1:
        cfg_path = sys.argv[1]
        print(f"Using config: {cfg_path}")

    db_url = os.getenv("NEON_DB_URL")
    if not db_url:
        print("❌ NEON_DB_URL not set in .env")
        sys.exit(1)

    print("🔌 Testing connection to PostgreSQL (Neon)…")

    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            res = conn.execute(text("SELECT 1")).scalar()
        print("✅ Connection OK, SELECT 1 ->", res)
    except Exception as e:
        print("❌ ERROR")
        # on affiche le message sans tenter de le re-décoder -> plus de UnicodeDecodeError
        print(repr(e))

if __name__ == "__main__":
    test_pg_connection()
