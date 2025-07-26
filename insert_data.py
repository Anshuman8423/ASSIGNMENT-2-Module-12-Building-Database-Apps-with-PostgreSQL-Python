import psycopg2

try:
    conn = psycopg2.connect(
        dbname="python_db",
        user="postgres",
        password="yourpassword",
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Alice", 22))
    conn.commit()
    print("Data inserted successfully!")
except Exception as e:
    print("Error:", e)
finally:
    if 'cur' in locals():
        cur.close()
    if 'conn' in locals():
        conn.close()
