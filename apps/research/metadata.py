import streamlit as st

import yfinance as yf					# https://github.com/ranaroussi/yfinance

print ('yfinance version ========== ', yf.__version__)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# download Meta Data for a single Ticker
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# @st.cache(allow_output_mutation=True)
# @st.cache_data(show_spinner="Fetching data from API...")
@st.cache_resource()
def fetch_yfinance_metadata(ticker):
	print('cache_data - yf_ticker appears to be running')
	return yf.Ticker(ticker)


