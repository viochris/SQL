from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text
import pandas as pd


engine = create_engine('mysql://root:@localhost/pembelian_shopee')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

df = pd.read_sql('select * from sku_detail', engine)


print(df.head())