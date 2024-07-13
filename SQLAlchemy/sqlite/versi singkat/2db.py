from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text, Date, Integer as Int
import pandas as pd


engine1 = create_engine('sqlite:///data latihan.db')
engine2 = create_engine('sqlite:///latihan.db')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

# Menggunakan connection dari engine
connection1 = engine1.raw_connection()
connection2 = engine2.raw_connection()

df_sku = pd.read_sql('select * from sku_detail', connection1)
df_order = pd.read_sql('select * from order_detail', connection1)
df_orders = pd.read_sql('select * from orders', connection2)

print(df_sku.head())
print(df_order.head())
print(df_orders.head())

