import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression




st.set_page_config(page_title="Diabetes Predictor", page_icon="🩸")

st.title(" Diabetes Prediction App")
st.write("""
This app predicts whether a person has **Diabetes** based on medical inputs  
using **Logistic Regression**.
""")

# 1. Sidebar Input
st.sidebar.header("User Input Parameters")

def user_input():
    glucose = st.sidebar.slider("Glucose Level", 0, 200, 120)
    bp = st.sidebar.slider("Blood Pressure", 0, 130, 70)
    skin_thickness = st.sidebar.slider("Skin Thickness", 0, 100, 20)
    insulin = st.sidebar.slider("Insulin", 0, 900, 79)
    bmi = st.sidebar.slider("BMI", 0.0, 70.0, 32.0)
    dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.sidebar.slider("Age", 10, 100, 33)

    data = {
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }
    return pd.DataFrame(data, index=[0])

df_user = user_input()
st.subheader("User Input Parameters")
st.write(df_user)


try:
    diabetes_url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
    diabetes = pd.read_csv(diabetes_url)

    
    X = diabetes.drop(["Outcome", "Pregnancies"], axis=1)
    y = diabetes["Outcome"]

    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    
    model = LogisticRegression()
    model.fit(X_scaled, y)

    
    df_scaled = scaler.transform(df_user)
    
    prediction = model.predict(df_scaled)
    prediction_proba = model.predict_proba(df_scaled)

    st.subheader("Prediction")
    if prediction[0] == 1:
        st.error(" Diabetes Detected")
    else:
        st.success(" No Diabetes Detected")

    st.subheader("Prediction Probability")
    st.write(f"Probability of Diabetes: {prediction_proba[0][1]*100:.2f}%")

except Exception as e:
    st.error(f"Error loading data or training model. Please check internet connection. Error: {e}")