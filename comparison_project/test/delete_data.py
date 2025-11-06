import sqlite3

conn = sqlite3.connect("Chinook.db")
cursor = conn.cursor()

# Replace 'Customer' with your table name
cursor.execute("DELETE FROM CUSTOMER_NEW WHERE CUSTOMERID = 1")

conn.commit()    
conn.close()