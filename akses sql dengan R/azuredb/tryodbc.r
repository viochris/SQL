# Muat paket odbc
library(odbc)

# Informasi koneksi
server <- 'tcp:dbofsilvio.database.windows.net,1433'
database <- 'MysampleDATABASE'
username <- 'CloudSA68811ae3'
password <- 'S1LV1Oooo'

# Buat koneksi
conn <- dbConnect(odbc::odbc(), 
                  Driver = "ODBC Driver 17 for SQL Server", 
                  Server = server, 
                  Database = database, 
                  UID = username, 
                  PWD = password, 
                  Port = 1433)

# Query untuk menarik data
query <- "SELECT * FROM SalesLT.Customer"

# Tarik data dan masukkan ke dalam data frame
df <- dbGetQuery(conn, query)

# Tutup koneksi
dbDisconnect(conn)

# Tampilkan data
print(head(df))
