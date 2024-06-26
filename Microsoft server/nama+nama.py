import pandas as pd
import pyodbc

# Koneksi ke database SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=LAPTOP-0F1OJ0T4;'
    'DATABASE=BikeStores;'
    'Trusted_Connection=yes;'  # Menggunakan otentikasi Windows
)

# Definisikan kueri SQL
query = """
    SELECT
        ord.order_id,
        -- CONCAT(cus.first_name, ' ', cus.last_name) AS customer,
        cus.first_name,
        cus.last_name,
        cus.city, 
        cus.state, 
        ord.order_date,
        ite.quantity, 
        ite.list_price,
        pro.product_name, 
        cat.category_name,
        bra.brand_name,
        sto.store_name,
        CONCAT(sta.first_name, ' ', sta.last_name) AS sales_name
    FROM 
        sales.orders ord
    JOIN sales.customers cus ON ord.customer_id = cus.customer_id
    JOIN sales.order_items ite ON ord.order_id = ite.order_id
    JOIN production.products pro ON ite.product_id = pro.product_id
    JOIN production.categories cat ON pro.category_id = cat.category_id
    JOIN production.brands bra ON pro.brand_id = bra.brand_id
    JOIN sales.stores sto ON ord.store_id = sto.store_id
    JOIN sales.staffs sta ON ord.staff_id = sta.staff_id
"""

# Jalankan kueri SQL dan baca hasilnya ke dalam DataFrame
df = pd.read_sql(query, conn)

# Tampilkan DataFrame
print(df)

# Tutup koneksi database
conn.close()
df['revenue'] = df['quantity'] * df['list_price']
print(df)


hasil = df.groupby(['order_id', 'first_name', 'last_name', 'city', 'state', 'order_date', 'product_name', 'category_name', 'brand_name', 'store_name', 'sales_name'])[['quantity', 'revenue']].sum().reset_index()
print(hasil)

hasil['pelanggan'] = hasil['first_name'] + ' ' + hasil['last_name']
hasil['pelanggan2'] = hasil.apply(lambda x: " ".join([x.first_name, x.last_name]), axis=1)
hasil['pelanggan4'] = hasil.apply(lambda x: " ".join([x['first_name'], x['last_name']]), axis=1)
print(hasil.head())
print(hasil.pelanggan4.head())