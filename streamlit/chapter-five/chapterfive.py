import streamlit as st
import requests
st.title("Live currency converter")
amount = st.number_input("Enter the amount in INR", min_value=1)

target_currency = st.selectbox("Convert to",["USD", "EUR", "GBP", "JPY", "AUD"])

if st.button("Convert"):
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rates = data["rates"][target_currency]
        converted = rates * amount
        st.success(f"{amount} INR = {converted}{target_currency} ")    
    else:
        st.error("Currency not supported.")