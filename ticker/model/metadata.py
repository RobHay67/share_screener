import streamlit as st

import yfinance as yf					# https://github.com/ranaroussi/yfinance


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# download Meta Data for a single Ticker
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

@st.cache(allow_output_mutation=True)
def fetch_yfinance_metadata(ticker):
	return yf.Ticker(ticker)


