import streamlit as st 

def lbs_to_kg():
    # Define the conversion logic here
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    # Define the conversion logic here
    st.session_state.lbs = st.session_state.kg*2.2046

st.title("States")

"st.session_state object:", st.session_state

col1, space, col2 = st.columns([2, .5, 2])

with col1:
    pounds = st.number_input("Pounds", key="lbs", on_change= lbs_to_kg)
with col2:
    kilograms = st.number_input("Kilograms", key="kg", on_change= kg_to_lbs)



def form_callback():
    st.write(st.session_state.my_slider)
    st.write(st.session_state.my_checkbox)

with st.form(key='my_form'):
    slider_input = st.slider('My slider', 0, 10, 5, key='my_slider')
    checkbox_input = st.checkbox('Yes or No', key='my_checkbox')
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)