from sqlalchemy import create_engine, Table, Column, VARCHAR, MetaData, Integer, String, Numeric, Date
import pyodbc

# Informasi koneksi
server = 'tcp:dbofsilvio.database.windows.net,1433'
database = 'MysampleDATABASE'
username = 'CloudSA68811ae3'
password = 'S1LV1Oooo'

# Membuat koneksi menggunakan pyodbc
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)

# Membuat engine SQLAlchemy dari koneksi pyodbc
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn_str)

metadata = MetaData()

products = Table(
    'Product', metadata,
    Column('ProductID', Integer, primary_key=True),
    Column('Name', String(255)),
    Column('ProductNumber', String(50)),
    Column('Color', String(50)),
    Column('StandardCost', Numeric(12, 2)),
    Column('ListPrice', Numeric(12, 2)),
    Column('Size', String(20)),
    Column('Weight', Numeric(10, 2)),
    Column('ProductCategoryID', Integer),
    Column('ProductModelID', Integer),
    Column('SellStartDate', Date),
    Column('SellEndDate', Date),
    Column('DiscontinuedDate', Date),
    Column('ThumbNailPhoto', String(255)),
    Column('ThumbnailPhotoFileName', String(255)),
    Column('rowguid', String(36)),
    Column('ModifiedDate', Date),
    schema='SalesLT'  # Menambahkan parameter schema untuk menyesuaikan dengan skema 'sales'
)

connection = engine.connect()

result = connection.execute(products.select())

for row in result:
    print(row)
    
    
# with engine.connect() as connection:
#     result = connection.execute(sku_detail.select())

#     # Cetak hasil
#     for row in result:
#         print(row)

connection.close()
