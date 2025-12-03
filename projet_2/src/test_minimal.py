import psycopg2

print("Trying connection...")

conn = psycopg2.connect(
    host="localhost",
    port=5434,
    user="admin",
    password="admin123",
    dbname="amazon_db"
)

print("✅ Connected !")
conn.close()
