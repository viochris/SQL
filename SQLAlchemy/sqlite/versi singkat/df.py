from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text
import pandas as pd


engine = create_engine('sqlite:///data latihan.db')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

# Menggunakan connection dari engine
connection = engine.raw_connection()

df = pd.read_sql('select * from sku_detail', connection)


print(df.head())