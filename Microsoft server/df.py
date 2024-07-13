import pyodbc
import pandas as pd

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-0F1OJ0T4;'
    'DATABASE=BikeStores;'
    'Trusted_Connection=yes;'  # Menggunakan otentikasi Windows
)

query = "SELECT * FROM sales.customers"

df = pd.read_sql(query, conn)
conn.close()
print(df.head())