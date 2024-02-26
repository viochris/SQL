from sqlalchemy import create_engine, Table, Column, VARCHAR, MetaData, Integer as int
import pyodbc

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
    Column('customer_id', int, primary_key=True),
    Column('first_name', VARCHAR(255)),
    Column('last_name', VARCHAR(255)),
    Column('phone', VARCHAR(25)),
    Column('email', VARCHAR(255)),
    Column('street', VARCHAR(255)),
    Column('city', VARCHAR(50)),
    Column('state', VARCHAR(25)),
    Column('zip_code', VARCHAR(5)),
    schema='sales'
)

connection = engine.connect()

result = connection.execute(customers.select())

for row in result:
    print(row)
    
    
# with engine.connect() as connection:
#     result = connection.execute(sku_detail.select())

#     # Cetak hasil
#     for row in result:
#         print(row)

connection.close()
