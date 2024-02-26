library(RSQLite)

# Ganti 'nama_database.db' sesuai dengan nama basis data SQLite Anda
conn <- dbConnect(SQLite(), dbname = "data latihan.db")
# Contoh query
query <- "SELECT * FROM sku_detail"
result <- dbGetQuery(conn, query)


dbDisconnect(conn)
# Cetak hasil akhir
print(head(result, 5))
