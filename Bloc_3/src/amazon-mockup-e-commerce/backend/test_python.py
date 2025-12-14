import os
from dotenv import load_dotenv

# Charger le .env situé dans le dossier parent du backend
load_dotenv("../.env")

db = os.getenv("DATABASE_URL")
print("RAW:", repr(db))
