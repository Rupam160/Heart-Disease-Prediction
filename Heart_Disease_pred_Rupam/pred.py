import streamlit as st
import joblib
import numpy as np
import webbrowser
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://lottie.host/a72ac1db-b1ff-463f-99be-02f7d9dd3bee/kWA6UtjRJ1.json")
lottie_coding1=load_lottieurl("https://lottie.host/b98b367e-b9bd-4178-9626-b72a9335e820/uwdMVdCEeT.json")
lottie_coding2=load_lottieurl("https://lottie.host/b0223cb1-356a-4792-848a-de80ba4b0236/fJDVFMXIxH.json")


# Load the pre-trained heart disease prediction model
model = joblib.load("heart_disease_model.joblib")

# Create a Streamlit web app
st.title("Heart Disease Prediction")
st_lottie(lottie_coding)

# Create columns to accept user input for different features
age = st.number_input("Age", min_value=1, max_value=150, value=25)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
resting_bp = st.number_input("Resting Blood Pressure", min_value=50, max_value=300, value=120)
cholesterol = st.number_input("Serum Cholestoral (mg/dl)", min_value=50, max_value=500, value=200)
fasting_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
rest_ecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
max_heart_rate = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=0.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
num_vessels = st.selectbox("Number of Major Vessels Colored by Flourosopy", [0, 1, 2, 3])
thal = st.selectbox("Thal", [0, 1, 2])

# Convert user input to numerical values and create a feature array
sex = 1 if sex == "Male" else 0
fasting_sugar = 1 if fasting_sugar == "Yes" else 0
exercise_angina = 1 if exercise_angina == "Yes" else 0

feature_array = np.array([age, sex, cp, resting_bp, cholesterol, fasting_sugar,
                          rest_ecg, max_heart_rate, exercise_angina, oldpeak,
                          slope, num_vessels, thal]).reshape(1, -1)

# Create a button to make the prediction
if st.button("Predict"):
    prediction = model.predict(feature_array)[0]
    if prediction == 0:
        result = "No heart disease"
        st_lottie(lottie_coding1)
    else:
        result = "Heart disease"
        st_lottie(lottie_coding2)
    
    st.write(f"The prediction is: {result}")

