import streamlit as st
import joblib
import numpy as np
import xgboost as xgb

# Load model
model = joblib.load('C:\\Users\\HP\\Drone_jamming_Detection.pkl')

# Define feature names
feature_names = [
    "Subcarrier Spacing",
    "CP length",
    "Average Received Power (mW)",
    "SNR",
    "Average Signal Power",
    "Average Noise Power"
]

# Function for prediction
def predict(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

# Streamlit UI
st.title("XGBoost Classifier Deployment")

# User inputs
input_data = []
for feature in feature_names:
    input_data.append(st.number_input(f"{feature}", value=0.0))

if st.button("Predict"):
    result = predict(input_data)
    st.write(f"Predicted Class: {result}")
