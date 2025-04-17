# Load necessary library
library(dplyr)

cat("Creating sample dataframe:\n")
data <- data.frame(
  ID = 1:10,
  Name = c("Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Ivy", "Jack"),
  Age = c(23, 35, 29, 40, 22, 31, 37, 24, 27, 45),
  Salary = c(50000, 60000, 55000, 70000, 48000, 62000, 68000, 53000, 57000, 75000),
  Department = c("HR", "IT", "Finance", "IT", "HR", "Marketing", "Finance", "IT", "HR", "Marketing")
)

cat("View first few rows:\n")
print(head(data))
cat("--------------\n\n")

cat("Selecting specific columns:\n")
selected_data <- data %>% select(Name, Age, Salary)
print(selected_data)
cat("--------------\n\n")

cat("Filtering rows where Age is greater than 30:\n")
filtered_data <- data %>% filter(Age > 30)
print(filtered_data)
cat("--------------\n\n")

cat("Sorting data by Salary in descending order:\n")
sorted_data <- data %>% arrange(desc(Salary))
print(sorted_data)
cat("--------------\n\n")

cat("Adding a new column (Bonus - 10% of Salary):\n")
mutated_data <- data %>% mutate(Bonus = Salary * 0.1)
print(mutated_data)
cat("--------------\n\n")

cat("Grouping by Department and summarizing average salary:\n")
grouped_data <- data %>% group_by(Department) %>% summarize(Avg_Salary = mean(Salary))
print(grouped_data)
cat("--------------\n\n")

cat("Counting number of employees in each department:\n")
count_data <- data %>% count(Department)
print(count_data)
cat("--------------\n\n")

cat("Renaming columns:\n")
renamed_data <- data %>% rename(Employee_Name = Name, Employee_Salary = Salary)
print(renamed_data)
cat("--------------\n\n")

cat("Replacing NA values in Age with mean Age:\n")
data$Age <- ifelse(is.na(data$Age), mean(data$Age, na.rm = TRUE), data$Age)
print(data)
cat("--------------\n\n")
