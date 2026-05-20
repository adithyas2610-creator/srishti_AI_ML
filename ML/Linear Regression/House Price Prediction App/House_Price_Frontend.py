import streamlit as st
import pandas as pd
from joblib import load

model=load("linear_model.pkl")
# scaler = load("scaler.pkl")

st.title("House Price Prediction App")

Medinc=st.number_input("Median Income",min_value=0.0,value=8.0)

HouseAge=st.number_input("House Age",min_value=1.0,value=20.0)

AveRooms=st.number_input("Average Rooms",min_value=0.0,value=5.0)

AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0)

Population = st.number_input("Population", min_value=0.0, value=1000.0)

AveOccup = st.number_input("Average Occupancy", min_value=0.0, value=3.0)

Latitude = st.number_input("Latitude", value=34.0)

Longitude = st.number_input("Longitude", value=-118.0)

if st.button("Predict House Price"):
    new_data=pd.DataFrame([[Medinc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]],
                          columns=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude'])
    
    prediction=model.predict(new_data)

    st.success(f"Predicted House Price : ${prediction[0]*100000:.2f}")
                         