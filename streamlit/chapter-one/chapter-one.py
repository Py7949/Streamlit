import streamlit as st

st.title("Hello, chai app")
st.subheader("Brewed with streamlit")
st.text("Welcome to first interactive app")
st.write("choose your fav.variety of chai")

chai = st.selectbox("Select your favorite chai:",["Masala Chai","Ginger Chai","Kesar Chai","Lemon Chai"])
st.write(f"You selected: {chai}.Excellent choice!")
st.success("Your chai is brewed")