import sqlite3

conn = sqlite3.connect("Chinook.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE Customer_New AS SELECT * FROM Customer WHERE 0;")

conn.commit()
conn.close()