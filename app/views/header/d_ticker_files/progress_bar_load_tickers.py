import streamlit as st
from tickers.model.load import load_ticker
from tickers.helpers.ticker_list import create_ticker_list_to_load


def load_tickers_progress_bar(scope):
	status_loaded_tickers = False
	ticker_list = create_ticker_list_to_load(scope)
	number_to_load = len(ticker_list)

	if number_to_load > 0:
		if status_loaded_tickers==False:
			my_bar = st.progress(0)
			status_loaded_tickers = True

		for counter, ticker in enumerate(ticker_list):
			poc = int(((counter+1) / number_to_load ) * 100)
			my_bar.progress(poc, text='Loading ohlcv Ticker File ( '+str(counter)+' )  > '+ticker)
			load_ticker(scope, ticker)
	

	# What to show after we have loaded or not loaded anything
	total_loaded = str(len(scope.tickers.keys()))
	# TODO - count for the page only - how do we do this???

	if status_loaded_tickers:
		success_string = ':blue[Just Finished Loading ( '+str(counter)+' ) ticker files. Total Loaded = ('+total_loaded+')]'
		my_bar.progress(100, text=success_string)
	else:
		st.write(':green[('+total_loaded+') Files previously loaded. Total Loaded = ('+total_loaded+')]')