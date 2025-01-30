import streamlit as st

st.set_page_config(page_title="Registration",
                   page_icon="🎉",
                   initial_sidebar_state="expanded")

st.title("Party Registration")
st.header("Come celebrate my birthday party")
st.subheader("Greg's 25th Birthday")

st.sidebar.title("Contact")
st.sidebar.subheader("We want to hear from you")
contactOption=st.sidebar.selectbox("How do you want to be contacted?",
                     options=["","email","call","text"])
if contactOption:
    st.sidebar.success(f"We will be {contactOption}ing you.")

with st.form("Registration",clear_on_submit=True):
    name = st.text_input("What is your name?",placeholder="First name and last name")
    age = st.number_input("How old are you?",min_value=21,step=1)
    email = st.text_input("Enter your email address",placeholder="email@email.com")
    major = st.selectbox("What is your major",options=[
        "","CS","Law","Marine Biology","Geology","Data Science and AI"
    ])
    level = st.selectbox("What is your degree", options=[
        "","Undergraduate","Masters","PhD","Other"
    ])
    subscribe = st.checkbox("Do you want to know about future events?")
    submit = st.form_submit_button("Submit")
    if name and age and email and major and level and subscribe:
        st.success(f"{name} has been successfully registered.")
    else:
        st.info("Please fill out the form to register for the party.")