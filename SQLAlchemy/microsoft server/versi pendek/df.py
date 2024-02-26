import pyodbc
from sqlalchemy import create_engine, Table, Column, VARCHAR, MetaData, Integer
import pandas as pd

server = 'LAPTOP-0F1OJ0T4'  # Ganti dengan nama server Anda
database = 'BikeStores'  # Ganti dengan nama database Anda
trusted_connection = 'yes'  # Menggunakan otentikasi Windows

# Membuat koneksi menggunakan pyodbc
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};'
conn = pyodbc.connect(conn_str)

# Membuat engine SQLAlchemy dari koneksi pyodbc
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn_str)

df = pd.read_sql('SELECT * FROM sales.customers', engine)

print(df.head())
