import sqlite3
import pandas as pd

# Path ke database SQLite
db_path = r'C:\Users\Silvio\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'

# Membuat koneksi ke database
conn = sqlite3.connect(db_path)

# Membuat cursor
cur = conn.cursor()

# Menjalankan query
cur.execute("SELECT * FROM Customer")

# Mengambil semua baris hasil query
rows = cur.fetchall()

# Menampilkan hasil
for row in rows:
    print(row)

# Menutup koneksi
conn.close()
