import psycopg2

try:
    conn = psycopg2.connect(
        dbname="python_db",
        user="postgres",
        password="yourpassword",
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE name = %s", ("Alice",))
    conn.commit()
    print("Data deleted successfully!")
except Exception as e:
    print("Error:", e)
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
