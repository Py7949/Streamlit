import streamlit as st
st.title("Chai test poll")
col1, col2 = st.columns(2)
with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/16228436/pexels-photo-16228436/free-photo-of-a-table-with-a-tea-pot-and-a-candle-on-it.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",width=100)
    vote1 = st.button("Vote for Masala Chai")


with col2:
    st.header("Ginger chai")
    st.image("https://images.pexels.com/photos/29054033/pexels-photo-29054033/free-photo-of-elegant-overhead-view-of-tea-on-checkered-tablecloth.jpeg?auto=compress&cs=tinysrgb&w=600",width=100)
    vote2 = st.button("Vote for Ginger Chai")


if vote1:
    st.success("Thanks for voting for Masala Chai")
elif vote2:
    st.success("Thanks for voting for Ginger Chai")
else:
    st.info("Please vote for your favorite chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your favorite tea", ["Masala Chai", "Ginger Chai", "Green Tea", "Black Tea"])
st.write(f"Welcome {name} and yourfavorite tea is {tea}")

with st.expander("Show Chai Making instructions"):
    st.write("""
    1. Boil water in a pot.
    2. Add tea leaves and let it steep for a few minutes.
    3. Add milk and sugar to taste.
    4. Strain the tea into a cup and enjoy!
    """)
    st.markdown('### Welcome to Chai App')
    st.markdown('> Blockquote')