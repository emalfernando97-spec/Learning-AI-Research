import numpy as np
from sklearn.linear_model import LinearRegression

# Clinical Data: [Hours of Research, Focus Level (1-10)]
X = np.array([[2, 5], [4, 7], [6, 8], [8, 9], [10, 10]])

# Target: Contribution Output (0-100)
y = np.array([20, 45, 65, 85, 98])

# Initialize the Estimator (Linear Regression Model)
model = LinearRegression()

# Train the model (Clinical fitment)
model.fit(X, y)

# Prediction: Predict output for 7 hours research at 8.5 focus
test_data = np.array([[7, 8.5]])
prediction = model.predict(test_data)

print(f"Predicted Contribution for 7hrs Research: {prediction[0]:.2f}")
