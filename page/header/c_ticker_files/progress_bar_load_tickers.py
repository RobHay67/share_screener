import logging
import streamlit as st
from tickers.model.load import load_ticker
from add_cols.model.replace_page_df import replace_page_df
from tickers.helpers.ticker_list import create_ticker_list_to_load


def progress_bar_load_tickers(scope):
	logging.info("progress_bar_load_tickers")
	page = scope.display['page']
	ticker_load_list = scope.page[page]['list_load_tickers']
	
	number_to_load = len(ticker_load_list)
	status_just_loaded_tickers = False
	app_row_limit = int(scope.config['row_limit'])
	
	if number_to_load > 0:
		# Show the progress bar - ONLY if we have tickers to load
		my_bar = st.progress(0)
		status_just_loaded_tickers = True
		load_counter=0
			
		for ticker in ticker_load_list:
			load_counter+=1
			poc = int(((load_counter) / number_to_load ) * 100)
			my_bar.progress(poc, text='Loading > '+ticker)
			load_ticker(scope, ticker)
			if ticker not in scope.ticker_schema['missing']['local']:
				replace_page_df(scope, page, ticker, app_row_limit)
	
	# Report (tickers just loaded) (or nothing to do)
	load_total = str(len(scope.tickers.keys()))
	page_total = str(len(scope.page[page]['list_loaded_tickers']))

	if status_just_loaded_tickers == True:
		my_bar.empty()
		st.write(':green[Loaded '+str(load_counter)+' ticker(s)]')
	else:
		st.write(':blue[Total Loaded = '+load_total+' | Loaded for Page = '+page_total+']')