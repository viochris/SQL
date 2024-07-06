from sqlalchemy import Column, Integer, String, create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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

Base = declarative_base()

# Use MetaData to specify schema explicitly
metadata = MetaData(schema='TPCDS_SF100TCL')

# Define the table with the correct schema and column names
class CatalogPage(Base):
    __table__ = Table('CATALOG_PAGE', metadata,
                      Column('cp_catalog_page_sk', Integer, primary_key=True),
                      Column('cp_catalog_page_id', String),
                      Column('cp_start_date_sk', Integer),
                      Column('cp_end_date_sk', Integer),
                      Column('cp_department', String),
                      Column('cp_catalog_number', Integer),
                      Column('cp_catalog_page_number', Integer),
                      Column('cp_description', String),
                      Column('cp_type', String),
                      autoload_with=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Run query using ORM
results = session.query(CatalogPage).all()
for instance in results:
    print(f"Catalog Page SK: {instance.cp_catalog_page_sk}, "
          f"Catalog Page ID: {instance.cp_catalog_page_id}, "
          f"Start Date SK: {instance.cp_start_date_sk}, "
          f"End Date SK: {instance.cp_end_date_sk}, "
          f"Department: {instance.cp_department}, "
          f"Catalog Number: {instance.cp_catalog_number}, "
          f"Catalog Page Number: {instance.cp_catalog_page_number}, "
          f"Description: {instance.cp_description}, "
          f"Type: {instance.cp_type}")
# Close session
session.close()
