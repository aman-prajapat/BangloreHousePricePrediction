import streamlit as st
import json
import joblib
import numpy as np

__data_columns = None
__location = None
__model = None

def load_article():
    global model
    global __data_columns 
    global __location 

    with open("Home_price_prediction_pickel_model",'rb') as f:
       model = joblib.load(f)

    with open('columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

def pred(bath,bhk,sqft,city):
    attributes = np.zeros(len(__data_columns))
    attributes[0] = bath
    attributes[1] = bhk
    attributes[2] = sqft
    try:
        loc_index = __data_columns.index(city)
    except:
        loc_index = -1

    if loc_index >= 0:
        attributes[loc_index] = 1
    

    return model.predict([attributes])[0]

load_article()

st.title('Home Price Prediction ')

BHK = st.number_input('BHK',min_value=0,max_value = 5,step = 1)
bath = st.number_input('Bath',min_value=0,max_value= 5,step = 1)
area = st.number_input('Area (Square Feet)',step = 1000)
city = st.selectbox('City', __location)

if st.button('Estimate Price'):
    result =  round(pred(bath,BHK,area,city),2)
    st.success(F'{result} Lake Rs.')
