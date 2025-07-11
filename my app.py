import streamlit as st
import pandas as pd
import numpy as np
import joblib
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# Streamlit page config
st.set_page_config(page_title="NYC Taxi Fare Predictor", layout="centered")
st.title("NYC Taxi Fare Prediction")

# Sidebar Inputs
st.sidebar.header("Trip Inputs")
pickup_lat = st.sidebar.number_input("Pickup Latitude", value=40.761432)
pickup_lon = st.sidebar.number_input("Pickup Longitude", value=-73.979815)
dropoff_lat = st.sidebar.number_input("Dropoff Latitude", value=40.651311)
dropoff_lon = st.sidebar.number_input("Dropoff Longitude", value=-73.880333)
passenger_count = st.sidebar.slider("Passengers", 1, 6, 1)
hour = st.sidebar.slider("Hour of Pickup", 0, 23, 14)
day_of_week = st.sidebar.selectbox("Day of Week (0=Mon, 6=Sun)", list(range(7)))
is_weekend = 1 if day_of_week in [5, 6] else 0

# Calculate distance between pickup and dropoff
distance_km = geodesic((pickup_lat, pickup_lon), (dropoff_lat, dropoff_lon)).km

# Create input DataFrame for prediction
input_data = {
    'passenger_count': passenger_count,
    'hour': hour,
    'day_of_week': day_of_week,
    'is_weekend': is_weekend,
    'distance_km': distance_km
}

# Load the trained model and predict fare
try:
    model = joblib.load('taxi_fare_model.pkl')  # Model must be in the same folder

    if st.button("Predict Fare"):
        prediction = model.predict(pd.DataFrame([input_data]))[0]
        st.success(f"Estimated Fare: ${prediction:.2f}")

        # Show map with Folium
        m = folium.Map(location=[pickup_lat, pickup_lon], zoom_start=12)
        folium.Marker([pickup_lat, pickup_lon], tooltip="Pickup", icon=folium.Icon(color='green')).add_to(m)
        folium.Marker([dropoff_lat, dropoff_lon], tooltip="Dropoff", icon=folium.Icon(color='red')).add_to(m)
        folium.PolyLine([[pickup_lat, pickup_lon], [dropoff_lat, dropoff_lon]], color="blue").add_to(m)
        st_folium(m, width=700, height=500)

except FileNotFoundError:
    st.error(" Model file 'taxi_fare_model.pkl' not found. Please make sure it's in the app folder.")
