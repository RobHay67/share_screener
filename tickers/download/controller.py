from tickers.download.y_finance import download_from_yahoo_finance
from tickers.download.cache import combine_cached_and_yf_data

from tickers.download.config import reset_yf_download_config

import streamlit as st

def download_tickers(scope):

	download_from_yahoo_finance(scope)

	combine_cached_and_yf_data(scope)

	print('ToDO - we might want to clear the download cache before each run - not after as we havnt reported yet')
	reset_yf_download_config(scope)





