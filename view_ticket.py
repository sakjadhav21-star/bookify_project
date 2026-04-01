from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

user_id = input("Enter your User ID: ")

cur.execute("""
    SELECT t.ticket_id, tr.train_name, s1.station_name, s2.station_name, t.travel_date, t.price
    FROM Ticket t
    JOIN Train tr ON t.train_id = tr.train_id
    JOIN Station s1 ON t.source_id = s1.station_id
    JOIN Station s2 ON t.destination_id = s2.station_id
    WHERE t.user_id = %s
""", (user_id,))

tickets = cur.fetchall()

print("Your Tickets:")
for ticket in tickets:
    print(ticket)

cur.close()
conn.close()