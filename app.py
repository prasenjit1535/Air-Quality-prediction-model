import streamlit as st
import numpy as np
import joblib

# Load your trained model
model = joblib.load(r"air_quality_model.pkl")  # Make sure this file exists

st.title("🌫️ Air Quality Index Prediction App")
st.markdown("Enter pollution values to predict AQI")

# Input features
pm25 = st.number_input("PM2.5", min_value=0.0)
pm10 = st.number_input("PM10", min_value=0.0)
no = st.number_input("NO", min_value=0.0)
co = st.number_input("CO", min_value=0.0)
so2 = st.number_input("SO2", min_value=0.0)

# Format input for model
input_data = np.array([[pm25, pm10, no, co, so2]])

# Predict and display result
if st.button("Predict AQI"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted AQI: {prediction:.2f}")
