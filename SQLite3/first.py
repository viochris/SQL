import sqlite3
import pandas as pd

conn = sqlite3.connect('data latihan.db')

cur = conn.cursor()

cur.execute("SELECT * FROM sku_detail")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()

