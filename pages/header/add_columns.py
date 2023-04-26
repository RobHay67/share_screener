# Add and Replace Dataframes and columns within Page Dataframes
# - refresh the page df (completely)
# - Refresh specific df columns (activate or change col_adders settings)
# - utilised the scope.tickers object to track what needs to be done

import streamlit as st

from add_cols.replace_page_df import replace_page_df
from add_cols.replace_df_cols import replace_page_df_columns
from trials.verdict import determine_verdict_for_ticker


def add_cols_to_df_layer(scope):

	page = scope.pages['display']

	if page in ['chart','intraday','screener']:
		col1,col2,col3 = st.columns([1.5, 9.0, 1.5])  #12.0
		with col1:st.caption('Add Columns to Ticker Files')
		with col2:render_progress_bar(scope, page)      # will add/update the columns as well!


def render_progress_bar(scope, page):

	if len(scope.pages[page]['worklist']) == 0:
		st.write('No Files available - select some')
	else:
		replace_df_and_add_columns(scope, page)


def replace_df_and_add_columns(scope, page):

	ticker_list = create_ticker_list_to_add_columns(scope, page)
	app_row_limit = int(scope.pages['row_limit'])
	# completion_text = 

	my_bar = st.progress(0)

	if len(ticker_list) > 0:
		no_of_tickers = len(ticker_list)

		for counter, ticker in enumerate(ticker_list):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Adding columns where file = '+ticker)
			replace_page_df(scope, page, ticker, app_row_limit)
			replace_page_df_columns(scope, page, ticker)
			determine_verdict_for_ticker(scope, ticker)

		my_bar.progress(100, text='Finished adding columns to ( ' + str(len(ticker_list)) + ' ) ticker files')
	else:
		my_bar = st.progress(100, text='No Files available - cannot add columns')


def create_ticker_list_to_add_columns(scope, page):

	list_of_tickers_to_add_columns= []

	for ticker in scope.pages[page]['worklist']:
		# Ensure ticker data available otherwise
		# function will fail on missing columns
		if ticker in list(scope.tickers.keys()): 
			list_of_tickers_to_add_columns.append(ticker)

	return list_of_tickers_to_add_columns
















