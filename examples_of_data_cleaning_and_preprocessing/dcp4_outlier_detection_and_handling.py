"""Data Exploration"""
# Outlier detection and handling
# Using Box Plots for visualization
# And Z-score and IQR (Interquartile Range) for identification and handling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student_ID' : np.arange(1, 6),
    'Name' : ['John', 'Emily', 'Michael', 'Sophia', 'William'],
    'Age' : [20 ,21, 19, 22, 20],
    'Grade' : [3.8, 3.9, 3.5, 4.0, 3.7],
    'Major' : ['Computer Science', 'Biology', 'Mathematics', 'Engineering', 'Psychology']
}

student_df = pd.DataFrame(data)

# Example: Box plot with Matplotlib
plt.boxplot(student_df['Grade'])
plt.title('Box Plot of Grade')
plt.show()

# Example: Detect Outliers using z-score with NumPy
z_scores = (student_df['Grade'] -np.mean(student_df['Grade'])) / np.std(student_df['Grade'])
outliers = student_df[(z_scores > 3) | (z_scores < -3)]
print(outliers)