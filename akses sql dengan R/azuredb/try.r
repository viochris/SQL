# Muat paket RODBC
library(RODBC)

# Informasi koneksi
server <- 'tcp:dbofsilvio.database.windows.net,1433'
database <- 'MysampleDATABASE'
username <- 'CloudSA68811ae3'
password <- 'S1LV1Oooo'

# Buat string koneksi
connection_string <- paste0("Driver={ODBC Driver 17 for SQL Server};Server=", server, 
                            ";Database=", database, ";Uid=", username, ";Pwd=", password)

# Buat koneksi
conn <- odbcDriverConnect(connection_string)

# Query untuk menarik data
query <- "SELECT * FROM SalesLT.Customer"

# Tarik data dan masukkan ke dalam data frame
df <- sqlQuery(conn, query)

# Tutup koneksi
close(conn)

# Tampilkan data
print(head(df))
