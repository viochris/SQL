import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('data latihan.db')

# SQL query to select all columns from the "orders" table
sql_query = "SELECT * FROM orders"

# Read data from the "orders" table into a DataFrame
df = pd.read_sql_query(sql_query, conn)

# Close the connection to the database
conn.close()

# Print the first few rows of the DataFrame
print(df.head())
