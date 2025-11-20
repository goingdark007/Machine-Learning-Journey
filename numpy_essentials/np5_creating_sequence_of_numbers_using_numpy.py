import numpy as np


# # np.arange() is a NumPy function that creates a sequence of
# numbers with a specific start, stop, and step value. Syntax is
# like this np.arange(start, stop, step).
numbers = np.arange(1, 6)
print(f'Sequence of Numbers : {numbers}')

# Using step
numbers2 = np.arange(1,8,2)
print(f'Sequence of Numbers with step : {numbers2}')