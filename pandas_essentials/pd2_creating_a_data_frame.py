import pandas as pd # imports pandas library as pd


# A dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}


# Creating a two-dimensional tabular data structure called DataFrame from
# the dictionary. Each key in the dictionary becomes a column in the DataFrame
df = pd.DataFrame(data)


# Print the DataFrame, its type, data types of each column, and shape
print(f'DataFrame :-\n{df}')
print(f'\nDataFrame type :-\n{type(df)}')
print(f'\nData types of each column of the DataFrame :-\n{df.dtypes}')
# df.shape method returns a tuple (rows, columns) — e.g. (3, 3) at this point
print(f'\nShape of the DataFrame :-\n{df.shape}')


# Accessing specific columns
print(f'\nAccessing a specific column :-\n{df['Name']}')  # Accessing the 'Name' column
# Accessing multiple columns
print(f'\nAccessing multiple columns :-\n{df[['Name', 'Age']]}')
# Accessing specific rows using .loc and .iloc
# Accessing the first row by label
print(f'\nAccessing a specific row by label :-\n{df.loc[0]}')
# Accessing the second row by integer position
print(f'\nAccessing a specific row by integer position :-\n{df.iloc[1]}')


# Adding a new column
df['Salary'] = [70000, 80000, 90000]
print(f'\nAdded a new column Salary :-\n{df}')


# Filtering rows based on a condition
# Rows where Age is greater than 28
print(f'\nFiltered rows based on a condition :-\n{df[df['Age'] > 28]}')


# Summary statistics
print(f'\nSummary Statistics :-\n{df.describe()}')


# Sorting the DataFrame by Age
print(f'\nSorting the DataFrame by Age :-\n{df.sort_values(by='Age')}')