import streamlit as st


st.set_page_config(page_title="🌀 Guess the right day! - by FP")
image_url = "https://raw.githubusercontent.com/frpeddis/Week-Whiz/927ecd1e0f19513b2e0887675fecfe4da17577a7/Image%2023-08-23%20at%2017.09.jpeg"

st.image(image_url, use_column_width=True)
st.title("Welcome!!!  :sunglasses:")
st.header("🗓️ Guess the **day of the week** for any **date**!")
st.write("You just need simple basic math and a little bit of memory... ") 
st.write("Let's give it a try!")

st.header("↖️ Your Calendar Challenge from the sidebar up on the left")

 
st.sidebar.success("Select your challenge ")
