# Load necessary libraries
library(ggplot2)

# Create a sample business dataset (Employee Salary by Department)
set.seed(123)
data <- data.frame(
  Department = rep(c("HR", "IT", "Finance", "Marketing", "Sales"), each = 20),
  Salary = c(
    rnorm(20, mean = 50000, sd = 5000),  # HR salaries
    rnorm(20, mean = 80000, sd = 8000),  # IT salaries
    rnorm(20, mean = 75000, sd = 7000),  # Finance salaries
    rnorm(20, mean = 60000, sd = 6000),  # Marketing salaries
    rnorm(20, mean = 55000, sd = 5000)   # Sales salaries
  )
)

# Create a boxplot using ggplot2
ggplot(data, aes(x = Department, y = Salary, fill = Department)) +
  geom_boxplot(outlier.color = "red", outlier.shape = 16, outlier.size = 3) + 
  labs(title = "Salary Distribution by Department",
       x = "Department",
       y = "Salary ($)",
       caption = "Outliers are marked in red") +
  theme_minimal()
