import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("final_model.pkl")

st.title("Heart Disease Risk Prediction")

age = st.slider("Age (years)", 0, 100, 50)

bmi = st.slider("Body Mass Index (BMI)", 15.0, 60.0, 25.0)

ap_hi = st.slider("Systolic blood pressure", 70, 250, 120)

ap_lo = st.slider("Diastolic blood pressure", 40, 150, 80)

chol = st.selectbox(
    "Cholesterol Level", ["Normal", "Above normal", "Well above normal"]
)
chol = ["Normal", "Above normal", "Well above normal"].index(chol) + 1

gluc = st.selectbox("Glucose Level", ["Normal", "Above normal", "Well above normal"])
gluc = ["Normal", "Above normal", "Well above normal"].index(gluc) + 1

smoke = st.selectbox("Smoking", ["Regular", "Rarely"])
smoke = 1 if smoke == "Regular" else 0

alco = st.selectbox("Alcohol Intake", ["Regular", "Rarely"])
alco = 1 if alco == "Regular" else 0

active = st.selectbox("Physical Activity", ["Regular", "Rarely"])
active = 1 if active == "Regular" else 0

gender = st.selectbox("Gender", ["Female", "Male"])
gender = 1 if gender == "Female" else 2


if st.button("Predict"):
    X = pd.DataFrame(
        [[age, gender, bmi, ap_hi, ap_lo, chol, gluc, smoke, alco, active]],
        columns=[
            "age_years",
            "gender",
            "bmi",
            "ap_hi",
            "ap_lo",
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
        ],
    )
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][pred]
    if pred == 1:
        st.error(f"High Risk (Probability: {prob*100:.2f}%)")
    else:
        st.success(f"Low Risk (Probability: {prob*100:.2f}%)")
