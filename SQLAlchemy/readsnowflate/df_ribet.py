from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String
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

# Mendapatkan metadata
metadata = MetaData()

# Definisi tabel
users = Table('CATALOG_PAGE', metadata,
                        Column('cp_catalog_page_sk', Integer, primary_key=True),
                        Column('cp_catalog_page_id', String),
                        Column('cp_start_date_sk', Integer),
                        Column('cp_end_date_sk', Integer),
                        Column('cp_department', String),
                        Column('cp_catalog_number', Integer),
                        Column('cp_catalog_page_number', Integer),
                        Column('cp_description', String),
                        Column('cp_type', String)
)

# Membuat tabel di database jika belum ada
metadata.create_all(engine)

# Contoh penggunaan tabel
with engine.connect() as conn:
    # Menjalankan query
    result = conn.execute(users.select())
    
    # Mengambil hasil query ke dalam DataFrame
    df = pd.DataFrame(result.fetchall(), columns=result.keys())
    
# Menampilkan DataFrame
print(df)