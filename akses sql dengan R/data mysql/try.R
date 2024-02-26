library(RMySQL)

# Ganti 'dbname', 'username', 'password', dan 'host' sesuai dengan informasi database Anda
con <- dbConnect(MySQL(), dbname = "pembelian", user = "root", password = "", host = "localhost")

query <- "SELECT * FROM customers"
df <- dbGetQuery(con, query)
dbDisconnect(con)

print(df)
