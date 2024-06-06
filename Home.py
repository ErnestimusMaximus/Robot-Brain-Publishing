# Home.py
import streamlit as st

st.title('Robot Brain Publishing')

st.write("Here's our first attempt at writing books!")
username = st.text_input("Enter your name")
if username != "":
    st.write(f"Hello, {username}!")
else: 
    st.write(f"What's your name?")
