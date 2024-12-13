import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load('best_model.joblib')

# Streamlit interface
st.title("ABC Bank Stock Closing Price Prediction")

open_price = st.number_input("Enter Open Price", min_value=0.0, step=0.01)
high_price = st.number_input("Enter High Price", min_value=0.0, step=0.01)
low_price = st.number_input("Enter Low Price", min_value=0.0, step=0.01)
#volume = st.number_input("Enter Volume", min_value=0, step=1)

if st.button('Predict Closing Price'):
    input_data = np.array([[open_price, high_price, low_price]])
    
    # Error handling for prediction
    try:
        predicted_price = model.predict(input_data)[0]
        st.write(f"Predicted Closing Price: ${predicted_price:.2f}")
    except Exception as e:
        st.write(f"Error: {e}")
