from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text, Date, Integer as Int, DateTime
import pandas as pd


engine = create_engine('sqlite:///data latihan.db')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

metadata = MetaData()

sku = Table(
    'sku_detail', metadata,
    Column('id', Text, primary_key=True),
    Column('sku_name', Text),
    Column('base_price', Float),
    Column('cogs', Float),
    Column('category', Text)
)

order = Table(
    'order_detail', metadata,
    Column('id', Text, primary_key=True),
    Column('customer_id', Text),
    Column('order_date', DateTime),
    Column('sku_id', Text),
    Column('price', Int),
    Column('qty_ordered', Int),
    Column('before_discount', Float),
    Column('discount_amount', Float),
    Column('after_discount', Float),
    Column('is_gross', Int),
    Column('is_valid', Int),
    Column('is_net', Int),
    Column('payment_id', Int)
)


connection = engine.connect()

sku_result = connection.execute(sku.select())
order_result = connection.execute(order.select())

df_sku = pd.DataFrame(sku_result.fetchall(), columns=sku_result.keys())
df_order = pd.DataFrame(order_result.fetchall(), columns=order_result.keys())

connection.close()

print(df_sku.head())
print()
print(df_order.head())