import psycopg2

try:
    conn = psycopg2.connect(
        dbname="python_db",
        user="postgres",
        password="yourpassword",
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("Students Data:")
    for row in rows:
        print(row)
except Exception as e:
    print("Error:", e)
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
