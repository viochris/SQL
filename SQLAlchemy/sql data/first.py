from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text


engine = create_engine('mysql://root:@localhost/pembelian_shopee')
# engine = create_engine('mysql://root:password@localhost/pembelian_shopee')

metadata = MetaData()

users = Table(
    'sku_detail', metadata,
    Column('id', Text, primary_key=True),
    Column('sku_name', Text),
    Column('base_price', Float),
    Column('cogs', Float),
    Column('category', Text)
)


connection = engine.connect()
result = connection.execute(users.select())

for row in result:
    print(row)
    
    
# with engine.connect() as connection:
#     result = connection.execute(sku_detail.select())

#     # Cetak hasil
#     for row in result:
#         print(row)    

connection.close()