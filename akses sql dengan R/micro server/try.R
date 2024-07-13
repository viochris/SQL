library(RODBC)

# Ganti nilai-nilai berikut sesuai dengan informasi koneksi Anda
server <- "LAPTOP-0F1OJ0T4"
database <- "BikeStores"
trusted_connection <- TRUE

# Membuat string koneksi
conn_str <- paste0(
  "Driver={ODBC Driver 17 for SQL Server};",
  "Server=", server, ";",
  "Database=", database, ";",
  "Trusted_Connection=", ifelse(trusted_connection, "yes", "no")
)

# Membuat koneksi
conn <- odbcDriverConnect(conn_str)

# Contoh query
query <- "SELECT * FROM sales.customers"

# Mengeksekusi query
result <- sqlQuery(conn, query)

# Menutup koneksi
odbcClose(conn)

# Tampilkan hasil
print(head(result,5))


