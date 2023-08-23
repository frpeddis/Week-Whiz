import streamlit as st


import requests
from PIL import Image
from io import BytesIO

# URL of the image on GitHub
image_url = "https://raw.githubusercontent.com/frpeddis/Week-Whiz/70c8739a6cc23b1f494c0453119bd2ac348c705d/Image%2023-08-23%20at%2017.23.jpeg"

# Fetch the image from the URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Display the image using st.image
st.image(image, use_container_width=True)

st.set_page_config(page_title="🌀 Guess the right day! - by FP")


st.title("Welcome!!!  :sunglasses:")
#image_url = "https://raw.githubusercontent.com/frpeddis/Week-Whiz/927ecd1e0f19513b2e0887675fecfe4da17577a7/Image%2023-08-23%20at%2017.09.jpeg"

#st.image(image_url, width=0.3)
st.header("🗓️ Guess the **day of the week** for any **date**!")
st.write("You just need simple basic math and a little bit of memory... ") 
st.write("Let's give it a try!")

st.header("↖️ Your Calendar Challenge from the sidebar up on the left")

 
st.sidebar.success("Select your challenge ")
