#Author: Francesco Peddis with ChatGPT

import streamlit as st

# Define the URL of the image on GitHub
image_url = "https://raw.githubusercontent.com/frpeddis/Week-Whiz/6231a03f8af9cbe9bdae1d1bab0136fe4af64735/Image%2023-08-23%20at%2017.23.jpeg"

# Display the image using Streamlit
st.image(image_url, caption='Image from GitHub', use_column_width=True)

st.set_page_config(page_title="🌀 Guess the weekday! - by FP")

st.write("↖️ Your Calendar Challenge on upper left sidebar")

st.title("Welcome!!!  :sunglasses:")
st.header("🗓️ Guess the **weekday** for **any date!**")
st.write("You just need simple basic math and a little bit of memory... ") 
st.write("Let's give it a try!")


 
st.sidebar.success("Select your challenge ")
