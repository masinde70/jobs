import streamlit as st
import yfinance as yf
import pandas as pd
from st_aggrid import AgGrid
import plotly.express as px

# Function to fetch stock data
def fetch_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Function to calculate the simple moving average
def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

st.title("Stock Data Visualization Tool")

# Initialize session state variables if they don't already exist
if 'symbol' not in st.session_state:
    st.session_state['symbol'] = 'AAPL'

if 'start_date' not in st.session_state:
    st.session_state['start_date'] = pd.to_datetime("2020-01-01")

if 'end_date' not in st.session_state:
    st.session_state['end_date'] = pd.to_datetime("today")

# Text input for the stock symbol
symbol = st.text_input("Enter Stock Symbol", st.session_state['symbol'])

# Date input for the start and end dates
start_date = st.date_input("Start Date", st.session_state['start_date'])
end_date = st.date_input("End Date", st.session_state['end_date'])

# Numeric input for the moving average window
ma_window = st.number_input("Moving Average Window (days)", min_value=1, max_value=365, value=20)

if st.button("Fetch Data"):
    # Update session state
    st.session_state['symbol'] = symbol
    st.session_state['start_date'] = start_date
    st.session_state['end_date'] = end_date

    # Fetch and display the data
    df = fetch_stock_data(symbol, start_date, end_date)

    # Calculate the moving average
    df['SMA'] = calculate_sma(df, ma_window)

    # Display the data using ag-Grid
    AgGrid(df, width='100%', height='400px')

    # Plotting the data using Plotly
    fig = px.line(df, x=df.index, y=['Close', 'SMA'], title=f'Closing Price and {ma_window}-Day SMA of {symbol}')
    st.plotly_chart(fig)
