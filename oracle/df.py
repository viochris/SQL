import cx_Oracle
import pandas as pd

cx_Oracle.init_oracle_client(lib_dir="D:\Downloads\instantclient-basic-windows.x64-12.1.0.2.0\instantclient_12_1")

# Informasi koneksi
username = 'SYSTEM'
password = 'S1LV1Ooo'
host = 'localhost'
port = '1521'
sid = 'xe'

# Membuat koneksi
connection = cx_Oracle.connect(username, password, host + ':' + port + '/' + sid)

# Eksekusi kueri dan simpan hasil dalam DataFrame
query = "SELECT * FROM order_detail"
df = pd.read_sql(query, con=connection)


# Menampilkan DataFrame
print(df)

# Menutup koneksi
connection.close()
