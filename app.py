import streamlit as st
import yfinance as yf

# Page configuration
st.set_page_config(page_title="Crypto Watcher", page_icon="📈", layout="centered")

# Title and description
st.title("Crypto & Stock Market Watcher 📈")
st.write("Track live prices and charts of your favorite digital assets.")

st.write("---")

# Dropdown menu to select the Crypto
crypto_asset = st.selectbox(
    "Select an asset to track:",
    ["BTC-USD", "ETH-USD", "SOL-USD", "DOGE-USD"]
)

# Fetching data from Yahoo Finance
with st.spinner("Fetching live data from the market..."):
    ticker_data = yf.Ticker(crypto_asset)
    # Get history for the last 30 days
    history = ticker_data.history(period="30d")

if not history.empty:
    # Get the latest close price
    current_price = history['Close'].iloc[-1]
    
    # Display the price beautifully
    st.metric(label=f"Current Price of {crypto_asset}", value=f"${current_price:,.2f}")
    
    st.write("### Price Trend (Last 30 Days)")
    # Draw a beautiful line chart automatically
    st.line_chart(history['Close'])
else:
    st.error("Error: Could not load market data. Please refresh the page.")
