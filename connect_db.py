import psycopg2

try:
    conn = psycopg2.connect(
        dbname="python_db",
        user="postgres",
        password="yourpassword",
        host="localhost"
    )
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print("Connection failed:", e)
finally:
    if 'conn' in locals() and conn:
        conn.close()
