import streamlit as st

import yfinance as yf					# https://github.com/ranaroussi/yfinance

# print ('yfinance version ========== ', yf.__version__)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# download Meta Data for a single Ticker
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# import yfinance as yf
# print (yf.__version__)
# metadata = yf.Ticker('CBA.AX')
# for key in metadata.info:print(key)




# @st.cache(allow_output_mutation=True)
# @st.cache_data(show_spinner="Fetching data from API...")
@st.cache_resource()
def fetch_yfinance_metadata(ticker):
	try:
		metadata = yf.Ticker(ticker)
	except:
		print('\033[91m' + 'Y Finance is not returning metadata for '+ ticker + '\033[0m')
		metadata = {}

	return metadata


