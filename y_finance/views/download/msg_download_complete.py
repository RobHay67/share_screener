import streamlit as st
import pandas as pd


def render_message_download_complete(scope, ticker_download_list):
	yf_download = scope.yf['data']
	no_in_worklist = len(ticker_download_list)

	print(yf_download)

	if yf_download.empty:
		no_of_rows = 0
		no_of_tickers_downloaded = 0
	else:
		no_of_rows = len(yf_download)
		no_of_tickers_downloaded = len(pd.unique(yf_download['ticker']))

	st.toast("Number of Tickers in Worklist  = "+str(no_in_worklist))
	st.toast("Number of Tickers Download     = "+str(no_of_tickers_downloaded))
	st.toast("Number of Rows in the Download = "+str(no_of_rows))
	st.toast('Download Complete', icon='🏆')


