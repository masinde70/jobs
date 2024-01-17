import streamlit as st 

st.title = ("Stateful apps")

st.write("Here is the session state: ")
st.write(st.session_state)
st.button("Update state")

# set the value using the key-value syntax
if "key" not in st.session_state:
    st.session_state["key"] = "value"

# set the value using the attribute syntax
if "attribute" not in st.session_state:
    st.session_state.attribute = "another value"

# Read the value from the session state
st.write(f"Reading with key-value syntax: {st.session_state['key']}")
st.write(f"Reading with attribute syntax: {st.session_state.attribute}")

# Update value in state
st.session_state["key"] = "new value"
st.session_state.attribute = "another new value"
    