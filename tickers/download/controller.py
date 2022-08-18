from tickers.download.y_finance import download_from_yahoo_finance
from tickers.download.cache import combine_cached_and_yf_data

from tickers.save import save_tickers
from tickers.config import reset_yf_download_config

import streamlit as st

def download_tickers(scope):

	download_from_yahoo_finance(scope)

	combine_cached_and_yf_data(scope)

	save_tickers(scope)

	print('Rob - we are playing with various process end output - i think we only need to report the erros')
	failed_download_list = []
	for ticker, error in scope.download['yf_errors'].items():
		failed_download_list.append(ticker)

	for ticker in scope.download['yf_ticker_list']:
		with scope.col5:
			if ticker not in failed_download_list:
				st.success(ticker)
			else:
				st.error(ticker)

	reset_yf_download_config(scope)






def report_on_download_errors(scope):

	# TODO - not sure this belongs at this point

	# The following seems to report on the download errors

	cache_progress( scope, 
					passed='Downloaded > ', 
					passed_2='na', 
					failed='Falied to Download > ' 
					)
	
	failed_download_list = []
	for ticker, error in scope.download['yf_errors'].items():
		failed_download_list.append(ticker)

	for ticker in scope.download['yf_ticker_list']:
		if ticker not in failed_download_list:
			cache_progress( scope, ticker, result='passed' )
		else:
			cache_progress( scope, ticker, result='failed' )
	
	cache_progress(scope, 'Finished', final_print=True )