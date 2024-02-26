from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text, Date, Integer as Int
import pandas as pd


engine1 = create_engine('mysql://root:@localhost/pembelian_shopee')
engine2 = create_engine('mysql://root:@localhost/pembelian')
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
    Column('order_date', Date),
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

orders = Table(
    'orders', metadata,
    Column('order_id', Int, primary_key=True),
    Column('order_date', Date),
    Column('amount', Float),
    Column('salesman_id', Int),
    Column('customer_id', Int)
)



connection1 = engine1.connect()
connection2 = engine2.connect()


sku_result = connection1.execute(sku.select())
order_result = connection1.execute(order.select())
orders_result = connection2.execute(orders.select())

df_sku = pd.DataFrame(sku_result.fetchall(), columns=sku_result.keys())
df_order = pd.DataFrame(order_result.fetchall(), columns=order_result.keys())
df_orders = pd.DataFrame(orders_result.fetchall(), columns=orders_result.keys())

connection1.close()
connection2.close()

print(df_sku.head())
print(df_order.head())
print(df_orders.head())

