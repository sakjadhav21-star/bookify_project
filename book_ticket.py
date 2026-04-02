from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

user_id = input("Enter your User ID: ")
train_id = input("Enter Train ID: ")
source = input("Enter Source Station ID: ")
destination = input("Enter Destination Station ID: ")
date = input("Enter Travel Date (YYYY-MM-DD): ")
price = input("Enter Price: ")

cur.execute("""
    INSERT INTO Ticket 
    (user_id, train_id, price, travel_date, source_id, destination_id)
    VALUES (%s, %s, %s, %s, %s, %s)
""", (user_id, train_id, price, date, source, destination))

conn.commit()
print("Ticket booked successfully!")

cur.close()
conn.close()
