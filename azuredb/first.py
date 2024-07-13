import pyodbc

# Informasi koneksi
server = 'tcp:dbofsilvio.database.windows.net,1433'
database = 'MysampleDATABASE'
username = 'CloudSA68811ae3'
password = 'S1LV1Oooo'

# Membuat koneksi
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

# Membuat cursor
cursor = conn.cursor()

# Menjalankan query
cursor.execute("SELECT TOP 10 * FROM SalesLT.Product")

# Mendapatkan hasil
for row in cursor.fetchall():
    print(row)

# Menutup koneksi
conn.close()
