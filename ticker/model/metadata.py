import streamlit as st

import yfinance as yf					# https://github.com/ranaroussi/yfinance


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# download Meta Data for a single Ticker
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
@st.cache
def fetch_yfinance_metadata(ticker):
	metadata = yf.Ticker(ticker)
	info = metadata.info
	divs = metadata.dividends
	return metadata, info, divs


