import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Define a sample DataFrame for student data"""

data = {
    'Student_ID' : np.arange(1, 6),
    'Name' : ['John', 'Emily', 'Michael', 'Sophia', 'William'],
    'Age' : [20 ,21, 19, 22, 20],
    'Grade' : ['3.8', '3.9', '3.5', '4.0', '3.7'],
    'Major' : ['Computer Science', 'Biology', 'Mathematics', 'Engineering', 'Psychology']
}

student_df = pd.DataFrame(data)
print(f'DataFrame :\n{student_df}')

"""Descriptive Statistics"""

summary_stats = student_df.describe()
print(f'\nDescriptive Statistics :\n{summary_stats}')

""""Data Distribution"""

# Example: Histogram with Matplotlib
plt.hist(student_df['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()