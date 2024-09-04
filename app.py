import streamlit as st
import pickle
import pandas as pd
from sklearn import preprocessing
import numpy as np


model = pickle.load(open('model_pickle.pkl', 'rb'))


def button(label):
    return f'{label}'


options = ["Select Option", 'NEAR BAY',
    'NEAR OCEAN', 'INLAND', 'ISLAND', 'COAST']


st.title("House Price Prediction")

with st.form('form1'):
    longitude = st.number_input('Longitude', 0)
    latitude = st.number_input('Latitude', 0)
    housing_median_age = st.number_input('Housing median age', 0)
    total_rooms = st.number_input('Total rooms', 0)
    total_bedrooms = st.number_input('Total bedrooms', 0)
    population = st.number_input('Population', 0)
    households = st.number_input('Households', 0)
    median_income = st.number_input('Median income', 0)
    ocean_proximity = st.selectbox(
        'Ocean proximity', options, format_func=button, index=0)
    # ocean_proximity = st.multiselect('Ocean proximity', )

    predict = st.form_submit_button('Predict')

    longitude = float(longitude)
    latitude = float(latitude)
    housing_median_age = float(housing_median_age)
    total_rooms = float(total_rooms)
    total_bedrooms = float(total_bedrooms)
    population = float(population)
    households = float(households)
    median_income = float(median_income)
    ocean_proximity = str(ocean_proximity)


    if ocean_proximity == 'Select Option':
        ocean_proximity_value = 0
    else:
        ocean_proximity_value = ocean_proximity

    user_data = {
        'longitude':longitude,
        'latitude':latitude,
        'housing_median_age':housing_median_age,
        'total_rooms':total_rooms,
        'total_bedrooms':total_bedrooms,
        'population':population,
        'households' : households,
        'median_income':median_income,
        'ocean_proximity':ocean_proximity_value
    }

    data = pd.DataFrame(user_data, index=[0])
   

    le = preprocessing.LabelEncoder()
    le.fit(data['ocean_proximity'])


    data['ocean_proximity'] = le.transform(data['ocean_proximity'])
    data['total_rooms'] = np.log(data['total_rooms'] + 1)
    data['total_bedrooms'] = np.log(data['total_bedrooms'] + 1)
    data['population'] = np.log(data['population'] + 1)
    data['households'] = np.log(data['households'] + 1)

    rf_y_pred = model.predict(data)
    st.write(rf_y_pred)
   






