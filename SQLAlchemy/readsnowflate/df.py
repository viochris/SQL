from sqlalchemy import create_engine, text
import pandas as pd


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

# Query SQL
query = text("SELECT * FROM CATALOG_PAGE")

# Eksekusi query menggunakan engine dan simpan hasil ke DataFrame
result_proxy = engine.execute(query)
df = pd.DataFrame(result_proxy.fetchall(), columns=result_proxy.keys())

# Menampilkan DataFrame
print(df)

# Tutup koneksi setelah selesai
engine.dispose()  # Close all connections in the connection pool
