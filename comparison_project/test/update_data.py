import sqlite3

conn = sqlite3.connect("Chinook.db")
cursor = conn.cursor()

cursor.execute("""
                UPDATE CUSTOMER_NEW
                SET EMAIL = 'puwadon.changed@mail.com'
                WHERE CUSTOMERID = 2
                """)




conn.commit()
conn.close()