import sqlite3
import os

# Verify the Sqlite file readable
print(os.path.exists('data/Chinook_Sqlite.sqlite'))

# Connect sqlite
conn = sqlite3.connect('data/Chinook_Sqlite.sqlite')
#conn = sqlite3.connect('data/Chinook_Sqlite.sqlite')
cursor = conn.cursor()

# Get all table in DB
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

#print(f"tables found: {tables}")

# Print all tables
for table in tables:
    print(f"table name :{table[0]}")
