import streamlit as st

st.set_page_config(
    page_title="Health AI",
    page_icon="🏥",
)

st.title(" Medical Prediction Dashboard")

st.write("""
Welcome to the Health AI System. This application uses Machine Learning to help predict potential health risks.

### Available Modules:
Please select a module from the **sidebar** on the left:

1. ** Diabetes Prediction**: Uses Logistic Regression to analyze blood/insulin levels.
2. ** COVID-19 Probability**: Uses Decision Trees to analyze symptoms.
""")

st.sidebar.info("Select a page above to start.")