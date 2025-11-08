import numpy as np

"""Example Min-Max scaling with numpy"""
# It's a way to rescale our data so that all values fit in a fixed range usually between 0 and 1

# Create a sample
data = np.array([[1, 2],
                [3, 4],
                [5 ,6]])

min_val = np.min(data, axis=0)
max_val = np.max(data, axis=0)

scaled_data = (data - min_val) / (max_val - min_val)
print(scaled_data)