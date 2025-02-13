import streamlit as st

st.title("🔢 Simple Counter using st.session_state")

# Properly initialize session state variable
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Function to increment counter
def increase():
    st.session_state.counter += 1

# Function to reset counter
def reset():
    st.session_state.counter = 0

# Display counter value
st.write(f"Current Count: **{st.session_state.counter}**")

# Buttons to increase or reset the counter
col1, col2 = st.columns(2)
with col1:
    st.button("➕ Increase", on_click=increase)

with col2:
    st.button("🔄 Reset", on_click=reset)


###########################################################################

import streamlit as st

# Convert temperature functions
def convert_f_to_c(temp):
    return (float(temp) - 32.) * 5. / 9.

def convert_c_to_f(temp):
    return (float(temp) * 9. / 5.) + 32.

# App title and description
st.title("🌡️ Interactive Temperature Converter")
st.write("Convert temperatures between Fahrenheit and Celsius in real time!")

# Interactive input
temp_input = st.slider("Select a temperature value", min_value=-100, max_value=200, value=32)

conv_type = st.radio("Select a conversion type:", ["Fahrenheit to Celsius", "Celsius to Fahrenheit"])

# Conversion and Display
if conv_type == "Fahrenheit to Celsius":
    output = convert_f_to_c(temp_input)
    st.metric(label="Converted Temperature", value=f"{output:.2f} ºC")
    st.write(f"🔥 {temp_input} F is **{output:.2f} ºC**")

elif conv_type == "Celsius to Fahrenheit":
    output = convert_c_to_f(temp_input)
    st.metric(label="Converted Temperature", value=f"{output:.2f} ºF")
    st.write(f"❄️ {temp_input} ºC is **{output:.2f} F**")

# Bonus Feature: Display both conversions simultaneously
st.subheader("🔄 Quick Reference")
st.write(f"🌡️ {temp_input} F is **{convert_f_to_c(temp_input):.2f} ºC**")
st.write(f"🌡️ {temp_input} ºC is **{convert_c_to_f(temp_input):.2f} F**")

# Themed Background Message Based on Temperature
if temp_input > 100:
    st.warning("🔥 That's really hot! Stay hydrated!")
elif temp_input < 0:
    st.warning("❄️ Brrr! It's freezing! Wear warm clothes!")
else:
    st.info("🌤️ A nice and comfortable temperature!")

# Keep track of conversion history
if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.append((temp_input, conv_type, output))

st.subheader("📜 Conversion History")
# for i, (temp, conv, result) in enumerate(reversed(st.session_state.history[-5:]), 1):
#     st.write(f"{i}. {temp} ({conv}) → {result:.2f}")

print(st.session_state.history)
rev=list(reversed(st.session_state.history[-5:]))
print(rev)
for i, (temp, conv, result) in enumerate(rev, 1):
    st.write(f"{i}. {temp} ({conv}) → {result:.2f}")