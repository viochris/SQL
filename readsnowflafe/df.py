import snowflake.connector
import pandas as pd

# Menghubungkan ke Snowflake
conn = snowflake.connector.connect(
    user='SILVIO',
    password='S1LV1Oooo',
    account='rf60339.ap-southeast-1'
)

# Membuat kursor
cur = conn.cursor()

# Menjalankan query
cur.execute("SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCDS_SF100TCL.CATALOG_PAGE")

# Mengambil semua hasil dan menyimpannya dalam DataFrame
df = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])

# Menutup kursor dan koneksi
cur.close()
conn.close()

# Menampilkan DataFrame
print(df)
