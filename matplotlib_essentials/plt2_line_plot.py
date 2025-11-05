import matplotlib.pyplot as plt
import  numpy as np

"""Line Plot"""
# A line plot connects individual data points with a continuous
# line. It’s mainly used to show trends over time or continuous
# relationships between variables

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
plt.plot(x, y, color= 'blue', linestyle='--', marker='o', label='Sin(x)')

# adding text labels for each axis
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# adds the title 'Line Plot' at the top of the graph
plt.title('Line Plot')

# displays the label 'Sin(x)' (from label='Sin(x)') in a small
# box on the plot. This helps identify different lines when multiple
# is plotted.
plt.legend()

# adds background grid lines for better readability.
plt.grid(True)

# Shows the plot window
plt.show()