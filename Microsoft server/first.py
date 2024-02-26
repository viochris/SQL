import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-0F1OJ0T4;'
    'DATABASE=BikeStores;'
    'Trusted_Connection=yes;'  # Menggunakan otentikasi Windows
)
cur = conn.cursor()
cur.execute("SELECT * FROM sales.customers")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()
