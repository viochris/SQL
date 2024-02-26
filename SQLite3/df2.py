import sqlite3
import pandas as pd

conn = sqlite3.connect('data latihan.db')
connection = sqlite3.connect('latihan.db')

sql1 = "SELECT * FROM orders"
sql2 = "SELECT * FROM customer"
sql3 = "SELECT * FROM Popular_Baby_Names"
df1 = pd.read_sql(sql1, conn)
df2 = pd.read_sql(sql2, conn)
df3 = pd.read_sql(sql3, connection)
conn.close()

print(df1.head())
print(df2.head())
print(df3.head())