from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text, Date, Integer as Int
import pandas as pd


engine = create_engine('sqlite:///data latihan.db')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

# Menggunakan connection dari engine
connection = engine.raw_connection()

df_sku = pd.read_sql('select * from sku_detail', connection)
df_order = pd.read_sql('select * from order_detail', connection)

print(df_sku.head())
print()
print(df_order.head())