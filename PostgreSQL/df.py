import psycopg2
import pandas as pd

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
columns = [desc[0] for desc in cur_postgresql.description]


df = pd.DataFrame(rows_postgresql, columns=columns)

# Tutup koneksi
conn_postgresql.close()
print(df.head())