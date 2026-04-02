from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

print("---- SIGN UP ----")
name = input("Enter name: ")
email = input("Enter email: ")
age = input("Enter age: ")

cur.execute(
    "INSERT INTO user_table (name, email, age) VALUES (%s, %s, %s)",
    (name, email, age)
)

conn.commit()
print("Signup successful!")

cur.close()
conn.close()
