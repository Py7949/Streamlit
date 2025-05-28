import streamlit as st
import pandas as pd

st.title("Chai sales dashboard")

file = st.file_uploader ("Upload your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)    

if file:
    st.subheader("Summary stats")   
    st.write(df.describe())    

if file:
    cities = df["City"].unique()             
    selected_city = st.selectbox("Filter by cities", cities)
    filtered_data = df["City"] == selected_city