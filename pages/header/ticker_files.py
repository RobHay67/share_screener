# Function to show status of data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.
# - button to press to download more data

import streamlit as st

from pages.widgets.download import download_button
from y_finance.price_data.controller import download_tickers
from page.worklist import build_app_worklist_dropdown
from tickers.load import load_ticker


def ticker_files_layer(scope):

	page = scope.pages['display']

	if page in ['chart', 'intraday', 'volume', 'screener',  ]:
		
		col1,col2,col3 = st.columns([1.5, 9.0, 1.5])  #12.0

		with col1:st.caption('Ticker Files (loaded)')
		with col2:progress_bar_loading_tickers(scope, ) # loads ticker data as well
		with col3:download_ticker_data = download_button(scope)

		if download_ticker_data:
			download_tickers(scope)
			build_app_worklist_dropdown(scope)





def progress_bar_loading_tickers(scope):
	
	progress_bar_exists = False
	list_of_tickers_to_load = create_ticker_list_to_load(scope)

	if len(list_of_tickers_to_load) > 0:
		
		no_of_tickers = len(list_of_tickers_to_load)

		if progress_bar_exists==False:
			my_bar = st.progress(0)
			progress_bar_exists = True

		for counter, ticker in enumerate(list_of_tickers_to_load):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Loading ohlcv Ticker File ( '+str(counter)+' )  > '+ticker)
			load_ticker(scope, ticker)
	
	# we will have new information after the load so update
	# the dropdown list for the worklist
	build_app_worklist_dropdown(scope)

	no_loaded_tickers = str(len(scope.tickers.keys()))

	if progress_bar_exists==True:
		my_bar.progress(100, text='All files loaded ( '+no_loaded_tickers+' )')
	else:
		
		my_bar = st.progress(100, text='Already Loaded ( '+no_loaded_tickers+ ' ) tickers. No additional Files to Load')


def create_ticker_list_to_load(scope):

	page = scope.pages['display']
	already_loaded_list = list(scope.tickers.keys())

	list_of_tickers_to_load = []

	for ticker in scope.pages[page]['worklist']:
		if ticker not in scope.tickers_missing['local']:
			if ticker not in already_loaded_list:
				list_of_tickers_to_load.append(ticker)

	return list_of_tickers_to_load





