import pandas as pd

"""
This program replicates the R code's functionality using Python and the pandas library.
It creates a DataFrame, performs various data manipulations such as selecting columns,
filtering rows, sorting, adding new columns, grouping and summarizing data, counting
values, renaming columns, and handling NA values.
"""

# Creating sample dataframe
print("Creating sample dataframe:\n")
data = pd.DataFrame({
    'ID': range(1, 11),
    'Name': ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ivy", "Jack"],
    'Age': [23, 35, 29, 40, 22, 31, 37, 24, 27, 45],
    'Salary': [50000, 60000, 55000, 70000, 48000, 62000, 68000, 53000, 57000, 75000],
    'Department': ["HR", "IT", "Finance", "IT", "HR", "Marketing", "Finance", "IT", "HR", "Marketing"]
})

print("View first few rows:\n")
print(data.head())
print("--------------\n\n")

# Selecting specific columns
print("Selecting specific columns:\n")
selected_data = data[['Name', 'Age', 'Salary']]
print(selected_data)
print("--------------\n\n")

# Filtering rows where Age is greater than 30
print("Filtering rows where Age is greater than 30:\n")
filtered_data = data[data['Age'] > 30]
print(filtered_data)
print("--------------\n\n")

# Sorting data by Salary in descending order
print("Sorting data by Salary in descending order:\n")
sorted_data = data.sort_values(by='Salary', ascending=False)
print(sorted_data)
print("--------------\n\n")

# Adding a new column (Bonus - 10% of Salary)
print("Adding a new column (Bonus - 10% of Salary):\n")
mutated_data = data.copy()  # Create a copy to avoid modifying the original DataFrame
mutated_data['Bonus'] = mutated_data['Salary'] * 0.1
print(mutated_data)
print("--------------\n\n")

# Grouping by Department and summarizing average salary
print("Grouping by Department and summarizing average salary:\n")
grouped_data = data.groupby('Department')['Salary'].mean().reset_index()
grouped_data.rename(columns={'Salary': 'Avg_Salary'}, inplace=True)
print(grouped_data)
print("--------------\n\n")

# Counting number of employees in each department
print("Counting number of employees in each department:\n")
count_data = data['Department'].value_counts().reset_index()
count_data.columns = ['Department', 'n']
print(count_data)
print("--------------\n\n")

# Renaming columns
print("Renaming columns:\n")
renamed_data = data.rename(columns={'Name': 'Employee_Name', 'Salary': 'Employee_Salary'})
print(renamed_data)
print("--------------\n\n")

# Replacing NA values in Age with mean Age
print("Replacing NA values in Age with mean Age:\n")
data['Age'] = data['Age'].fillna(data['Age'].mean())
print(data)
print("--------------\n\n")