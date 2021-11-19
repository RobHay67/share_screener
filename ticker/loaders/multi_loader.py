import streamlit as st

from ticker.views.selectors import select_a_market, select_industries, select_tickers
from scope.pages.ticker_list import update_multi_ticker_list
from ticker.loaders.controller import load_ticker_or_tickers
from ticker.downloader.controller import load_and_download_ticker_data
from analysis.analysis_df import establish_analysis_df
from ticker.views.all_tickers import view_all_loaded_ticker_files
from analysis.views.analysis_files import view_all_analysis_files



def multi_loader(scope):
	
	col1,col2,col3,col4,col5,col6 = st.columns([2,3,2,1.2,2,1.8])

	with col1: select_a_market(scope)
	with col2: select_industries(scope)
	with col3: select_tickers(scope)
	
	if scope.selected['multi']['market'] != 'select entire market' or (len(scope.selected['multi']['industries']) != 0) or len(scope.selected['multi']['tickers']) != 0:
		total_loaded_rows, total_analysis_rows = 0, 0
		
		download_button_msg = 'Download ' + str(int(scope.download_days)) + ' day'
		if scope.download_days > 1: download_button_msg += 's'

		with col4: load_tickers 	= st.button( 'Load These Files')
		with col4: download_tickers = st.button(download_button_msg)
		with col6: st.button('Clear any Messages')

		update_multi_ticker_list(scope)

		if load_tickers : 
			# scope.download_industries is establised by the update_multi_ticker_list() function
			load_ticker_or_tickers(scope)

		if download_tickers:
			# scope.download_industries is establised by the update_multi_ticker_list() function
			load_and_download_ticker_data(scope)

		# iterate through loaded ticker list and call the establish_analysis_df method 
		list_of_loaded_files = list(scope.ticker_data_files.keys())
		no_of_loaded_files = len(list_of_loaded_files)

		for ticker in list_of_loaded_files:
			no_of_loaded_rows = len(scope.ticker_data_files[ticker])
			establish_analysis_df(scope, ticker, no_of_loaded_rows)

			no_of_analysis_rows = len(scope.selected['multi']['analysis_df'][ticker])

			total_loaded_rows += no_of_loaded_rows
			total_analysis_rows += no_of_analysis_rows

		no_of_analysis_files = len(scope.selected['multi']['analysis_df'])

		with col5: show_ticker_files   = st.button(('Loaded Files   = ' + str(no_of_loaded_files)   + ' rows = ' + str(total_loaded_rows)))
		with col5: show_analysis_files = st.button(('Analysis Files = ' + str(no_of_analysis_files) + ' rows = ' + str(total_analysis_rows)))


		if show_ticker_files:
			view_all_loaded_ticker_files(scope)

		if show_analysis_files:
			view_all_analysis_files(scope)




