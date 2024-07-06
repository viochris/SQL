import snowflake.connector

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

# Mendapatkan hasil
for row in cur:
    print(row)

# Menutup kursor dan koneksi
cur.close()
conn.close()
