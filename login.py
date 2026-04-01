from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

print("---- LOGIN ----")
email = input("Enter email: ")
password = input("Enter password: ")

cur.execute(
    "SELECT * FROM user_table WHERE email=%s AND password=%s",
    (email, password)
)

user = cur.fetchone()

if user:
    print("Login successful!")
    print("Your User ID is:", user[0])
else:
    print("Invalid login!")

cur.close()
conn.close()