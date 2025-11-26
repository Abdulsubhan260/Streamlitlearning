import streamlit as st

st.title("Welcome to Language Picker")
# st.title() is used for main title 
st.subheader("this language picker is made by Streamlit")
# st.subhearder() Shows a smaller title under the main title
st.write("which language you like most.please pick one:")
# st.write() displays normal text in the app


st.selectbox("slect language: ",["Python","java script","css","HTML","C++"])
# Creates a dropdown menu,user can choose one option from list,default value is select language
# user can choose any value from list


st.success("conrats!you select language successfully")
# Shows a success message in green  box 
st.balloons()
# shows some baloons to congrats the user





import streamlit as st
## Widgets of stream-lit
st.title("Widgets of Streamlit")
st.subheader("this project shows widgets of streamlit")
name=st.text_input("what is your name: ?")
if name:
    st.success(f"your name is {name}")
# st.text_input() function is used to let the user type text,user can write its name,messages etc

language=st.selectbox("choose your language:",["python","java script","css","html","c++","c#"])
# st.selectbox() is used to make a drop down menue user can choose from that menu

rating=st.slider("rate your skills in choosen language.minimum criteria is 3",0,10,3)

# st.slider is used to create a slide bar(volume button like shape)and in this case default value is 3


agree=st.checkbox("i agree to all terms and conditions")
# st.checkbox this will make a box and user have to check it before preceding further
# st.button()is use to creates a simple button(submit in this case).when user clicks on it,it will run.
if st.button("Submit"):
    if agree:
        st.success(f"Hello {name}! You selected {language} and rated yourself {rating}/10.")
        st.balloons()
    else:
        st.warning("Please agree to the terms to continue.")




# ###  *****practice of widgets******

import streamlit as st


st.title("Loan Eligibility Checker")


st.header("Applicant Details")


name = st.text_input("Enter your name")
age = st.slider("Age", 18, 65, 25)  # min value, max value, default value
gender = st.radio("Gender", ["Male", "Female"])
married = st.selectbox("Marital Status", ["Single", "Married"])
dependents = st.number_input("Number of Dependents", 0, 5, 0)
income = st.number_input("Monthly Income : ", 500, 20000, 3000)
loan_amount = st.number_input("Loan Amount : ", 1000, 50000, 5000)
credit_score = st.slider("Credit Score", 300, 900, 650)


if st.button("Check Eligibility"):
    
    if age < 18:
        st.warning("You must be at least 18 years old.")
    elif income < 2000:
        st.error("Income too low for loan eligibility.")
    elif credit_score < 600:
        st.error("Credit score too low for loan approval.")
     
    else:
        st.success(f"Congratulations {name}! You are eligible for the loan ")


