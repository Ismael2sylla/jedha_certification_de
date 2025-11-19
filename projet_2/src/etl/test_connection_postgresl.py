import sys
import psycopg2
import os

from dotenv import load_dotenv
load_dotenv()


def main():
    try:
            conn = psycopg2.connect ("postgresql://neondb_owner:npg_GqCk6oL2Nubc@ep-gentle-term-abxwcrqs-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
                   
            print("[OK] Connected to PostgreSQL")
            return conn
    except Exception as e:
            print(f"[FAIL] Failed to connect to PostgreSQL: {e}")
            raise

if __name__ == "__main__":
     main()
