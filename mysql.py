import mysql.connector as msql
from mysql.connector import Error
import pandas as pd

# Assuming sales is a pandas DataFrame containing the data
sales = pd.read_csv('superstore_dataset.csv')

conn = None
cursor = None

try:
    # Connect to MySQL database
    conn = msql.connect(host='localhost', database='superstore', user='root')

    if conn.is_connected():
        cursor = conn.cursor()

        # Check if the 'superstore' database exists; if not, create it
        cursor.execute("CREATE DATABASE IF NOT EXISTS superstore")
        cursor.execute("USE superstore")

        # Drop the table if it exists and discard the tablespace
        cursor.execute('DROP TABLE IF EXISTS sales;')
        cursor.execute('CREATE TABLE IF NOT EXISTS sales ('
                       'OrderDate DATE,'
                       'Segment VARCHAR(255),'
                       'Country VARCHAR(255),'
                       'City VARCHAR(255),'
                       'State VARCHAR(255),'
                       'Region VARCHAR(255),'
                       'ProductID VARCHAR(50),'
                       'Category VARCHAR(50),'
                       'ProductName VARCHAR(255),'
                       'Sales DECIMAL(10, 2),'
                       'Quantity INT,'
                       'Discount DECIMAL(4, 2),'
                       'Profit DECIMAL(10, 2)'
                       ') ENGINE=InnoDB;')
        print("sales table is created....")

        # Assuming sales is a pandas DataFrame containing the data
        for i, row in sales.iterrows():
            sql = "INSERT INTO sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")

        # Commit changes to the database
        conn.commit()
        print("Changes committed")

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    # Close the cursor and connection
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
        print("MySQL connection closed")