import pandas as pd


# A dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}


# Creating a two-dimensional tabular data structure called DataFrame from
# the dictionary. Each key in the dictionary becomes a column in the DataFrame
df = pd.DataFrame(data)


""" Indexing and slicing"""
# Select a single column by label
print(f'Selecting a single column by label :-\n{df['Name']}\n')


# .iloc[:, 0] method selects a single column by position
print(f'Selecting a single column by position :-\n{df.iloc[:, 0]}\n')


# .loc[1:3, ['Name', 'Age']] method selects rows and columns by label
print(f'Selecting rows and columns by label :-\n{df.loc[1:3, ['Name', 'Age']]}\n')


# .iloc[1:3, 0:2] method selects rows and columns by position
print(f'Selecting rows and columns by position :-\n{df.iloc[1:3, 0:2]}\n')