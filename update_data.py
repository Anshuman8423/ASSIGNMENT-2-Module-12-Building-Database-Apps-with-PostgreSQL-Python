import psycopg2

try:
    conn = psycopg2.connect(
        dbname="python_db",
        user="postgres",
        password="yourpassword",
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("UPDATE students SET age = %s WHERE name = %s", (25, "Alice"))
    conn.commit()
    print("Data updated successfully!")
except Exception as e:
    print("Error:", e)
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
