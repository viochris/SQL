from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import pandas as pd

# Path ke database SQLite
db_path = r'C:\Users\Silvio\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'

# Membuat URL koneksi untuk SQLAlchemy
db_url = f'sqlite:///{db_path}'

# Membuat engine SQLAlchemy
engine = create_engine(db_url)

# Inisialisasi metadata
metadata = MetaData()

# Definisikan tabel Customer
customer_table = Table(
    'Customer', metadata,
    Column('CustomerId', Integer, primary_key=True),
    Column('FirstName', String(50)),
    Column('LastName', String(50)),
    Column('Company', String(50)),
    Column('Address', String(100)),
    Column('City', String(50)),
    Column('State', String(50)),
    Column('Country', String(50)),
    Column('PostalCode', String(50)),
    Column('Phone', String(50)),
    Column('Fax', String(50)),
    Column('Email', String(100)),
    Column('SupportRepId', Integer)
)

# Buat tabel di database (jika belum ada)
metadata.create_all(engine)

# Buka koneksi
with engine.connect() as connection:
    # Query data dari tabel Customer
    query = customer_table.select()
    
    # Eksekusi query
    result = connection.execute(query)
    
    # Ambil hasil dan simpan ke DataFrame
    df = pd.DataFrame(result.fetchall(), columns=result.keys())
    print(df)
