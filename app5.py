import streamlit as st
import requests


st.title("Crypto Monitoring")
st.header("Find the lates Cryptocurrency price updates")

crypto = st.selectbox("Choose a cryptocurrenty", options=[
    "","Bitcoin","Litecoin","Ripple"
])

if crypto == "Bitcoin":
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    response = requests.get(url).json()
    btc_price = response["USD"]
    st.success(f"The current price of {crypto} is US$ {btc_price}.")

elif crypto == "Litecoin":
    url = "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD"
    response = requests.get(url).json()
    ltc_price = response["USD"]
    st.success(f"The current price of {crypto} is US$ {ltc_price}.")

elif crypto == "Ripple":
    url = "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD"
    response = requests.get(url).json()
    xrp_price = response["USD"]
    st.success(f"The current price of {crypto} is US$ {xrp_price}.")

else:
    st.info("Please choose a cryptocurrency.")
# TODO: Complete the code to include Litecoin (LTC) and Ripple (XRP)