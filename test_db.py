import psycopg2

print("Connecting to database...")

try:
    conn = psycopg2.connect(
        host="localhost",
        database="bookify",
        user="postgres",
        password=input("Enter DB password"),
        port="5432"
    )

    print("Connected!")

    cur = conn.cursor()
    cur.execute("SELECT * FROM train")
    rows = cur.fetchall()

    print("Data from Train table:")
    for row in rows:
        print(row)

    conn.close()
    print("Connection closed.")

except Exception as e:
    print("Error:", e)
