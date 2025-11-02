import numpy as np

"""Broadcasting"""
# when arrays have different shapes, NumPy "stretches" one to
# match the other if possible. So, operations can happen element by element.

# Create an array and scalar
a = np.array([1,2,3,4])
scalar = 10

# Scalar multiplication
result = a * scalar
print(result)