# Memuat library ROracle
library(ROracle)


# Informasi koneksi
username <- "SYSTEM"
password <- "S1LV1Ooo"
host <- "localhost"
port <- 1521
sid <- "xe"

# Membuat string koneksi
dsn <- paste("(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST =", host, ")(PORT =", port, "))(CONNECT_DATA = (SID =", sid, ")))", sep=" ")

# Membuat koneksi
connection <- dbConnect(dbDriver("Oracle"), username=username, password=password, dbname=dsn)

# Contoh eksekusi kueri
query <- "SELECT * FROM order_detail"
result <- dbSendQuery(connection, query)

# Mendapatkan hasil dan menyimpannya ke dalam data frame
data <- fetch(result)

# Menutup koneksi
dbClearResult(result)
dbDisconnect(connection)

# Menampilkan data frame
print(data)
