from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, DateTime, Numeric

# Path ke database SQLite
db_path = r'C:\Users\Silvio\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'

# Membuat URL koneksi untuk SQLAlchemy
db_url = f'sqlite:///{db_path}'

# Membuat engine SQLAlchemy
engine = create_engine(db_url)

metadata = MetaData()

# Definisikan tabel Customer (contoh)
customer = Table(
    'Customer', metadata,
    Column('CustomerId', Integer, primary_key=True),
    Column('FirstName', String(100)),
    Column('LastName', String(100)),
    Column('Company', String(100)),
    Column('Address', String(100)),
    Column('City', String(100)),
    Column('State', String(100)),
    Column('Country', String(100)),
    Column('PostalCode', String(20)),
    Column('Phone', String(100)),
    Column('Fax', String(100)),
    Column('Email', String(100)),
    Column('SupportRepId', Integer),
)

# Buat tabel di database
metadata.create_all(engine)

# Buka koneksi
with engine.connect() as connection:
    # Eksekusi kueri untuk menampilkan semua data dalam tabel Customer
    result = connection.execute(customer.select())

    # Cetak hasil
    for row in result:
        print(row)

# Tutup koneksi
engine.dispose()
