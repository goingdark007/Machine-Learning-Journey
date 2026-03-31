"""Data Exploration"""
# Outlier detection and handling
# Using Box Plots for visualization
# And Z-score and IQR (Interquartile Range) for identification and handling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Student_ID' : np.arange(1, 7),
    'Name' : ['John', 'Emily', 'Michael', 'Sophia', 'William', 'Lol'],
    'Age' : [20 ,21, 19, 22, 20, 19],
    'Grade' : [3.8, 3.9, 3.5, 4.0, 3.7, 5.0],
    'Major' : ['Computer Science', 'Biology', 'Mathematics', 'Engineering', 'Psychology', 'Arts']
}

student_df = pd.DataFrame(data)

# Example: Box plot with Matplotlib
plt.boxplot(student_df['Grade'])
plt.title('Box Plot of Grade')
plt.show()

# Example: Detect Outliers using z-score with NumPy
z_scores = (student_df['Grade'] -np.mean(student_df['Grade'])) / np.std(student_df['Grade'])
outliers = student_df[(z_scores > 3) | (z_scores < -3)] # Lower threshold 2 to -2
print(outliers) # Empty data frame because outlier is not extreme


# Example: Detect Outliers using IQR
Q1 = student_df['Grade'].quantile(0.25)
Q3 = student_df['Grade'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = student_df[
    (student_df['Grade'] < lower) |
    (student_df['Grade'] > upper)
]

print(outliers) # Detects even small outliers (better)