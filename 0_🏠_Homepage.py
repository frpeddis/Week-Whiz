#Author: Francesco Peddis with ChatGPT

import streamlit as st
import streamlit.components.v1 as com
import time

st.set_page_config(page_title="🌀 Guess the Weekday!")

st.subheader("↖️ Your Calendar Challenge on the upper left sidebar")

com.iframe("https://lottie.host/?file=f8b3d68c-9de2-4a01-8c29-1bb24bbe72c6/Rafbgzfeae.json")

st.title("Welcome!!!  :sunglasses:")
#st.header("Guess the **weekday** for **any date!**")

text = "Guess the weekday for any date! "


t = st.empty()
for i in range(len(text) + 1):
    t.markdown("## %s" % text[0:i])
    time.sleep(0.05)

time.sleep(0.2)

st.subheader("With a little practice you can calculate it in your head... ") 
