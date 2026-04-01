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

print("---- SIGN UP ----")
name = input("Enter name: ")
email = input("Enter email: ")
password = input("Enter password: ")
age = int(input("Enter age: "))

cur.execute("INSERT INTO user_table (name, email, password, age) VALUES (%s, %s, %s, %s)",
            (name, email, password, age))

conn.commit()
print("Signup successful!")

conn.close()