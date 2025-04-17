# Import necessary library
import pandas as pd

# Create sample dataframe
print("Creating sample dataframe:")
data = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [23, 35, 29, 40, 22, 31, 37, 24, 27, 45],
    'Salary': [50000, 60000, 55000, 70000, 48000, 62000, 68000, 53000, 57000, 75000],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Marketing', 'Finance', 'IT', 'HR', 'Marketing']
})

print(data.head())
print("--------------")

# Select specific columns
print("Selecting specific columns:")
selected_data = data[['Name', 'Age', 'Salary']]
print(selected_data)
print("--------------")

# Filter rows where Age is greater than 30
print("Filtering rows where Age is greater than 30:")
filtered_data = data[data['Age'] > 30]
print(filtered_data)
print("--------------")

# Sort data by Salary in descending order
print("Sorting data by Salary in descending order:")
sorted_data = data.sort_values(by='Salary', ascending=False)
print(sorted_data)
print("--------------")

# Add a new column (Bonus - 10% of Salary)
print("Adding a new column (Bonus - 10% of Salary):")
data['Bonus'] = data['Salary'] * 0.1
print(data)
print("--------------")

# Group by Department and summarize average salary
print("Grouping by Department and summarizing average salary:")
grouped_data = data.groupby('Department')['Salary'].mean().reset_index()
print(grouped_data)
print("--------------")

# Count number of employees in each department
print("Counting number of employees in each department:")
count_data = data['Department'].value_counts().reset_index()
count_data.columns = ['Department', 'count']
print(count_data)
print("--------------")

# Rename columns
print("Renaming columns:")
renamed_data = data.rename(columns={'Name': 'Employee_Name', 'Salary': 'Employee_Salary'})
print(renamed_data)
print("--------------")

# Replace NA values in Age with mean Age
print("Replacing NA values in Age with mean Age:")
data['Age'].fillna(data['Age'].mean(), inplace=True)
print(data)
print("--------------")