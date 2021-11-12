

import yfinance as yf
import streamlit as st




@st.cache
def fetch_yfinance_metadata(ticker):
	metadata = yf.Ticker(ticker)
	info = metadata.info
	divs = metadata.dividends
	return metadata, info, divs



	

