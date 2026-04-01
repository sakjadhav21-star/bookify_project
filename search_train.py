from db_connect import get_connection

conn = get_connection()
cur = conn.cursor()

source = input("Enter Source Station Name: ")
destination = input("Enter Destination Station Name: ")

cur.execute("""
    SELECT tr.train_id, tr.train_name, s1.station_name, s2.station_name
    FROM Train tr
    JOIN Ticket t ON tr.train_id = t.train_id
    JOIN Station s1 ON t.source_id = s1.station_id
    JOIN Station s2 ON t.destination_id = s2.station_id
    WHERE s1.station_name = %s AND s2.station_name = %s
""", (source, destination))

result = cur.fetchall()

if result:
    print("Available Trains:")
    for row in result:
        print(row)
else:
    print("No trains found")

cur.close()
conn.close()