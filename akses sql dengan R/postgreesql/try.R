# Load the RPostgreSQL library
library(RPostgreSQL)
library(dplyr)

# Isi informasi koneksi ke database PostgreSQL
host <- "localhost" # Ganti dengan host database Anda
port <- 5432 # Port default PostgreSQL
dbname <- "Shopee" # Ganti dengan nama database Anda
user <- "postgres" # Ganti dengan nama pengguna database Anda
password <- "S1LV1Ooo" # Ganti dengan password database Anda

# Buat koneksi
con <- dbConnect(RPostgres::Postgres(),
    dbname = dbname,
    host = host,
    port = port,
    user = user,
    password = password
)

# Execute the query
result <- dbGetQuery(con, "SELECT * FROM customer_detail")

# Print the result
print(head(result))

# Close the connection
dbDisconnect(con)

result$registered_date <- as.Date(result$registered_date, "%Y-%m-%d")
hasil <- result%>%
    group_by(id)%>% 
    summarise(pembelian_pertama = min(registered_date))
print(hasil)