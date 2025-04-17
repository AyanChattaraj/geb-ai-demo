"""
This Python program replicates the R code's functionality:
It generates a sample business dataset of employee salaries by department,
then creates a boxplot visualizing the salary distribution for each department,
highlighting outliers in red.  It uses pandas for data handling and matplotlib/seaborn for plotting.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample business dataset (Employee Salary by Department)
np.random.seed(123)
data = pd.DataFrame({
    'Department': np.repeat(['HR', 'IT', 'Finance', 'Marketing', 'Sales'], 20),
    'Salary': np.concatenate([
        np.random.normal(50000, 5000, 20),  # HR salaries
        np.random.normal(80000, 8000, 20),  # IT salaries
        np.random.normal(75000, 7000, 20),  # Finance salaries
        np.random.normal(60000, 6000, 20),  # Marketing salaries
        np.random.normal(55000, 5000, 20)   # Sales salaries
    ])
})

# Create a boxplot using matplotlib and seaborn
plt.figure(figsize=(10, 6))  # Adjust figure size for better readability
sns.boxplot(x='Department', y='Salary', data=data, palette='viridis', fliersize=7,  # Adjust fliersize for outlier size
            flierprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "red"}) # Customize outlier appearance
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary ($)")
plt.figtext(0.5, 0.01, "Outliers are marked in red", ha="center", fontsize=10) # Add caption
sns.despine(left=True, bottom=False) # Remove spines for a cleaner look
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent labels from overlapping
plt.show()