import streamlit as st
import pandas as pd
from joblib import load

model = load("logistic_model.pkl")

st.title("Titanic Survival Prediction")

pclass = st.selectbox("Passenger Class", ["First Class", "Second Class", "Third Class"])

gender = st.selectbox("Gender",["Male", "Female"])

age = st.number_input( "Age", min_value=1.0, max_value=100.0,value=25.0)

sibsp = st.number_input("Siblings/Spouses", min_value=0, value=0)

parch = st.number_input("Parents/Children",min_value=0,value=0)


embarked = st.selectbox("Embarked",["C", "Q", "S"])

pclass_map = { "First Class": 1,"Second Class": 2,"Third Class": 3}

gender_map = {"Male": 1,"Female": 0}

embarked_map = {"C": 0,"Q": 1,"S": 2}

encoded_pclass = pclass_map[pclass]
encoded_gender = gender_map[gender]
encoded_embarked = embarked_map[embarked]

if st.button("Predict"):

   
    new_data = pd.DataFrame([[encoded_pclass,encoded_gender,age,sibsp,parch,encoded_embarked]],
            columns=['Pclass','Sex','Age','SibSp','Parch','Embarked'])

    
    prediction = model.predict(new_data)[0]

    if prediction == 1:
        st.success("Passenger Survived")
    else:
        st.error("Passenger Died")