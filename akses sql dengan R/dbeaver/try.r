library(DBI)
library(RSQLite)

# Path ke database SQLite
db_path <- "C:/Users/Silvio/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"

# Membuat koneksi ke database
con <- dbConnect(RSQLite::SQLite(), dbname = db_path)

# Menjalankan query
query <- "SELECT * FROM Customer"
df <- dbGetQuery(con, query)

# Menampilkan hasil
print(head(df))

# Menutup koneksi
dbDisconnect(con)
