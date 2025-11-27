import streamlit as st
import requests




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







# Random JOke generator


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






 

#  any random DOG image generator






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




# RAndom  FAct  generator:








st.title("Random Fact Generator")

if st.button("Get Fact"):


    url = "https://uselessfacts.jsph.pl/random.json?language=en"


    response = requests.get(url)
    if response.status_code == 200:
        fact = response.json()["text"]


        st.success(fact)
    else:
        st.error("Failed to fetch a fact")



