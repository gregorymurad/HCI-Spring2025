import streamlit as st
import datetime

st.set_page_config(layout="wide")

st.title("My First Web App for HCI")
st.header("CAP 4104 - Human-Computer Interaction")
st.subheader("Prof. Greg Reis")

st.divider()

st.write("Registration Form")

first_name = st.text_input("Enter first name")
last_name = st.text_input("Enter last name")
year_of_birth = st.number_input("Enter your year of birth")
start_year_at_fiu = st.number_input("Enter the year you started at FIU")

current_year = datetime.date.today().year
age = current_year - year_of_birth
years_at_fiu = current_year - start_year_at_fiu

if first_name and last_name and year_of_birth and start_year_at_fiu:
    st.success(f"Hi {first_name}, you are {age} years old, and you have "
               f"been working at FIU for {years_at_fiu} years.")

else:
    st.info("Please fill out the form")