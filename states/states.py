import streamlit as st 

st.title("States")

"st.session_state object:", st.session_state

## Works with all widgets
number = st.slider("A number", 1, 10, key="slider")

st.write(st.session_state)

col1, buff, col2 = st.columns([1, .5, 3])
option_names = ["a", "b", "c"]

option = col1.radio("Pick an option", option_names, key="radio_option")
st.session_state

if option == "a":
    col2.write("You picked 'a' :smile:")
elif option == "b":
    col2.write("You picked 'b' :heart:")
else:
    col2.write("You picked 'c' :sunglasses:")