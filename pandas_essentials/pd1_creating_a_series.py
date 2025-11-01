import pandas as pd # Import pandas library as pd

# A list of data
data = [1, 2, 3, 4, 5]

# Creating a one-dimensional array-like object Series from the list
# .series() method is used to create a Series the left column represents
# the default index 0 to 4, and the right column contains the values
# from the data list
series = pd.Series(data)

# Print the Series, its type, data type of elements, and size
print(series)
print(type(series))
print(series.dtype)
print(series.size)