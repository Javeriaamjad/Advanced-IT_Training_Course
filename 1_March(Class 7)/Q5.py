
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

# Load dataset
file_path =  r"C:\Users\javer\Downloads\IT_TRAINING_CLASSES\class7\owid-energy-data.csv"
df = pd.read_csv(file_path)

# Display column names to identify the correct column for energy consumption
st.write("Dataset Columns:", df.columns.tolist())

# Identify the correct column for energy consumption
energy_columns = [col for col in df.columns if "consumption" in col.lower()]
if not energy_columns:
    raise KeyError("No column related to energy consumption found in the dataset.")

# Use the first identified energy consumption column
energy_column = energy_columns[0]
st.write(f"Using '{energy_column}' as the target variable.")

# Drop missing values
df.dropna(inplace=True)

# One-hot encode categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
if categorical_cols:
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Define features and target variable
X = df.drop(columns=[energy_column])
y = df[energy_column]

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Implement Gradient Descent for Linear Regression
def gradient_descent(X, y, lr=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    bias = 0
    history = []
    
    for epoch in range(epochs):
        y_pred = np.dot(X, theta) + bias
        error = y_pred - y
        
        # Compute gradients
        d_theta = (1/m) * np.dot(X.T, error)
        d_bias = (1/m) * np.sum(error)
        
        # Update parameters
        theta -= lr * d_theta
        bias -= lr * d_bias
        
        mse = mean_squared_error(y, y_pred)
        history.append(mse)
        
    return theta, bias, history

# Train model using Gradient Descent
theta, bias, loss_history = gradient_descent(X_train, y_train, lr=0.01, epochs=1000)

def predict(X, theta, bias):
    return np.dot(X, theta) + bias

# Predictions
y_pred = predict(X_test, theta, bias)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Streamlit app
st.title('Energy Consumption Prediction')
st.write(f'MSE: {mse:.2f}, R-squared: {r2:.2f}')

# Visualization
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, alpha=0.5, color='blue')
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r', lw=2)
ax.set_xlabel('Actual Energy Consumption')
ax.set_ylabel('Predicted Energy Consumption')
st.pyplot(fig)

# Loss Plot
fig_loss, ax_loss = plt.subplots()
ax_loss.plot(loss_history)
ax_loss.set_title("Loss Over Iterations")
ax_loss.set_xlabel("Iterations")
ax_loss.set_ylabel("MSE")
st.pyplot(fig_loss)

# User input for prediction
st.sidebar.header('Predict Energy Consumption')
features = {col: st.sidebar.number_input(f'Enter {col}:', float(df[col].min()), float(df[col].max())) for col in X.columns}

if st.sidebar.button('Predict'):
    input_data = np.array([features[col] for col in X.columns]).reshape(1, -1)
    input_scaled = scaler.transform(input_data)
    prediction = predict(input_scaled, theta, bias)[0]
    st.sidebar.write(f'Predicted Energy Consumption: {prediction:.2f} kWh')

# [Your Task]
# 1. Install the dependencies
# 2. Collect energy usage dataset from Open Energy Data sources.
# 3. Perform exploratory data analysis (EDA) to understand trends.
# 4. Train a linear regression model with temperature and time-based 
# features.
# 5. Optimize the model with Gradient Descent.
# 6. Deploy a simple dashboard to display energy usage trends.
# 7. Compile and run the code
# 8. Print and show the output