import sqlite3

conn = sqlite3.connect("Chinook.db")
cursor = conn.cursor()

# Replace 'Customer' with your table name
cursor.execute("PRAGMA table_info(Customer_New)")
columns = cursor.fetchall()

# Display column details
for col in columns:
    print(f"Column {col[0]}: {col[1]} ({col[2]})")
    
conn.close()
