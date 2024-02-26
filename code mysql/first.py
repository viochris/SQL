import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='', database='pembelian')

cur = conn.cursor()

cur.execute("SELECT * FROM customers")
rows = cur.fetchall()
for row in rows:
    print(row)
conn.close()