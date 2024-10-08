import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian')
sql1 = "SELECT * FROM orders"
sql2 = "SELECT * FROM customers"
df1 = pd.read_sql(sql1, connection)
df2 = pd.read_sql_query(sql2, connection)

# print(df1)
# print(df2)


df = pd.merge(df1, df2, on='customer_id', how='outer')
print(df)
print(df[df.isnull().any(axis = 1)])
print(df[df['order_id'].isnull()])
print(df[df['order_id'].isna()])
# akhir = pd.isna(df['order_id'])
# print(df[akhir])