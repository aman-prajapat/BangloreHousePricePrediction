import json
import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    attributes = np.zeros(len(__data_columns))

    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    attributes[0] = bath
    attributes[1] = bhk
    attributes[2] = sqft

    if loc_index >= 0:
        attributes[loc_index] = 1

    return round(__model.predict([attributes])[0],2)    #loca area bath bhk

def get_location_names():
    return __location

def load_saved_artifacts():
    print("Loading saved artifacts start........")
    global __location
    global __data_columns
    global  __model
    
    with open('columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open("Home_price_prediction_pickel_model",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved artifacts done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Indira Nagar',1000, 2, 2))
