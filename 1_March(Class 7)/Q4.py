# Customer Churn Prediction for a Subscription Service
#  Concepts Used:
# • Cost Function (MSE)
# • Bias-Variance Tradeoff
# • Regression Coefficients
#  Project Overview:
# • Predict whether a customer will continue their subscription or churn based on 
# factors like engagement, billing issues, and customer support interactions.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import streamlit as st

# Load dataset
df = pd.read_csv(r'C:\Users\javer\Downloads\IT_TRAINING_CLASSES\class7\customer_churn_data.csv') 

# Preprocess data
df.dropna(inplace=True)  # Remove missing values

# Convert 'churn' column to integers
df['churn'] = df['churn'].astype(str).str.strip().map({'False': 0, 'True': 1})

# Convert categorical columns to numerical
df = pd.get_dummies(df, columns=['international_plan', 'voice_mail_plan'], drop_first=True)

# Drop unnecessary columns
df.drop(columns=['Id', 'state', 'phone_number'], errors='ignore', inplace=True)

# Define features and target variable
X = df.drop(columns=['churn'])
y = df['churn']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}\n')
print(report)

# Streamlit app for visualization
st.title('Customer Churn Prediction')
st.write(f'Accuracy: {accuracy:.2f}')

# Confusion Matrix Visualization
fig, ax = plt.subplots()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d',
            cmap='Blues', xticklabels=['No Churn', 'Churn'], yticklabels=['No Churn', 'Churn'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
st.pyplot(fig)

# User input for prediction
st.sidebar.header('Predict Customer Churn')

features = {col: st.sidebar.number_input(f'Enter {col}:', float(X[col].min()), float(X[col].max())) for col in X.columns}

if st.sidebar.button('Predict'):
    input_data = np.array([features[col] for col in X.columns]).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    st.sidebar.write(f'Predicted Churn: {"Yes" if prediction == 1 else "No"}')

# [Your Task]
# 1. Install the dependencies
# 2. Collect customer interaction and subscription data.
# 3. Define independent (features like usage, complaints) and dependent 
# variables (churn or not).
# 4. Apply linear regression and analyze coefficients.
# 5. Optimize model using Gradient Descent.
# 6. Create an alert system for potential churners.
# 7. Compile and run the code
# 8. Print and show the output