library(bigrquery)

# Set path to JSON service account key
Sys.setenv(GOOGLE_APPLICATION_CREDENTIALS="D:\\Program Files\\fifth-citadel-428301-k3-2afc36d9b323.json")

# Tentukan proyek dan dataset BigQuery
project_id <- "fifth-citadel-428301-k3"
dataset_id <- "bigquery-public-data"

# Query yang ingin dieksekusi
query <- "
SELECT *
FROM `bigquery-public-data.google_trends.top_terms`
LIMIT 10
"

# Eksekusi query dan simpan hasilnya
df <- bq_table_download(bq_project_query(project_id, query))
print(df)