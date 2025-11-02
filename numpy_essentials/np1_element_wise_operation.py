import numpy as np

"""Computing Element-wise operations"""
# Element-wise operations mean performing a mathematical operation
# on each element of an array individually, instead of looping through
# it manually. Each operation is applied to every corresponding element in
# both arrays automatically, without using any for loop.

# Create two arrays or lists
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

# Element-wise addition
result = a + b
print(result)