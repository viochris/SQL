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

metadata = MetaData()

customers = Table(
    'customers', metadata,
    Column('customer_id', Integer, primary_key=True),
    Column('first_name', VARCHAR(255)),
    Column('last_name', VARCHAR(255)),
    Column('phone', VARCHAR(25)),
    Column('email', VARCHAR(255)),
    Column('street', VARCHAR(255)),
    Column('city', VARCHAR(50)),
    Column('state', VARCHAR(25)),
    Column('zip_code', VARCHAR(5)),
    schema='sales'  # Menambahkan parameter schema untuk menyesuaikan dengan skema 'sales'
)


# Membuat koneksi dan eksekusi query
connection = engine.connect()
result = connection.execute(customers.select())
df = pd.DataFrame(result.fetchall(), columns=result.keys())

print(df.head())
