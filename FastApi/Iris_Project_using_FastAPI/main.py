import streamlit as st
import joblib
import numpy as np
import os

# Load the trained model
model = None
model_path = os.path.join(os.path.dirname(__file__), 'ML_Model', 'iris_model.joblib')

try:
    model = joblib.load(model_path)
    st.success(f"Model loaded successfully from {model_path}.")
except FileNotFoundError:
    st.error(f"Model file not found at: {model_path}")
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")

st.title("Iris Species Predictor")

with st.form("iris_form"):
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, format="%.2f")
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, format="%.2f")
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, format="%.2f")
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Predict")

    if submitted:
        if model is None:
            st.error("Model not loaded")
        else:
            data = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(1, -1)
            try:
                prediction = model.predict(data)[0]
                species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
                species = species_mapping.get(prediction, "unknown")
                st.success(f"Predicted Species: {species}")
            except Exception as e:
                st.error(f"Error making prediction: {e}")