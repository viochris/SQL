from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text, Date, Integer as Int
import pandas as pd


engine = create_engine('mysql://root:@localhost/pembelian_shopee')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

df_sku = pd.read_sql('select * from sku_detail', engine)
df_order = pd.read_sql('select * from order_detail', engine)

print(df_sku.head())
print()
print(df_order.head())