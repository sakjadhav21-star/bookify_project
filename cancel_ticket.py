from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

ticket_id = input("Enter Ticket ID to cancel: ")
user_id = input("Enter Your User ID: ")

cur.execute(
    "DELETE FROM Ticket WHERE ticket_id = %s AND user_id = %s",
    (ticket_id, user_id)
)

conn.commit()
print("Ticket cancelled successfully!")

cur.close()
conn.close()
