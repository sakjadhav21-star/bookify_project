from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

print("---- SIGN UP ----")
name = input("Enter name: ")
email = input("Enter email: ")
password = input("Password: "),
age = input("Enter age: ")

cur.execute(
    "INSERT INTO user_table (name, email, password, age) VALUES (%s, %s, %s,  %s)",
    (name, email, password, age)
)

conn.commit()
print("Signup successful!")

cur.close()
conn.close()
