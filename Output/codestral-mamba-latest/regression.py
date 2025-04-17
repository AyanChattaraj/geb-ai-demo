# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample house price dataset
np.random.seed(123)
data = pd.DataFrame({
    'SquareFeet': np.random.uniform(800, 3500, 100),  # Random house sizes
    'Bedrooms': np.random.randint(1, 6, 100),  # Random bedroom counts
    'Age': np.random.randint(1, 51, 100)  # Random house ages
})

# Apply price formula
data['Price'] = data['SquareFeet'] * 100 + data['Bedrooms'] * 5000 - data['Age'] * 300 + np.random.normal(0, 15000, 100)

# Split data into training (70%) and testing (30%)
train_data, test_data = train_test_split(data, train_size=0.7, random_state=123)

# Train linear regression model
model = LinearRegression()
model.fit(train_data[['SquareFeet', 'Bedrooms', 'Age']], train_data['Price'])

# Display model summary
print("Model Summary:")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Predict house prices on test set
test_data['PredictedPrice'] = model.predict(test_data[['SquareFeet', 'Bedrooms', 'Age']])

# Calculate model accuracy
mse = mean_squared_error(test_data['Price'], test_data['PredictedPrice'])
r2 = r2_score(test_data['Price'], test_data['PredictedPrice'])
print("\nModel Accuracy Metrics:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Scatter plot of actual vs predicted house prices
plt.scatter(test_data['Price'], test_data['PredictedPrice'], color='blue', alpha=0.6)
plt.plot(test_data['Price'], test_data['Price'], color='red', linestyle='dashed')
plt.xlabel('Actual Price ($)')
plt.ylabel('Predicted Price ($)')
plt.title('Actual vs Predicted House Prices')
plt.show()