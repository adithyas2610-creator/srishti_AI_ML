# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix

st.set_page_config(
    page_title="Internship Selection Prediction",
    layout="wide"
)

df = pd.read_csv("C:/Users/ADHITHYA/Downloads/archive (1)/Internship_Selection_Dataset.csv")

df.columns = df.columns.str.strip()

model = pickle.load(open("svm_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


target_column = "PlacementStatus"

x = df.drop("selected", axis=1)
y = df["selected"]

menu = st.sidebar.selectbox(
    "Navigation",
    ["Home", "About", "Prediction", "Results"]
)

if menu == "Home":

    st.title("🎓 Internship Selection Prediction System")

    st.header("📌 Project Introduction")

    st.write("""
    This project predicts whether a student
    will get selected for an internship.
    """)

    st.header("📊 Dataset Details")

    st.write("""
    Dataset contains:
    - CGPA
    - Skills
    - Projects
    - Communication
    - Aptitude
    - Internship Experience
    """)

    st.header("🎯 Objectives")

    st.write("""
    - Predict internship selection
    - Compare machine learning algorithms
    - Build interactive Streamlit app
    """)

    st.header("✅ Advantages")

    col1, col2 = st.columns(2)

    with col1:
        st.success("Fast prediction")
        st.success("User friendly")

    with col2:
        st.success("Interactive UI")
        st.success("Good accuracy")

elif menu == "About":

    st.title("ℹ About Project")

    st.header("What is SVM?")

    st.write("""
    Support Vector Machine (SVM)
    is a supervised learning algorithm
    used for classification problems.
    """)

    st.header("🛠 Technologies Used")

    st.write("""
    - Python
    - Pandas
    - NumPy
    - Scikit-Learn
    - Streamlit
    - Matplotlib
    - Seaborn
    """)

    st.header("👨‍💻 Team Members")

    st.write("""
    - Adithya Suresh
    - Surya T V
    """)

elif menu == "Prediction":

    st.title("🔍 Internship Prediction")

    st.header("Enter Student Details")

    input_data = []

    for column in x.columns:

        value = st.number_input(
            f"Enter {column}",
            min_value=0.0,
            step=0.1
        )

        input_data.append(value)

    input_array = np.array(input_data).reshape(1, -1)

    input_scaled = scaler.transform(input_array)

    if st.button("Predict"):

        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.success("🎉 Selected for Internship")
        else:
            st.error("❌ Not Selected")


    st.header("📄 Resume Score Calculator")

    cgpa = st.slider("CGPA", 0.0, 10.0, 5.0)

    projects = st.slider("Projects", 0, 10, 2)

    skills = st.slider("Skills", 0, 10, 5)

    score = (cgpa * 5) + (projects * 3) + (skills * 2)

    st.metric("Resume Score", score)

elif menu == "Results":

    st.title("📈 Results")

    st.header("📄 Dataset Preview")

    st.dataframe(df.head())

    st.header("📊 Dataset Shape")

    st.write(df.shape)

    st.header("📉 Correlation Heatmap")

    # Create numeric dataset

    df_numeric = df.copy()

    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()

    for col in df_numeric.columns:
        if df_numeric[col].dtype == 'object':
            df_numeric[col] = le.fit_transform(df_numeric[col])

    # Heatmap

    fig, ax = plt.subplots(figsize=(12, 8))

    sns.heatmap(df_numeric.corr(), annot=True, cmap="coolwarm")

    st.pyplot(fig)

    st.header("⬇ Download Dataset")

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="dataset.csv",
        mime="text/csv"
    )