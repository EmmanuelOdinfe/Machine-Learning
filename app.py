import streamlit as st
import pickle
import pandas as pd

with open("regressor.pkl", "rb") as file:
    model = pickle.load(file)
    
st.title("Machine Learning Predicction App")
st.write("Enter the details below to make a prediction.")

# Input fields
experience = st.number_input("Years Of Experience",min_value=0, max_value=50, value=2)

# Prediction button
if st.button("Predict Salary"):
    input_data= pd.DataFrame({
        "YearsExperience":[experience]
    })

    predicted_salary = model.predict(input_data)[0]
    st.success(f"Predicted Salary : N{predicted_salary:,.2f}")

