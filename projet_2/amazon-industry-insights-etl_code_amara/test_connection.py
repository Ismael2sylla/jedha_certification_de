import os
import psycopg2
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def test_postgres_connection():
    print("🔍 Testing PostgreSQL connection with parameters:")
    print("  HOST     =", os.getenv("POSTGRES_HOST"))
    print("  PORT     =", os.getenv("POSTGRES_PORT"))
    print("  USER     =", os.getenv("POSTGRES_USER"))
    print("  DB       =", os.getenv("POSTGRES_DB"))

    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            dbname=os.getenv("POSTGRES_DB")
        )

        print("✅ [OK] Connection successful!")

        # Optional : test simple requête
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        print("🔎 Test query result:", result)

        cur.close()
        conn.close()
        print("🔒 Connection closed.")

    except Exception as e:
        print("❌ [FAIL] Connection error:")
        print(e)

    print("\n🔬 RAW BYTES CHECK:")
    for key in ["POSTGRES_HOST", "POSTGRES_PORT", "POSTGRES_USER", "POSTGRES_DB", "POSTGRES_PASSWORD"]:
        value = os.getenv(key)
        if value is None:
            print(f"{key} = None")
        else:
            print(f"{key} =", value.encode("utf-8", errors="replace"))


if __name__ == "__main__":
    test_postgres_connection()

