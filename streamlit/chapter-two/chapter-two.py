import streamlit as st
st.title("Chai maker app")

if st.button("Make Chai"):
    st.success("Your chai is being brewed!")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala is being added to your chai!")

tea_type = st.radio("Choose your chai base:",["Milk","Water","Honey","Sugar","Almond Milk"])
st.write(f"You have chosen {tea_type} as your chai base.")

flavour = st.selectbox("Choose your flavour:",["Cardamom","Ginger","Mint","Lemon","Cinnamon"])
st.write(f"You have chosen {flavour} as your flavour.")

sugar = st.slider("How much sugar do you want?", 0, 10, 5)
st.write(f"You have chosen {sugar} teaspoons of sugar.")

st.number_input("How many cups of chai do you want?", min_value=1, max_value=10, value=1)
st.write(f"Selected sugar level: {sugar} teaspoons")
name = st.text_input("Enter your name:", placeholder="Your Name")
if name:
    st.write(f"Welcome, {name} ! Your chai is on the way")
st.text_area("Enter any special instructions:", placeholder="Special Instructions")
st.date_input("Select a date for your chai delivery:")
st.time_input("Select a time for your chai delivery:")
st.selectbox("Choose a delivery method:", ["Pickup", "Delivery"])
st.color_picker("Pick a color for your chai:", "#FF5733")
st.button("Submit Order")
st.success("Your order has been placed successfully!")