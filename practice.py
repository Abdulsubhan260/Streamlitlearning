# Mutlt-feature App:
import streamlit as st
import requests

st.title("Multi-Purpose-App")

st.subheader("by using streamlit")

if "page" not in st.session_state:
    st.session_state.page = None


side=st.sidebar.write("Our Services")
if st.sidebar.button("Currency Converter"):
    st.session_state.page = "converter"

if st.sidebar.button("Dog Pic Generator"):
    st.session_state.page="dog"
    

if st.sidebar.button("Joke Generator"):
    st.session_state.page="joke"


if st.sidebar.button("fact"):
    st.session_state.page="fact"


if st.session_state.page == "converter":
    st.title("Currency Converter")

    st.subheader("using streamlit")

    amount=st.number_input("Enter your amount in pkr",min_value=1)

    target_currency=st.selectbox("Convert to: ",["USD","GBP","AED","SAR","EUR"])


    if st.button("Convert"):
        url="https://v6.exchangerate-api.com/v6/5e9e7c8751ffe9f608424a35/latest/PKR"


        response=requests.get(url)

        if response.status_code==200:
            data=response.json()

            rate=data["conversion_rates"][target_currency]

            converted=rate*amount

            st.success(f"{amount} PKR is equal to {converted:.2f} {target_currency}")

        else:
            st.error("Sorry! Fail to Convert")

#  dog image generator
if st.session_state.page=="dog":
    st.title(" Random Dog Image Generator")

    st.subheader("Click the button to see a random dog image!")

    if st.button("Show me a Dog"):



        url = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(url)



        if response.status_code == 200:
            data = response.json()
            image_url = data["message"]
            st.image(image_url, use_column_width=True)


        else:
            st.error("Failed to fetch a dog image. Try again!")


# joke geberator
if st.session_state.page=="joke":
    st.title(" Random Joke Generator")
    st.subheader("Click the button to get a new joke!")

    if st.button("Get a Joke"):



        url = "https://official-joke-api.appspot.com/random_joke"


        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            setup = data["setup"]
            punchline = data["punchline"]

            st.write(f"**{setup}**")
            st.write(f"*{punchline}*")



        else:
            st.error("Failed to fetch a joke. Try again!")


# fact generator

if st.session_state.page=="fact":
    st.title("Random Fact Generator")

    if st.button("Get Fact"):


            url = "https://uselessfacts.jsph.pl/random.json?language=en"


            response = requests.get(url)
            if response.status_code == 200:
                fact = response.json()["text"]


                st.success(fact)
            else:
                st.error("Failed to fetch a fact")






# Simple Dash Board App

import streamlit as st
import pandas as pd
import numpy as np


st.title("Simple Sales Dashboard")
st.write("""
This is a simple interactive dashboard built with Streamlit
You can filter data, view tables, and see charts dynamically
""")


data = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 150, 200, 130, 170],
    'Profit': [20, 40, 50, 30, 45],
    'Region': ['North', 'South', 'East', 'West', 'North']
})


st.sidebar.header("Filter Options")


selected_product = st.sidebar.selectbox("Select Product", data['Product'].unique())


selected_region = st.sidebar.multiselect("Select Region", data['Region'].unique(), default=data['Region'].unique())


filtered_data = data[(data['Product'] == selected_product) & (data['Region'].isin(selected_region))]




st.subheader("Filtered Data")
st.dataframe(filtered_data)



st.subheader("Sales and Profit Chart")




st.line_chart(filtered_data[['Sales', 'Profit']])



st.subheader("Sales Bar Chart")
st.bar_chart(filtered_data['Sales'])


st.subheader("Summary Statistics")
st.write(filtered_data.describe())










