import pandas as pd

# A dictionary with missing data
data = {
    'Name': ['Alice', 'Bob', None , 'Charlie'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Washington']
}

# Creating a two-dimensional tabular data structure called DataFrame from
# the dictionary. Each key in the dictionary becomes a column in the DataFrame
df = pd.DataFrame(data)

print(f'Before cleaning: \n{df}')


"""Drop Rows with Missing Values"""
df_cleaned = df.dropna()

print(f'\nAfter cleaning: \n{df_cleaned}')


"""Fill missing values with a specified value"""

data2 = {
    'Name': ['Rafi', 'Nusrat', None, 'Tania'],
    'Age': [20, None, 22, 25],
    'City': ['Dhaka', 'Chittagong', 'Sylhet', None]
}

df2 = pd.DataFrame(data2)

print(f'\n\nBefore filling missing values: \n{df2}')

df_filled = df2.fillna('Unknown')

print(f'\nAfter filling missing values: \n{df_filled}')

# Using fillna() for different values for columns. Here:
# Missing Name → “Unknown”
# Missing Age → replaced with mean of the Age column
# Missing City → “Dhaka”
df_filled2 = df2.fillna({
    'Name': 'Unknown',
    'Age': df2['Age'].mean(),  # Fill NaN Age with average age
    'City': 'Dhaka'
})

print(f'\nAfter filling with different missing values: \n{df_filled2}')

# Using methods like ffill() and bfill() . These are useful when we have time-series or ordered data.
# Forward fill: fills NaN with the previous row’s value
# Backward fill: fills NaN with the next row’s value
df_forward_filled = df2.ffill()
print('\nAfter forward filled: \n', df_forward_filled)

df_backward_filled = df2.bfill()
print('\nAfter backward filled: \n', df_backward_filled)