# Function to show status of data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.
# - button to press to download more data

import streamlit as st

from widgets.download import download_button
from tickers.download.controller import download_tickers
from apps.worklist import refresh_app_worklist_dropdown
from tickers.load import load_ticker


def ticker_files_layer(scope):

	app = scope.apps['display_app']

	if app in ['screener', 'chart', 'intraday']:
		
		col1,col2,col3 = st.columns([1.5, 9.0, 1.5])  #12.0

		with col1:st.caption('Ticker Files (loaded)')
		with col2:progress_bar_loading_tickers(scope, app) # loads ticker data as well
		with col3:download_ticker_data = download_button(scope)

		if download_ticker_data:
			download_tickers(scope)
			refresh_app_worklist_dropdown(scope)





def progress_bar_loading_tickers(scope, app):
	
	progress_bar_exists = False
	list_of_tickers_to_load = create_ticker_list_to_load(scope)

	if len(list_of_tickers_to_load) > 0:
		
		no_of_tickers = len(list_of_tickers_to_load)

		if progress_bar_exists==False:
			my_bar = st.progress(0)
			progress_bar_exists = True

		for counter, ticker in enumerate(list_of_tickers_to_load):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Loading ohlcv Ticker File = '+ticker)
			load_ticker(scope, ticker)
	
	# we will have new information after the load so update
	# the dropdown list for the worklist
	refresh_app_worklist_dropdown(scope)

	if progress_bar_exists==True:
		my_bar.progress(100, text='All files loaded')
	else:
		my_bar = st.progress(100, text='No Files to Load')


def create_ticker_list_to_load(scope):

	app = scope.apps['display_app']
	already_loaded_list = list(scope.tickers.keys())

	list_of_tickers_to_load = []

	for ticker in scope.apps[app]['worklist']:
		if ticker not in scope.missing_tickers['local']:
			if ticker not in already_loaded_list:
				list_of_tickers_to_load.append(ticker)

	return list_of_tickers_to_load





