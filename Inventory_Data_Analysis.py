# # Import Required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # load the Dataset

salesfinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\SalesFINAL12312016.csv")
purchasefinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\PurchasesFINAL12312016.csv")
invoicepurchase = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\InvoicePurchases12312016.csv")
endfinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\EndInvFINAL12312016.csv")
begfinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\BegInvFINAL12312016.csv")
purchase2017 = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\2017PurchasePricesDec.csv")


# # salesfinal Data
salesfinal.head()

salesfinal.shape

# # Checking Missing values

salesfinal.isnull().sum()

salesfinal.info()

# Convert SalesDate to datetime format
salesfinal['SalesDate'] = pd.to_datetime(salesfinal['SalesDate'], errors='coerce')
salesfinal.info()

# Check for duplicate rows
print("Number of Duplicate Rows:", salesfinal.duplicated().sum())

# Drop duplicates
#df = salesfinal.drop_duplicates()
#print("Duplicates Removed.")

# Save the cleaned dataset
salesfinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\salesfinal_cleaned.csv', index=False)


# # purchasefinal Data

purchasefinal.head()

purchasefinal.shape

purchasefinal.isnull().sum()

purchasefinal.info()

# Convert date columns to datetime format
date_columns = ['PODate', 'ReceivingDate', 'InvoiceDate', 'PayDate']
for col in date_columns:
    purchasefinal[col] = pd.to_datetime(purchasefinal[col], errors='coerce')

purchasefinal.dropna(subset=['Size'], inplace=True)

purchasefinal.info()

purchasefinal.isnull().sum()

print("Number of Duplicate Rows:", purchasefinal.duplicated().sum())

# Save the cleaned dataset
purchasefinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchasefinal_cleaned.csv', index=False)

# # invoicepurchase Data

invoicepurchase.head()

invoicepurchase.shape

invoicepurchase.info()

invoicepurchase.isnull().sum()

missing_percentage = (invoicepurchase['Approval'].isnull().sum() / len(invoicepurchase)) * 100
print(f"Missing Approval Data: {missing_percentage:.2f}%")

# Drop the Approval column
invoicepurchase.drop(columns=['Approval'], inplace=True)

# Verify the column has been removed
print(invoicepurchase.columns)

invoicepurchase.isnull().sum()

date_columns = ['InvoiceDate', 'PODate', 'PayDate']
for col in date_columns:
    invoicepurchase[col] = pd.to_datetime(invoicepurchase[col])

invoicepurchase.info()

invoicepurchase.head()

print("Number of Duplicate Rows:", invoicepurchase.duplicated().sum())

# Save the cleaned dataset
invoicepurchase.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\invoicepurchase_cleaned.csv', index=False)

# # endfinal Data
endfinal.head()

endfinal.shape

endfinal.info()

endfinal.isnull().sum()

# Example: Fill missing cities based on the mode City for each Store
endfinal['City'] = endfinal.groupby('Store')['City'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 'Unknown'))

endfinal.isnull().sum()

# Convert 'endDate' column to datetime
endfinal['endDate'] = pd.to_datetime(endfinal['endDate'], errors='coerce')

endfinal.info()

print("Number of Duplicate Rows:", endfinal.duplicated().sum())

# Save the cleaned dataset
endfinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\endfinal_cleaned.csv', index=False)


# # begfinal Data

begfinal.head()

begfinal.shape

begfinal.isnull().sum()

begfinal.info()

# Convert 'endDate' column to datetime
begfinal['startDate'] = pd.to_datetime(begfinal['startDate'], errors='coerce')

begfinal.info()

print("Number of Duplicate Rows:", begfinal.duplicated().sum())

# Save the cleaned dataset
begfinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\begfinal_cleaned.csv', index=False)

# # purchase2017 Data

purchase2017.head()

purchase2017.shape

purchase2017.isnull().sum()

purchase2017.info()

purchase2017.dropna(subset=['Description', 'Size', 'Volume'], inplace=True)

purchase2017.isnull().sum()

print("Number of Duplicate Rows:", purchase2017.duplicated().sum())

# Save the cleaned dataset
purchase2017.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchase2017_cleaned.csv', index=False)


# # Connect jupyter notebook to SQL workbench

pip install mysql-connector-python pandas
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import urllib.parse

pip install pymysql
pip install mysql-connector-python
import urllib.parse
username = 'root'
password = urllib.parse.quote_plus("@$Hishmukati")
host = 'localhost'
port = '3306'
database = 'inventory_db'
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(connection_string)
connection = engine.connect()
try:
    with engine.connect() as connection:
        print("Connection successful!")
        result = connection.execute(text("SELECT 1"))
        print(result.fetchone())  # Should print (1,)
except Exception as e:
    print(f"Error: {e}")
    
purchase2017_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchase2017_cleaned.csv')
begfinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\begfinal_cleaned.csv')
endfinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\endfinal_cleaned.csv')
invoicepurchase_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\invoicepurchase_cleaned.csv')
purchasefinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchasefinal_cleaned.csv')
salesfinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\salesfinal_cleaned.csv')

# Create a connection to MySQL using SQLAlchemy
# Write data to MySQL
purchase2017_df.to_sql('purchase2017', con=engine, if_exists='replace', index=False)
begfinal_df.to_sql('begfinal', con=engine, if_exists='replace', index=False)
endfinal_df.to_sql('endfinal', con=engine, if_exists='replace', index=False)
invoicepurchase_df.to_sql('invoicepurchase', con=engine, if_exists='replace', index=False)
purchasefinal_df.to_sql('purchasefinal', con=engine, if_exists='replace', index=False)
salesfinal_df.to_sql('salesfinal', con=engine, if_exists='replace', index=False)
    




