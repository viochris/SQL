
from sqlalchemy import create_engine
import pandas as pd
import json
import urllib.parse
import os
from google.oauth2 import service_account
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Date

# Lokasi dari file JSON kunci service account
key_path = r"D:\Program Files\fifth-citadel-428301-k3-2afc36d9b323.json"

# Load the credentials from the JSON key file
with open(key_path) as f:
    credentials = json.load(f)

# Extract the project ID from the credentials
project_id = credentials.get('project_id')

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path

# Properly encode the credentials JSON
encoded_credentials = urllib.parse.quote_plus(json.dumps(credentials))

# Create the connection URL
connection_url = f'bigquery://{project_id}/?credentials_info={encoded_credentials}'

# Buat engine SQLAlchemy
engine = create_engine(connection_url)

metadata = MetaData()

# Definisikan tabel Customer untuk BigQuery (hanya contoh, tidak ada create_all() untuk BigQuery)
customer = Table(
    'Customer', metadata,
    Column('term', String),
    Column('week', Date),
    Column('score', Integer),
    Column('rank', Integer),
    Column('refresh_date', Date),
    Column('dma_name', String),
    Column('dma_id', Integer)
)

# Query yang ingin dieksekusi
query = """
    SELECT *
    FROM `bigquery-public-data.google_trends.top_terms`
    WHERE term LIKE 'Aaron%'
    LIMIT 10
"""
# Menggunakan connection dari engine
connection = engine.raw_connection()

# Eksekusi query dan ambil hasilnya sebagai DataFrame
results_df = pd.read_sql(query, connection)

# Tampilkan DataFrame
print(results_df)

# Tutup koneksi
engine.dispose()
