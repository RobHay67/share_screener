import streamlit as st
from tickers.model.load import load_ticker
from tickers.helpers.ticker_list import create_ticker_list_to_load
from tickers.helpers.count_page_tickers import count_page_tickers


def progress_bar_for_loading_tickers(scope):
	ticker_list = create_ticker_list_to_load(scope)
	number_to_load = len(ticker_list)
	status_just_loaded_tickers = False
	if number_to_load > 0:
		# Show the progress bar - ONLY if we have tickers to load
		my_bar = st.progress(0)
		status_just_loaded_tickers = True
		load_counter=0
			
		for ticker in ticker_list:
			load_counter+=1
			poc = int(((load_counter) / number_to_load ) * 100)
			my_bar.progress(poc, text='Loading > '+ticker)
			load_ticker(scope, ticker)
	
	# Report (tickers just loaded) (or nothing to do)
	load_total = str(len(scope.tickers.keys()))
	page_total = str(count_page_tickers(scope))
	if status_just_loaded_tickers == True:
		my_bar.empty()
		st.write(':green[Loaded '+str(load_counter)+' ticker(s)]')
	else:
		st.write(':blue[Total Loaded = '+load_total+' | Loaded for Page = '+page_total+']')