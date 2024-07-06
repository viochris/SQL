import pandas as pd
import sqlite3

# Path ke database SQLite
db_path = r'C:\Users\Silvio\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'

# Membuat koneksi ke database
conn = sqlite3.connect(db_path)

# Menjalankan query
query = "SELECT * FROM Customer"
df = pd.read_sql(query, con=conn)

# Menampilkan hasil
print(df.head())

# Menutup koneksi
conn.close()
