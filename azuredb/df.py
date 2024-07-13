import pyodbc
import pandas as pd

# Informasi koneksi
server = 'tcp:dbofsilvio.database.windows.net,1433'
database = 'MysampleDATABASE'
username = 'CloudSA68811ae3'
password = 'S1LV1Oooo'

# Membuat koneksi
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

query = "SELECT * FROM SalesLT.Product"

df = pd.read_sql(query, conn)
conn.close()
print(df.head())