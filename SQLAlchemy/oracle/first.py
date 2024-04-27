from sqlalchemy import create_engine, Table, Column, Float, String, MetaData, DateTime, Numeric

# Inisialisasi klien Oracle
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="D:/Downloads/instantclient-basic-windows.x64-12.1.0.2.0/instantclient_12_1")

# Buat koneksi ke database Oracle
username = 'SYSTEM'
password = 'S1LV1Ooo'
host = 'localhost'
port = '1521'
sid = 'xe'
connection_url = f'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(connection_url)

metadata = MetaData()

# Buat tabel sku_detail
sku_detail = Table(
    'order_detail', metadata,
    Column('id', String(100), primary_key=True),
    Column('customer_id', String(100)),
    Column('order_date', DateTime),
    Column('sku_id', String(100)),
    Column('price', Numeric),
    Column('qty_ordered', Numeric),
    Column('before_discount', Float),
    Column('discount_amount', Float),
    Column('after_discount', Float),
    Column('is_gross', Numeric),
    Column('is_valid', Numeric),
    Column('is_net', Numeric),
    Column('payment_id', Numeric)
)

# Buat tabel di database
metadata.create_all(engine)


# Buka koneksi
with engine.connect() as connection:
    # Eksekusi kueri untuk menampilkan semua data dalam tabel sku_detail
    result = connection.execute(sku_detail.select())

    # Cetak hasil
    for row in result:
        print(row)

# Tutup koneksi
engine.dispose()
