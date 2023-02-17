import streamlit as st


name = st.text_input('enter your name', key=1)
st.write(name)

age = st.text_input('enter your age', key=2)
st.write(age)
