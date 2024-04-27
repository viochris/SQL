import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="D:\Downloads\instantclient-basic-windows.x64-12.1.0.2.0\instantclient_12_1")

# Informasi koneksi
username = 'SYSTEM'
password = 'S1LV1Ooo'
host = 'localhost'
port = '1521'
sid = 'xe'

# Membuat koneksi
connection = cx_Oracle.connect(username, password, host + ':' + port + '/' + sid)

# Membuat kursor
cursor = connection.cursor()

# Contoh eksekusi kueri
cursor.execute("SELECT * FROM order_detail")

print('\n\n\n\n')

# Mendapatkan hasil
for row in cursor:
    print(row)

# Menutup kursor dan koneksi
cursor.close()
connection.close()
