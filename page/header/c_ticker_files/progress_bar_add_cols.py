import logging
import streamlit as st

from add_cols.model.replace_df_cols import replace_page_df_columns
from trials.helpers.re_run_verdicts import determine_verdict_for_ticker


def progress_bar_add_columns(scope, page):
	logging.info("progress_bar_add_columns")

	# List of tickers that require extra columns
	list_of_tickers_to_add_columns = []
	for ticker in scope.page[page]['list_selected_tickers']:
		# Ensure ticker data available otherwise function will fail on missing columns
		# if ticker in list(scope.tickers.keys()):
		if ticker in scope.page[page]['list_loaded_tickers']:
			status_add_ticker = False
			if scope.tickers[ticker][page]['replace_df']:status_add_ticker = True
			if True in scope.tickers[ticker][page]['re_run_functions'].values():status_add_ticker = True
			if status_add_ticker:list_of_tickers_to_add_columns.append(ticker)
	number_to_add_columns = len(list_of_tickers_to_add_columns)
	
	status_just_added_columns = False
	if number_to_add_columns > 0:
		my_bar = st.progress(0)
		status_just_added_columns = True
		add_cols_counter=0

		for ticker in list_of_tickers_to_add_columns:
			add_cols_counter+=1
			poc = int(((add_cols_counter) / number_to_add_columns ) * 100)
			my_bar.progress(poc, text='Adding columns to > '+ticker)
			
			replace_page_df_columns(scope, page, ticker)
			determine_verdict_for_ticker(scope, ticker)
	
	# Report (columns just added) (or nothing to do)
	load_total = str(len(scope.tickers.keys()))
	page_total = str(len(scope.page[page]['list_loaded_tickers']))

	if status_just_added_columns:
		my_bar.empty()
		st.write(':green[Added Columns to '+str(load_total)+' ticker(s)]')
	else:
		st.write(':blue[Total Added Columns Tickers = '+load_total+' | Loaded for Page = '+page_total+']')
