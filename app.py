import streamlit as st
import pandas as pd
import joblib

FEATURE_NAMES = ["Annual Income (k$)", "Spending Score (1-100)"]

# ------------------------------------------------------------
# Load model + scaler (cached so it only loads once)
# ------------------------------------------------------------
@st.cache_resource
def load_model():
    kmeans = joblib.load("kmeans_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return kmeans, scaler

kmeans, scaler = load_model()

# ------------------------------------------------------------
# Page setup
# ------------------------------------------------------------
st.set_page_config(page_title="Customer Segmentation", page_icon="🛍️")
st.title("🛍️ Customer Segmentation")
st.write("Enter a customer's details to see which segment they belong to.")

# ------------------------------------------------------------
# Input form
# ------------------------------------------------------------
income = st.number_input("Annual Income (k$)", min_value=0, max_value=500, value=60)
spending_score = st.slider("Spending Score (1-100)", 1, 100, 50)

if st.button("Predict Segment"):
    input_df = pd.DataFrame([{
        "Annual Income (k$)": income,
        "Spending Score (1-100)": spending_score,
    }])
    scaled_input = scaler.transform(input_df)
    cluster = kmeans.predict(scaled_input)[0]
    st.success(f"Predicted Segment: **Cluster {cluster}**")

# ------------------------------------------------------------
# Optional: show cluster centers in real units
# ------------------------------------------------------------
with st.expander("View cluster centers"):
    centers = pd.DataFrame(
        scaler.inverse_transform(kmeans.cluster_centers_),
        columns=FEATURE_NAMES,
    )
    st.dataframe(centers)
