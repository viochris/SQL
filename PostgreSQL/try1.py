import psycopg2

# Buat koneksi ke PostgreSQL
conn_postgresql = psycopg2.connect(
    dbname="Shopee",
    user="postgres",
    password="S1LV1Ooo",
    host="localhost"
)

# Buat kursor
cur_postgresql = conn_postgresql.cursor()

# Eksekusi query
cur_postgresql.execute("SELECT * FROM sku_detail")

# Ambil hasil
rows_postgresql = cur_postgresql.fetchall()
for row in rows_postgresql:
    print(row)

# Tutup koneksi
conn_postgresql.close()
