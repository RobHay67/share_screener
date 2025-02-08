import logging
import streamlit as st


def render_message_download(scope):
	logging.warning("render_message_download")
	col1,col2,col3,col4 = st.columns([5.5,1.5,1,4])

	yf_ticker_list = scope.yf['batch_ticker_string'].split(' ')
	no_of_tickers = len(yf_ticker_list)

	if scope.yf['batch_industry'] == 'random_tickers':
		batch_no = 'Manually Selected Tickers'		
	else:
		batch_no = (
					' ( batch ' + 
					str(scope.yf['batch_no']+1) + 
					' of ' + 
					str(len(scope.yf['download_these_industries'])) + 
					' )'
					)

