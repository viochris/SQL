library(bigrquery)
library(dplyr)

# Atur path ke JSON kunci service account
Sys.setenv(GOOGLE_APPLICATION_CREDENTIALS="D:\\Program Files\\fifth-citadel-428301-k3-2afc36d9b323.json")

# Buat koneksi BigQuery
project <- "fifth-citadel-428301-k3"  # Ganti dengan ID proyek Anda


# Query yang ingin dieksekusi
query <- "SELECT * FROM `bigquery-public-data.google_trends.top_terms` LIMIT 10"

# Eksekusi query
query_result <- project %>% bq_project_query(query)

# Ambil hasil query dan konversi ke DataFrame R
result_df <- bq_table_download(query_result)

# Tampilkan DataFrame
print(result_df)
