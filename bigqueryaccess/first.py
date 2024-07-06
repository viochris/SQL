from google.cloud import bigquery

# Lokasi dari file JSON kunci service account
key_path = r"D:\Program Files\fifth-citadel-428301-k3-2afc36d9b323.json"

# Inisialisasi client BigQuery dengan kunci service account
client = bigquery.Client.from_service_account_json(key_path)

# Query yang ingin dieksekusi
query = """
    SELECT *
    FROM `bigquery-public-data.google_trends.top_terms`
    WHERE term LIKE 'Aaron%'
    LIMIT 10
"""

# Eksekusi query
query_job = client.query(query)

# Ambil hasil query
results = query_job.result()

# Loop untuk hasil query
for row in results:
    print(row)
