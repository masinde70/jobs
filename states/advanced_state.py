import streamlit as st
from datetime import datetime, timedelta

st.title("Advance state Management")

# Store widget value in session state
st.subheader("Store widget value in session state")

st.slider("select a number", 0, 10, key="slider")
st.write(st.session_state)

# Initialize widget value with session state
st.subheader("Initialize widget value with session state")
if "num_input" not in st.session_state:
    st.session_state["num_input"] = 5

# Callbacks
st.subheader("use callbacks")

st.markdown("### select your time range")

st.radio("select a range", ["7 days", "28 days", "custom"], horizontal=True)