# Feb 6th 2025

import streamlit as st

st.title("A Counter and State Management")

if "counter" not in st.session_state:
    st.session_state.counter = 0

def increase():
    st.session_state.counter += 1

def reset():
    st.session_state.counter = 0

st.write(f"The current value of the counter is {st.session_state.counter}.")

col1, col2 = st.columns(2)

with col1:
    st.button("Increase", on_click=increase)
with col2:
    st.button("Reset", on_click=reset)