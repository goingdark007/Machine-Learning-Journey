"""Histogram"""
import matplotlib.pyplot as plt
import numpy as np

# A histogram shows HOW OFTEN each value occurs. It visualizes frequency using bars

# Generate random data using numpy
data = np.random.normal(loc=50, scale=10, size=1000)

plt.hist(
    data,
    bins=20,
    color='skyblue',
    edgecolor='black',
    alpha=0.7
)

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")

plt.show()
