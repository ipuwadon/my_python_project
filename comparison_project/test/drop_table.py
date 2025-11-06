import sqlite3

conn = sqlite3.connect("Chinook.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS CUSTOMER_NEW")

conn.commit()
conn.close()