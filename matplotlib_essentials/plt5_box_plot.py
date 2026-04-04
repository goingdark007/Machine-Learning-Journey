"""Box Plot for Outlier Detection"""
# Outlier detection and handling
# Using Box Plots for visualization

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
plt.boxplot(student_df['Grade']) # 5.0 is the Outlier
plt.title('Box Plot of Grade')
plt.show()