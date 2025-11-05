import matplotlib.pyplot as plt
import numpy as np

"""Subplots"""

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
plt.subplot(2, 1, 1)

plt.plot(x, y1, color='blue')
plt.title('Sin(x) Subplot')

plt.subplot(2, 1, 2)
plt.plot(x, y2, color='red')
plt.title('Cos(x) Subplot')

plt.tight_layout()
plt.show()