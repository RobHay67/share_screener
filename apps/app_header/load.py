import streamlit as st
import os

from files.path import path_for_ticker_file
from tickers.load import load_ticker
from tickers.cache import cache_ticker_data
from tickers.events.missing_local_file import missing_file_event
from tickers.events.add_ticker import add_ticker_event


# ==============================================================
# Load ticker controller here so we can render a progress bar
# on this function which can be time consuming
# ==============================================================

def load_tickers(scope):
	app = scope.apps['display_app']
	worklist = scope.apps[app]['worklist']
	no_of_tickers = len(worklist)
	already_loaded_list = list(scope.tickers.keys())
	added_progress_bar = False

	for counter, ticker in enumerate(worklist):
		if ticker not in scope.missing_tickers['local']:
			if ticker not in already_loaded_list:
				# Add a Progress Bar for user process feedback
				if added_progress_bar==False:
					col1,col2,col3 = st.columns([1,11,2])
					with col1:
						st.write('Loading Tickers')
					with col2:
						my_bar = st.progress(0)
						added_progress_bar = True
					with col3:
						st.write('dataframes here')
				poc = int(((counter+1) / no_of_tickers ) * 100)
				my_bar.progress(poc, text='Loading Ticker Data')

				path_for_ticker_file(scope, ticker )
				# Check that a local file is available to load
				if os.path.exists( scope.files['paths']['ticker_data'] ):
					ticker_data = load_ticker(scope, ticker )
					add_ticker_event(scope, ticker)
					cache_ticker_data(scope, ticker, ticker_data)
				else:
					# The expected Local file is not available
					missing_file_event(scope, ticker)		

	if counter+1 == no_of_tickers:
		if added_progress_bar == True:
			my_bar.progress(100, text='Finished Loading Ticker Data')

