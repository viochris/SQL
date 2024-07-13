import pandas as pd
from sqlalchemy import create_engine

# Path ke database SQLite
db_path = r'C:\Users\Silvio\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db'

# Membuat URL koneksi untuk SQLAlchemy
db_url = f'sqlite:///{db_path}'

# Membuat engine SQLAlchemy
engine = create_engine(db_url)

# Menggunakan connection dari engine
connection = engine.raw_connection()

# Menjalankan query dan menyimpan hasil ke DataFrame
query = "SELECT * FROM Customer"
df = pd.read_sql(query, con=connection)

# Menampilkan hasil
print(df.head())

# Menutup koneksi (engine)
engine.dispose()
