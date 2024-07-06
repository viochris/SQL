from sqlalchemy import create_engine

# Contoh penggunaan:
username = 'SILVIO'
password = 'S1LV1Oooo'
account_identifier = 'rf60339.ap-southeast-1'
database = 'SNOWFLAKE_SAMPLE_DATA'
schema = 'TPCDS_SF100TCL'
warehouse = 'COMPUTE_WH'
role = 'ACCOUNTADMIN'
# Membuat URL koneksi
engine = create_engine(
    f"snowflake://{username}:{password}@{account_identifier}/{database}/{schema}?warehouse={warehouse}&role={role}"
)

# # Membuat URL koneksi
# engine = create_engine(
#     'snowflake://SILVIO:S1LV1Oooo@rf60339.ap-southeast-1/SNOWFLAKE_SAMPLE_DATA/TPCDS_SF100TCL?warehouse=COMPUTE_WH&role=ACCOUNTADMIN'
# )

# Membuat koneksi
connection = engine.connect()

# Menjalankan query
result = connection.execute("SELECT * FROM CATALOG_PAGE")

# Menampilkan hasil
for row in result:
    print(row)

# Menutup koneksi
connection.close()
