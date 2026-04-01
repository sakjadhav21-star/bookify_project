import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="bookify",
        user="postgres",
        password=input("Enter DB password: ")
    )
    return conn