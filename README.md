# B41_DA_015_Data-Detectives

# Catch project presentation
Inventory Analysis:
Inventory data analysis is the process of examining and interpreting inventory-related data to optimize stock management and improve operational efficiency. It plays a crucial role in helping businesses maintain the right balance between supply and demand. By analyzing key metrics such as stock levels, inventory turnover, and reorder points, organizations can make data-driven decisions to minimize costs, reduce waste, and enhance customer satisfaction.

This analysis leverages historical and real-time data to identify patterns, forecast future demand, 
and pinpoint inefficiencies such as overstocking or stock-outs. Advanced tools like Power BI 
enable businesses to visualize inventory trends and track key performance indicators (KPIs) 
through interactive dashboards, ensuring timely and informed decision-making.
## Table of Contents
1. Project Overview
2. Folder Structure
3. Technologies Used
4. Setup Instructions
5. Files Overview
6. How to Run
7. Power-BI Dashboard Images

## Project Overview
The Inventory Analysis Project is designed to analyze and manage inventory data for a business, offering insights into purchase prices, sales, and stock levels. This project utilizes Google Drive API to fetch files,
processes the data using Python, and loads it into a MySQL database for storage and analysis. The final goal is to create dashboards and visualizations in Power BI.

## Technologies Used
- Python: For data processing, manipulation, and integration with Google Drive and MySQL.
- Pandas: To handle and clean data within Python.
- Google Drive API: Used to fetch data files from Google Drive.
- MySQL: For database storage and data analysis.
- Jupyter Notebook: Used for data cleaning and exploratory data analysis (EDA).
- Power BI: For visualization and dashboard creation.

## Setup Instructions
1. Import required libraries
import numpy as np
import pandas as pd

### 2. import dataset 
dataset = pd.read_csv(r"")


### 3. Install Dependencies Install all necessary libraries from the requirements.txt file:
``` bash
pip install -r requirements.txt
```
### 5.Database Setup
- Ensure MySQL server is installed and running.
- Create a new database called inventory_analysis in MySQL.
- Update the load_to_sql.py file with your MySQL username and password to connect to the database.

### 6. Files Overview
Organize the cleaned datasets into six structured tables:

1. begfinal_cleaned
2. invoicepurchase_cleaned
3. purchase2017_cleaned
4. purchasefinal_cleaned
5. endfinal_cleaned
6. salesfinal_cleaned


### 2. Open data_cleaning.ipynb in Jupyter Notebook and run the cells to clean and prepare the data for analysis.
- Save the cleaned files in the data/cleaned folder for database loading.

### 3. Load Data Into SQL Database
Create a SQL database and define the schema for each table.

Import the cleaned datasets into the database using MySQL Workbench.
```
This will create and populate the necessary tables in the inventory_analysis database.

### 4. Analyze Data in Power BI
Open Power BI Desktop.

Connect to the SQL database by selecting Home > Get Data > MYSQL Server.

Load the tables into Power BI and verify relationships in the Model View.

Adjust relationships as needed to ensure accurate data integration.
## 3.Power-BI Dashboard Screenshots

![image](https://github.com/user-attachments/assets/297d7d7d-0ee8-4793-853d-a322f211b3c8)

![image](https://github.com/user-attachments/assets/94e49665-3296-40d7-9578-568221d33571)

![image](https://github.com/user-attachments/assets/d9f93449-e584-46d9-97d6-9e5576e7e8e5)

