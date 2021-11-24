import streamlit as st

from ticker.views.selectors import select_a_ticker
from ticker.controller import load_tickers, download_tickers
from ticker.views.df_status import dataframe_status


def single_loader(scope, page):
	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	with col1: select_a_ticker(scope, page)

	ticker = scope.pages[page]['ticker_list'][0]
	
	if ticker != 'select a ticker':	

		download_button_msg = 'Download most recent ' + str(int(scope.download_days)) + ' day'
		if scope.download_days > 1: download_button_msg += 's'

		with col1: download_button = st.button(download_button_msg)
		with col6: st.button('Clear any Messages')

		scope.download_industries = ['random_tickers']									# used for y_finance downloading
		
		load_tickers(scope, col6, ticker)												# load whatever ticker data we have				

		if download_button: download_tickers(scope)
			

		# ----------------------------------------------
		# Report Loaded File Status
		# ----------------------------------------------
		dataframe_status(scope, page, col5, col6)








