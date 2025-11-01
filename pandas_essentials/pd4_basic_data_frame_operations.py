import pandas as pd # importing pandas as pd


# A dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}


# Creating a two-dimensional tabular data structure called DataFrame from
# the dictionary. Each key in the dictionary becomes a column in the DataFrame
df = pd.DataFrame(data)


# Basic DataFrame operations
# df.head() method shows first few (5) rows
print(f'\nFirs few rows :-\n{df.head()}')


# df.tail() method shows last few (5) rows
print(f'\nLast few rows :-\n{df.tail()}')


# df.info() method gets information about the data frame
print(f'\nInformation of the DataFrame :-\n')
print(df.info())


# df.describe() method generates descriptive statistics
print(f'\nGenerating descriptive statistics :-\n{df.describe()}')