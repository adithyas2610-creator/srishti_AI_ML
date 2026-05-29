import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Breast Cancer Prediction",
    page_icon="🩺",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #f8fbff, #e3f2fd);
    }

    .title {
        font-size: 42px;
        font-weight: bold;
        color: #0d47a1;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 18px;
        color: #37474f;
        text-align: center;
        margin-bottom: 25px;
    }

    .prediction-box {
        padding: 20px;
        border-radius: 15px;
        background-color: white;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
        margin-top: 20px;
    }

    .stButton>button {
        background-color: #1565c0;
        color: white;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #0d47a1;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🩺 Breast Cancer Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning based prediction using K-Nearest Neighbors (KNN)</div>', unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# ---------------- TRAIN MODEL ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# ---------------- SIDEBAR ----------------
st.sidebar.header("📋 About Project")
st.sidebar.info(
    "This application predicts whether a tumor is Malignant or Benign using the Breast Cancer Dataset and KNN algorithm."
)

st.sidebar.success("Model: K-Nearest Neighbors")
st.sidebar.write("Accuracy is usually above 95%.")

# ---------------- INPUT SECTION ----------------
st.subheader("🔍 Enter Tumor Details")

col1, col2, col3 = st.columns(3)

inputs = []

for i, feature in enumerate(X.columns[:15]):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        value = st.number_input(feature, value=float(X[feature].mean()))
        inputs.append(value)

for i, feature in enumerate(X.columns[15:]):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        value = st.number_input(feature, value=float(X[feature].mean()), key=feature)
        inputs.append(value)

# ---------------- PREDICTION ----------------
if st.button("Predict Cancer Type"):

    input_array = np.array(inputs).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    st.markdown('<div class="prediction-box">', unsafe_allow_html=True)

    if prediction == 0:
        st.error("⚠️ Prediction: Malignant Tumor")
        st.write(f"Confidence: {round(max(probability)*100, 2)}%")
    else:
        st.success("✅ Prediction: Benign Tumor")
        st.write(f"Confidence: {round(max(probability)*100, 2)}%")

    st.markdown("### 📊 Prediction Probability")

    prob_df = pd.DataFrame({
        "Category": ["Malignant", "Benign"],
        "Probability": probability
    })

    st.bar_chart(prob_df.set_index("Category"))

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DATA PREVIEW ----------------
with st.expander("📂 View Dataset"):
    st.dataframe(X.head())

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center>Developed using Streamlit ❤️ | Machine Learning Project</center>",
    unsafe_allow_html=True
)
