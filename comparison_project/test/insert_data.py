import sqlite3

data = [
    (1, "Puw", "Ham", "None", "puw@mail.com", 3),
    (2, "Leonie", "Köhler", "None", "leonekohler@surfeu.de", 5),
    (3, "Puw2", "Ham2", "+55 (12) 3923-5566", "Puw2@mail.com", 5),
    (4, "Bjørn", "Hansen", "None", "bjorn.hansen@yahoo.no", 4),
    (5, "Puw3", "Ham3", "+420 2 4172 5555", "Puw3@exam.com", 4),
]

conn = sqlite3.connect("Chinook.db")
cursor = conn.cursor()

cursor.execute("""INSERT INTO Customer_New SELECT * FROM Customer""")

#cursor.execute("PRAGMA table_info(CUSTOMER_NEW)")
#for row in cursor.fetchall():
#    print(row)


#cursor.executemany("""INSERT INTO CUSTOMER_NEW (CUSTOMERID, FIRSTNAME, LASTNAME, FAX, EMAIL, SUPPORTREPID) VALUES (?, ?, ?, ?, ?, ?)""", 
#                   data)


conn.commit()
conn.close()