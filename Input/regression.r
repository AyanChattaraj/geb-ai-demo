# Load necessary libraries
library(ggplot2)
library(caret)

# Generate sample house price dataset
set.seed(123)
data <- data.frame(
  SquareFeet = runif(100, min = 800, max = 3500),  # Random house sizes
  Bedrooms = sample(1:5, 100, replace = TRUE),     # Random bedroom counts
  Age = sample(1:50, 100, replace = TRUE),         # Random house ages
  Price = function(x) {                            # Generate house price
    x$SquareFeet * 100 + x$Bedrooms * 5000 - x$Age * 300 + rnorm(100, mean = 0, sd = 15000)
  }
)

data$Price <- data$Price(data)  # Apply price formula

# Split data into training (70%) and testing (30%)
set.seed(123)
trainIndex <- createDataPartition(data$Price, p = 0.7, list = FALSE)
trainData <- data[trainIndex, ]
testData <- data[-trainIndex, ]

# Train linear regression model
model <- lm(Price ~ SquareFeet + Bedrooms + Age, data = trainData)

# Display model summary
cat("Model Summary:\n")
summary(model)

# Predict house prices on test set
testData$PredictedPrice <- predict(model, newdata = testData)

# Calculate model accuracy
accuracy <- postResample(testData$PredictedPrice, testData$Price)
cat("\nModel Accuracy Metrics:\n")
print(accuracy)

# Scatter plot of actual vs predicted house prices
ggplot(testData, aes(x = Price, y = PredictedPrice)) +
  geom_point(color = "blue", alpha = 0.6) +
  geom_abline(slope = 1, intercept = 0, color = "red", linetype = "dashed") +
  labs(title = "Actual vs Predicted House Prices",
       x = "Actual Price ($)",
       y = "Predicted Price ($)") +
  theme_minimal()
