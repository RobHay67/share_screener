import streamlit as st

from ticker.views.selectors import select_a_ticker
from ticker.loaders.controller import load_ticker_or_tickers
from ticker.downloader.controller import load_and_download_ticker_data
from analysis.model.analysis_df import establish_analysis_df
from ticker.views.ticker import view_a_ticker_file
from analysis.views.analysis_files import view_an_analysis_file

def single_loader(scope, page):
	col1,col2,col3,col4,col5,col6 = st.columns([2.0, 2.0, 1.5, 1.5, 2.0, 3.0])
	with col1: select_a_ticker(scope, page)

	ticker = scope.selected[page]['ticker_list'][0]
	
	if ticker != 'select a ticker':	
		download_button_msg = 'Download ' + str(int(scope.download_days)) + ' day'
		if scope.download_days > 1: download_button_msg += 's'

		with col4: load_tickers 	= st.button( 'Load This File')
		with col4: download_tickers = st.button(download_button_msg)
		with col6: st.button('Clear any messages')

		if load_tickers : 
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			load_ticker_or_tickers(scope, ticker)											

		if download_tickers:
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			load_and_download_ticker_data(scope)

		if ticker in list(scope.ticker_data_files.keys()):
			no_of_loaded_rows = int(len(scope.ticker_data_files[ticker]))
			establish_analysis_df(scope, ticker, no_of_loaded_rows)
			no_of_analysis_rows = len(scope.selected[scope.display_page]['analysis_df'][ticker])

			with col5: show_ticker_data = st.button(('Loaded Rows = ' + str(no_of_loaded_rows)))
			with col5: show_analysis_data = st.button(('Analysis Rows = ' + str(no_of_analysis_rows)))

			if show_ticker_data		: view_a_ticker_file(scope, ticker)
			if show_analysis_data	: view_an_analysis_file(scope)

			# Render the Company Name
			col1,col2,col3,col4 = st.columns([7.0, 1.7, 0.3, 3.0])
			with col1: st.header( scope.ticker_index.loc[ticker]['company_name'] )
			
















# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers for All Pages - Options and Buttons
# -------------------------------------------------------------------------------------------------------------------------------------------------------------


# def no_of_loaded_rows(scope, ticker):

# 	min_value,max_value,default_value,no_of_rows=0,0,0,0	

# 	# Count the rows in loaded dataframe
# 	if ticker in list(scope.ticker_data_files.keys()):
# 		min_value = 1
# 		no_of_rows = len(scope.ticker_data_files[ticker])
# 		max_value = no_of_rows if no_of_rows > 0 else 0
# 		default_value = 300 if max_value > 300 else max_value		
	
# 	return min_value,max_value,default_value,no_of_rows


