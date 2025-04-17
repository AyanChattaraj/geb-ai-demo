# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a sample business dataset (Employee Salary by Department)
np.random.seed(123)
data = pd.DataFrame({
    'Department': np.repeat(['HR', 'IT', 'Finance', 'Marketing', 'Sales'], 20),
    'Salary': [
        np.random.normal(50000, 5000, 20),  # HR salaries
        np.random.normal(80000, 8000, 20),  # IT salaries
        np.random.normal(75000, 7000, 20),  # Finance salaries
        np.random.normal(60000, 6000, 20),  # Marketing salaries
        np.random.normal(55000, 5000, 20)   # Sales salaries
    ]
})

# Create a boxplot using matplotlib
plt.figure(figsize=(10, 6))
plt.boxplot([data[data['Department'] == dept]['Salary'] for dept in data['Department'].unique()], labels=data['Department'].unique())
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary ($)')
plt.show()