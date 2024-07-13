library(DBI)
library(odbc)

# Membuat koneksi
con <- dbConnect(odbc::odbc(),
                    Driver = "SnowflakeDSIIDriver",
                    Server = "rf60339.ap-southeast-1.snowflakecomputing.com",
                    UID = "SILVIO",
                    PWD = "S1LV1Oooo",
                    Database = "SNOWFLAKE_SAMPLE_DATA",
                    Schema = "TPCDS_SF100TCL",
                    Warehouse = "COMPUTE_WH",
                    Role = "ACCOUNTADMIN")

# Menjalankan query
result <- dbGetQuery(con, "SELECT * FROM CATALOG_PAGE")

# Menampilkan hasil
print(result)

# Menutup koneksi
dbDisconnect(con)
