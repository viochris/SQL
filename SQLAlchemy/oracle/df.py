from sqlalchemy import create_engine
import pandas as pd
import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="D:/Downloads/instantclient-basic-windows.x64-12.1.0.2.0/instantclient_12_1")

# Informasi koneksi
username = 'SYSTEM'
password = 'S1LV1Ooo'
host = 'localhost'
port = '1521'
sid = 'xe'

# Membuat URL koneksi
connection_url = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

# Membuat engine
engine = create_engine(connection_url)

# Eksekusi kueri dan simpan hasil dalam DataFrame
query = "SELECT * FROM order_detail"
df = pd.read_sql(query, con=engine)

# Menampilkan DataFrame
print(df)
print(df.dtypes)

# Tutup koneksi
engine.dispose()
