from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, Text

# Buat koneksi ke PostgreSQL dengan SQLAlchemy
engine = create_engine('postgresql://postgres:S1LV1Ooo@localhost/Shopee')

# Inisialisasi metadata
metadata = MetaData()

# Definisikan tabel sku_detail
sku_detail = Table(
    'sku_detail', metadata,
    Column('id', Text, primary_key=True),
    Column('sku_name', Text),
    Column('base_price', Float),
    Column('cogs', Float),
    Column('category', Text)
)

# Buat tabel di database (jika belum ada)
metadata.create_all(engine)

connection = engine.connect()
result = connection.execute(sku_detail.select())

for row in result:
    print(row)

# Tutup koneksi
engine.dispose()
