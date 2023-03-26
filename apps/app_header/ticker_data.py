# Function to show status of data
# - progress bar while loading files (as can be time consuming)
# - status once all files are loaded
# - status if there is nothing too load.

import streamlit as st

from tickers.load import load_ticker
from tickers.download.controller import download_tickers
from widgets.worklist import render_worklist, render_errors
from widgets.dataframes import dataframe_dropdown_list
from widgets.dataframes import reset_page_render
from widgets.download import download_button


def ticker_data_title(scope):
	button = st.button(
						label='Loaded Ticker Files ohlcv', 
						use_container_width=True, 
						disabled=True,
						key='ticker_data_title'
						)
	return button


def render_ticker_files(scope):

	app = scope.apps['display_app']

	if app in ['screener', 'chart', 'intraday']:
		
		col1,col2,col3,col4,col5 = st.columns([1.5, 5.0, 2.0, 2.0, 1.5])  #12.5

		with col1:ticker_data_title(scope)
		with col2:render_ticker_load_progress_bar(scope) # loads ticker data as well
		with col3:render_errors(scope)
		with col4:dataframe_dropdown_list(scope)
		with col5:download_ticker_data = download_button(scope)

		if download_ticker_data:download_tickers(scope)


def render_ticker_load_progress_bar(scope):
	
	progress_bar_exists = False
	list_of_tickers_to_load = ticker_list_to_load(scope)

	if len(list_of_tickers_to_load) > 0:
		
		no_of_tickers = len(list_of_tickers_to_load)

		if progress_bar_exists==False:
			my_bar = st.progress(0)
			progress_bar_exists = True

		for counter, ticker in enumerate(list_of_tickers_to_load):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Loading ohlcv Ticker Files')
			load_ticker(scope, ticker)
	
	if progress_bar_exists==True:
		my_bar.progress(100, text='All files loaded')
	else:
		my_bar = st.progress(100, text='No Files to Load')


def ticker_list_to_load(scope):

	app = scope.apps['display_app']
	already_loaded_list = list(scope.tickers.keys())

	list_of_tickers_to_load = []

	for ticker in scope.apps[app]['worklist']:
		if ticker not in scope.missing_tickers['local']:
			if ticker not in already_loaded_list:
				list_of_tickers_to_load.append(ticker)

	return list_of_tickers_to_load







# def render_page_data(scope):
# 	# Render Data Status - whats loaded - what has load or download errors

# 	app = scope.apps['display_app']

# 	if app in ['screener', 'chart', 'intraday']:
		
# 		col1,col2,col3,col4,col5,col6 = st.columns([1.0, 2.5, 2.5, 2.0, 2.0, 2.0])
		
# 		with col1:
# 			st.write('Page Data :')
# 		with col2:
# 			render_worklist(scope)
# 		with col3:
# 			render_errors(scope)
# 		with col4:
# 			dataframe_dropdown_list(scope, 'tickers')
# 		with col5:
# 			if app == 'screener':
# 				dataframe_dropdown_list(scope, 'trials')
# 			if app == 'chart':
# 				dataframe_dropdown_list(scope, 'charts')		
# 		with col6:
# 			reset_page_render(scope)