"""
This program simulates a house price prediction model. It generates a synthetic dataset of house prices based on square footage, number of bedrooms, and age.
The data is split into training and testing sets, and a linear regression model is trained on the training data.
The model is then used to predict house prices on the test set, and the accuracy of the model is evaluated using metrics like RMSE, R-squared, and MAE.
Finally, a scatter plot is generated to visualize the actual vs. predicted house prices.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Generate sample house price dataset
np.random.seed(123)
n = 100  # Number of data points
square_feet = np.random.uniform(800, 3500, n)
bedrooms = np.random.randint(1, 6, n)
age = np.random.randint(1, 51, n)

# Function to generate house price
def generate_price(square_feet, bedrooms, age):
    return square_feet * 100 + bedrooms * 5000 - age * 300 + np.random.normal(0, 15000, len(square_feet))

price = generate_price(square_feet, bedrooms, age)

data = pd.DataFrame({'SquareFeet': square_feet, 'Bedrooms': bedrooms, 'Age': age, 'Price': price})

# Split data into training (70%) and testing (30%)
train_data, test_data, train_price, test_price = train_test_split(
    data[['SquareFeet', 'Bedrooms', 'Age']], data['Price'], test_size=0.3, random_state=123
)

train_data = pd.concat([train_data, train_price], axis=1)
test_data = pd.concat([test_data, test_price], axis=1)

# Train linear regression model
model = LinearRegression()
model.fit(train_data[['SquareFeet', 'Bedrooms', 'Age']], train_data['Price'])

# Display model summary
print("Model Summary:")
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Predict house prices on test set
predicted_price = model.predict(test_data[['SquareFeet', 'Bedrooms', 'Age']])
test_data['PredictedPrice'] = predicted_price

# Calculate model accuracy
rmse = np.sqrt(mean_squared_error(test_data['Price'], test_data['PredictedPrice']))
r2 = r2_score(test_data['Price'], test_data['PredictedPrice'])
mae = mean_absolute_error(test_data['Price'], test_data['PredictedPrice'])

print("\nModel Accuracy Metrics:")
print("RMSE:", rmse)
print("R-squared:", r2)
print("MAE:", mae)

# Scatter plot of actual vs predicted house prices
plt.figure(figsize=(8, 6))
plt.scatter(test_data['Price'], test_data['PredictedPrice'], color='blue', alpha=0.6)
plt.plot([test_data['Price'].min(), test_data['Price'].max()], [test_data['Price'].min(), test_data['Price'].max()], color='red', linestyle='--')
plt.xlabel("Actual Price ($)")
plt.ylabel("Predicted Price ($)")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()