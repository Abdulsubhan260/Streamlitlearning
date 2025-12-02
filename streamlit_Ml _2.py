import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

st.write("""
# House Price Prediction App (KNN)
Predict the price of a house using K-Nearest Neighbors!
""")


st.sidebar.header('User Input Features')

def user_input_features():
    MedInc = st.sidebar.slider('Median Income (10k USD)', 0.5, 15.0, 3.0)
    HouseAge = st.sidebar.slider('House Age', 1, 52, 20)
    AveRooms = st.sidebar.slider('Average Rooms', 1.0, 10.0, 5.0)
    AveBedrms = st.sidebar.slider('Average Bedrooms', 0.5, 5.0, 1.0)
    Population = st.sidebar.slider('Population', 3, 3500, 1000)
    AveOccup = st.sidebar.slider('Average Occupancy', 1.0, 10.0, 3.0)
    Latitude = st.sidebar.slider('Latitude', 32.5, 42.0, 34.0)
    Longitude = st.sidebar.slider('Longitude', -124.0, -114.0, -118.0)

    data = {'MedInc': MedInc,
            'HouseAge': HouseAge,
            'AveRooms': AveRooms,
            'AveBedrms': AveBedrms,
            'Population': Population,
            'AveOccup': AveOccup,
            'Latitude': Latitude,
            'Longitude': Longitude}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


st.subheader('User Input parameters')
st.write(df)


housing = fetch_california_housing(as_frame=True)
X = housing.data
y = housing.target


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
df_scaled = scaler.transform(df)


knn_model = KNeighborsRegressor(n_neighbors=5)  
knn_model.fit(X_scaled, y)


prediction = knn_model.predict(df_scaled)

st.subheader('Predicted House Price (in 100k USD)')
st.write(round(prediction[0], 2))
