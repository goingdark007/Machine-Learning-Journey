import pandas as pd


# Loading data into DataFrame
# pd.read_csv() method loads data from CSV file
df1 =pd.read_csv('data.csv')


# pd.read_excel() method loads data from Excel file
df = pd.read_excel('data.xlsx')


# pd.read_json() method loads data from JSON file
df3 = pd.read_json('data.json')