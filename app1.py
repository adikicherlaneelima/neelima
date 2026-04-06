import streamlit as st
import matplotlib.pyplot as plt
from utils import load_data, get_close_prices
from model import moving_average, predict_next

st.set_page_config(page_title="Stock Predictor", layout="centered")

st.title("📊 Stock Price Predictor (Simple)")

# Sidebar controls
st.sidebar.header("Settings")
window = st.sidebar.slider("Moving Average Window", 2, 10, 5)

file = st.file_uploader("Upload your stock CSV", type=["csv"])

if file is not None:
    df = load_data(file)
    prices = get_close_prices(df)

    st.subheader("📋 Last 5 Records")
    st.dataframe(df.tail())

    # Prediction
    next_price = predict_next(prices, window)
    st.metric("📈 Predicted Next Price", f"{next_price:.2f}")

    # Moving average
    ma = moving_average(prices, window)

    # Plot
    st.subheader("📉 Price Chart")
    fig, ax = plt.subplots()
    ax.plot(prices, label="Actual Prices", color="blue")
    ax.plot(range(window-1, len(prices)), ma, label="Moving Average", color="orange")
    ax.legend()
    ax.set_xlabel("Days")
    ax.set_ylabel("Price")

    st.pyplot(fig)

else:
    st.info("Please upload a CSV file to continue.")