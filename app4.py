import streamlit as st
import pandas as pd
import numpy as np
from datetime import time


st.title("Charts, Images, and Videos")
st.sidebar.title("Test")
st.markdown("INSERT YOUR HTML/CSS CODE HERE",unsafe_allow_html=True)
basic_plots = st.checkbox("Basic Plots")

if basic_plots:
    df = pd.DataFrame(
        np.random.rand(20,3),
        columns=["A","B","C"]
    )
    st.dataframe(df)
    st.line_chart(df)

sliders = st.checkbox("Sliders")
if sliders:
    age = st.slider("How old are you?",18,130,20)
    someRange = st.slider("Select a range",
                          0.,200.,(25.,50.))
    officeHours = st.slider("Select an appointment timeslot",
                            value=(time(10,30),time(12,30)))

my_data = pd.read_csv("oct25-2024.csv")
st.dataframe(my_data)