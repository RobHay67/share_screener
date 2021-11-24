import streamlit as st

from ticker.views.selectors import select_a_market, select_industries, select_tickers
from scope.pages.ticker_list import update_multi_ticker_list
from ticker.controller import load_tickers
from ticker.controller import download_tickers
from ticker.views.df_status import dataframe_status


def multi_loader(scope):
	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 3.4, 0.1, 1.5, 2.0, 3.0])

	with col1: select_tickers(scope)

	with col2: select_industries(scope)
	with col2: select_a_market(scope)
	
	
	if scope.pages['multi']['market'] != 'select entire market' or (len(scope.pages['multi']['industries']) != 0) or len(scope.pages['multi']['tickers']) != 0:
		
		download_button_msg = 'Download ' + str(int(scope.download_days)) + ' day'
		if scope.download_days > 1: download_button_msg += 's'

		with col1: download_button = st.button(download_button_msg)
		with col6: st.button('Clear any Messages')
		
		update_multi_ticker_list(scope)									# scope.download_industries is establised by this function

		load_tickers(scope, col6,)										# AUTO load whatever ticker data we have	

		if download_button: download_tickers(scope)

		dataframe_status(scope, 'multi', col5, col6)





