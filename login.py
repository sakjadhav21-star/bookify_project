import psycopg2

db_password = input("Enter DB password: ")

conn = psycopg2.connect(
    host="localhost",
    database="bookify",
    user="postgres",
    password=db_password,
    port="5432"
)

cur = conn.cursor()

print("---- LOGIN ----")
email = input("Enter email: ")
password = input("Enter password: ")

cur.execute("SELECT * FROM user_table WHERE email=%s AND password=%s", (email, password))
user = cur.fetchone()

if user:
    print("Login successful!")
else:
    print("Invalid email or password")

conn.close()