import streamlit as st 

st.title("States")

"st.session_state object:", st.session_state

## Works with all widgets
number = st.slider("A number", 1, 10, key="slider")

st.write(st.session_state)