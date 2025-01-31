import pandas as pd
import numpy as np
from datetime import date

data = pd.read_csv('C:\\Users\\Alba\\Downloads\\archive (1)\\Sample - Superstore.csv', encoding='latin1')

# Display the first 10 rows 
print(data.head(10))

# Display the last 10 rows 
print(data.tail(10))

# The number of rows and columns
num_rows, num_columns = data.shape

# Print the results
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# Count the number of missing values in each column
print(data.isnull().sum())

# Identify duplicates
print('Number of duplicates')
print(data.duplicated().sum())



# Removing the columns that won't be needed
columns_to_remove = ['Row ID', 'Order ID', 'Customer ID', 'Sub-Category', 'Customer Name', 'Postal Code', 'Ship Date', 'Ship Mode']
data = data.drop(columns=columns_to_remove)

#To confirm the removal of the columns
print("\nFinal Dataset Overview:")
print(data.head())
print(data.info())

# Types of data for each column
print('Data types: ')
print(data.dtypes)

# Assuming data is your DataFrame
data['Order Date'] = pd.to_datetime(data['Order Date'], format='%m/%d/%Y', errors='coerce')
data['Order Date'] = data['Order Date'].dt.strftime('%Y-%m-%d')

# Display the first few rows to verify the changes
print(data.head())

data.to_csv('superstore_dataset.csv', index=False)