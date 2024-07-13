import pyodbc
from sqlalchemy import create_engine, Table, Column, VARCHAR, MetaData, Integer
import pandas as pd

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

# Menggunakan connection dari engine
connection = engine.raw_connection()

df = pd.read_sql('SELECT * FROM SalesLT.Customer', connection)


print(df.head())
