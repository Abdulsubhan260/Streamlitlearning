import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


st.set_page_config(page_title="Covid Predictor", page_icon="🦠")

st.title("COVID Probability Predictor")
st.write("Find probability of COVID based on your symptoms")


data = {
    'Fever': [1,0,1,0,1,0,1,0],
    'Cough': [1,1,0,0,1,0,1,1],
    'SoreThroat': [1,0,1,0,1,0,1,0],
    'LossTasteSmell': [1,0,1,0,1,0,1,1],
    'COVID_Positive': [1,0,1,0,1,0,1,1]
}

df = pd.DataFrame(data)

X = df[['Fever','Cough','SoreThroat','LossTasteSmell']]
y = df['COVID_Positive']


model = DecisionTreeClassifier()
model.fit(X, y)


st.sidebar.header('Select Your Symptoms')

def user_input_features():
    Fever = st.sidebar.selectbox('Fever', ['No','Yes'])
    Cough = st.sidebar.selectbox('Cough', ['No','Yes'])
    SoreThroat = st.sidebar.selectbox('Sore Throat', ['No','Yes'])
    LossTasteSmell = st.sidebar.selectbox('Loss of Taste/Smell', ['No','Yes'])

    data = {
        'Fever': [1 if Fever=='Yes' else 0],
        'Cough': [1 if Cough=='Yes' else 0],
        'SoreThroat': [1 if SoreThroat=='Yes' else 0],
        'LossTasteSmell': [1 if LossTasteSmell=='Yes' else 0]
    }

    features = pd.DataFrame(data, columns=X.columns)
    return features

df_input = user_input_features()

st.subheader('Your Symptoms')
st.write(df_input)


prediction_proba = model.predict_proba(df_input)

st.subheader('Predicted COVID Probability')
prob = prediction_proba[0][1]*100
st.write(f"**{prob:.2f}%**")

if prob > 50:
    st.warning("You have a high probability of COVID symptoms.")
else:
    st.success("Your symptoms currently indicate low probability.")