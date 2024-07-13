from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text
import pandas as pd

# Buat koneksi ke PostgreSQL dengan SQLAlchemy
engine = create_engine('postgresql://postgres:S1LV1Ooo@localhost/Shopee')

# Menggunakan connection dari engine
connection = engine.raw_connection()

df = pd.read_sql('select * from sku_detail', connection)

# Tutup koneksi
engine.dispose()
print(df.head())