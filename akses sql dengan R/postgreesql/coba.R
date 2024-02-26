# Install paket RPostgres jika belum terinstall
# install.packages("RPostgres")

library(RPostgres)

# Isi informasi koneksi ke database PostgreSQL
host <- "localhost"  # Ganti dengan host database Anda
port <- 5432         # Port default PostgreSQL
dbname <- "Shopee"   # Ganti dengan nama database Anda
user <- "postgres"   # Ganti dengan nama pengguna database Anda
password <- "S1LV1Ooo" # Ganti dengan password database Anda

# Buat koneksi
con <- dbConnect(RPostgres::Postgres(), 
                    dbname = dbname, 
                    host = host, 
                    port = port, 
                    user = user, 
                    password = password)

# Cek apakah koneksi berhasil
if (dbIsValid(con)) {
    cat("Berhasil tersambung ke database PostgreSQL!\n")
} else {
    cat("Gagal tersambung ke database PostgreSQL.\n")
}

# Sekarang Anda dapat melakukan query ke database menggunakan koneksi 'con'
# Misalnya:
# dbGetQuery(con, "SELECT * FROM nama_tabel")

# Jangan lupa untuk menutup koneksi setelah selesai menggunakan database
# dbDisconnect(con)
