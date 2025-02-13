import streamlit as st


st.title("Temperature Converter")

def convertFtoC(temp):
    return (float(temp)-32.) * 5./9.

def convertCtoF(temp):
    return (float(temp)*9./5.) + 32.

temp_input = st.slider("Select a temperature value",
                       min_value=-100,
                       max_value=200,
                       value=32)

conv_type = st.radio("Select a conversion type",options=[
    "Fahrenheit to Celsius",
    "Celsius to Fahrenheit"
])

if conv_type == "Fahrenheit to Celsius":
    output = convertFtoC(temp_input)
    st.metric(label="Converted Temperature",value=f"{output:.2f} C")

elif conv_type == "Celsius to Fahrenheit":
    output = convertCtoF(temp_input)
    st.metric(label="Converted Temperature", value=f"{output:.2f} F")

if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append((temp_input,conv_type,output))
print(st.session_state.history)

st.divider()
history_data = st.session_state.history

rev = list(reversed(st.session_state.history[-5:]))
st.subheader("Conversion History")

for i,(temp,conv,output) in enumerate(rev,1):
    st.write(f"{i}. {temp} ({conv}) -> {output}")