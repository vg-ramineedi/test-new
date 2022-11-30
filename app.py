import streamlit as st
import math

st.set_page_config(page_title="Simple Multiplier",
                   page_icon=":heavy_multiplication_x:")
with st.container():
    st.title("Multiplication app")

    # Input
    # calInput = st.text_input("Enter here:", placeholder="3*5")
    # ans = math.eval(calInput)
    a = st.number_input("First number:", step=0.10)
    b = st.number_input("Second number:", step=0.10)
    ans = a*b
    st.success(f"Answer: {ans}")
