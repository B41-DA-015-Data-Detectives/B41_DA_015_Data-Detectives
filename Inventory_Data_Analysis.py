#!/usr/bin/env python
# coding: utf-8

# # Import Required libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # load the Dataset

# In[2]:


salesfinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\SalesFINAL12312016.csv")
purchasefinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\PurchasesFINAL12312016.csv")
invoicepurchase = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\InvoicePurchases12312016.csv")
endfinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\EndInvFINAL12312016.csv")
begfinal = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\BegInvFINAL12312016.csv")
purchase2017 = pd.read_csv(r"G:\My Drive\Construct Week Data Analytics Project\2017PurchasePricesDec.csv")


# # salesfinal Data

# In[3]:


salesfinal.head()


# In[4]:


salesfinal.shape


# # Checking Missing values

# In[5]:


salesfinal.isnull().sum()


# In[6]:


salesfinal.info()


# In[7]:


# Convert SalesDate to datetime format
salesfinal['SalesDate'] = pd.to_datetime(salesfinal['SalesDate'], errors='coerce')


# In[8]:


salesfinal.info()


# In[9]:


# Check for duplicate rows
print("Number of Duplicate Rows:", salesfinal.duplicated().sum())

# Drop duplicates
#df = salesfinal.drop_duplicates()
#print("Duplicates Removed.")


# In[56]:


# Save the cleaned dataset
salesfinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\salesfinal_cleaned.csv', index=False)


# # purchasefinal Data

# In[10]:


purchasefinal.head()


# In[11]:


purchasefinal.shape


# In[12]:


purchasefinal.isnull().sum()


# In[13]:


purchasefinal.info()


# In[14]:


# Convert date columns to datetime format
date_columns = ['PODate', 'ReceivingDate', 'InvoiceDate', 'PayDate']
for col in date_columns:
    purchasefinal[col] = pd.to_datetime(purchasefinal[col], errors='coerce')


# In[15]:


purchasefinal.dropna(subset=['Size'], inplace=True)


# In[16]:


purchasefinal.info()


# In[17]:


purchasefinal.isnull().sum()


# In[18]:


print("Number of Duplicate Rows:", purchasefinal.duplicated().sum())


# In[55]:


# Save the cleaned dataset
purchasefinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchasefinal_cleaned.csv', index=False)


# In[ ]:





# # invoicepurchase Data

# In[19]:


invoicepurchase.head()


# In[20]:


invoicepurchase.shape


# In[21]:


invoicepurchase.info()


# In[22]:


invoicepurchase.isnull().sum()


# In[23]:


missing_percentage = (invoicepurchase['Approval'].isnull().sum() / len(invoicepurchase)) * 100
print(f"Missing Approval Data: {missing_percentage:.2f}%")


# In[24]:


# Drop the Approval column
invoicepurchase.drop(columns=['Approval'], inplace=True)

# Verify the column has been removed
print(invoicepurchase.columns)


# In[25]:


invoicepurchase.isnull().sum()


# In[26]:


date_columns = ['InvoiceDate', 'PODate', 'PayDate']
for col in date_columns:
    invoicepurchase[col] = pd.to_datetime(invoicepurchase[col])


# In[27]:


invoicepurchase.info()


# In[28]:


invoicepurchase.head()


# In[29]:


print("Number of Duplicate Rows:", invoicepurchase.duplicated().sum())


# In[54]:


# Save the cleaned dataset
invoicepurchase.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\invoicepurchase_cleaned.csv', index=False)


# # endfinal Data

# In[31]:


endfinal.head()


# In[32]:


endfinal.shape


# In[33]:


endfinal.info()


# In[34]:


endfinal.isnull().sum()


# In[35]:


# Example: Fill missing cities based on the mode City for each Store
endfinal['City'] = endfinal.groupby('Store')['City'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 'Unknown'))


# In[36]:


endfinal.isnull().sum()


# In[37]:


# Convert 'endDate' column to datetime
endfinal['endDate'] = pd.to_datetime(endfinal['endDate'], errors='coerce')


# In[38]:


endfinal.info()


# In[39]:


print("Number of Duplicate Rows:", endfinal.duplicated().sum())


# In[57]:


# Save the cleaned dataset
endfinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\endfinal_cleaned.csv', index=False)


# # begfinal Data

# In[40]:


begfinal.head()


# In[41]:


begfinal.shape


# In[42]:


begfinal.isnull().sum()


# In[43]:


begfinal.info()


# In[44]:


# Convert 'endDate' column to datetime
begfinal['startDate'] = pd.to_datetime(begfinal['startDate'], errors='coerce')


# In[45]:


begfinal.info()


# In[46]:


print("Number of Duplicate Rows:", begfinal.duplicated().sum())


# In[58]:


# Save the cleaned dataset
begfinal.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\begfinal_cleaned.csv', index=False)


# # purchase2017 Data

# In[47]:


purchase2017.head()


# In[48]:


purchase2017.shape


# In[49]:


purchase2017.isnull().sum()


# In[50]:


purchase2017.info()


# In[51]:


purchase2017.dropna(subset=['Description', 'Size', 'Volume'], inplace=True)


# In[52]:


purchase2017.isnull().sum()


# In[53]:


print("Number of Duplicate Rows:", purchase2017.duplicated().sum())


# In[59]:


# Save the cleaned dataset
purchase2017.to_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchase2017_cleaned.csv', index=False)


# # Connect jupyter notebook to SQL workbench

# In[1]:


pip install mysql-connector-python pandas


# In[1]:


import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import urllib.parse


# In[3]:


pip install pymysql


# In[4]:


pip install mysql-connector-python


# In[5]:


import urllib.parse
username = 'root'
password = urllib.parse.quote_plus("@$Hishmukati9009847197")
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


# In[7]:


purchase2017_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchase2017_cleaned.csv')
begfinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\begfinal_cleaned.csv')
endfinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\endfinal_cleaned.csv')
invoicepurchase_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\invoicepurchase_cleaned.csv')
purchasefinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\purchasefinal_cleaned.csv')
salesfinal_df = pd.read_csv(r'G:\My Drive\Construct Week Data Analytics Project\salesfinal_cleaned.csv')


# In[9]:


# Create a connection to MySQL using SQLAlchemy
# Write data to MySQL
purchase2017_df.to_sql('purchase2017', con=engine, if_exists='replace', index=False)
begfinal_df.to_sql('begfinal', con=engine, if_exists='replace', index=False)
endfinal_df.to_sql('endfinal', con=engine, if_exists='replace', index=False)
invoicepurchase_df.to_sql('invoicepurchase', con=engine, if_exists='replace', index=False)
purchasefinal_df.to_sql('purchasefinal', con=engine, if_exists='replace', index=False)
salesfinal_df.to_sql('salesfinal', con=engine, if_exists='replace', index=False)
    


# In[ ]:





# In[ ]:





# In[ ]:




