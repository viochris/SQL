library(odbc)

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
conn <- dbConnect(odbc::odbc(), .connection_string = conn_str)

# Contoh query
query <- "SELECT * FROM sales.customers"

# Mengeksekusi query
result <- dbGetQuery(conn, query)

# Menutup koneksi
dbDisconnect(conn)

# Tampilkan hasil
print(head(result, 5))
