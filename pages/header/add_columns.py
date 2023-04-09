# Add and Replace Dataframes and columns within Page/page Dataframes
# - refresh the page df (completely)
# - Refresh specific df columns (activate or change col_adders)
# - utilised the scope.tickers object to track what needs to be done

import streamlit as st

from trials.verdict import determine_overall_ticker_verdict


def add_cols_to_df_layer(scope):

	page = scope.display_page

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
	completion_text = 'Finished adding columns to Ticker File(s)'

	my_bar = st.progress(0)

	if len(ticker_list) > 0:
		no_of_tickers = len(ticker_list)

		for counter, ticker in enumerate(ticker_list):
			poc = int(((counter+1) / no_of_tickers ) * 100)
			my_bar.progress(poc, text='Adding columns where file = '+ticker)
			replace_app_df(scope, page, ticker, app_row_limit)
			replace_specific_app_columns(scope, page, ticker)
			determine_overall_ticker_verdict(scope, ticker)

		my_bar.progress(100, text=completion_text)
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


def replace_app_df(scope, page, ticker, app_row_limit):
	# Replace the page df if requested

	if scope.tickers[ticker][page]['replace_df'] == True:
		ticker_df = scope.tickers[ticker]['df'].copy()
		# limit no of rows for the page df (speeds up page rendering)	
		ticker_df = ticker_df.head(app_row_limit)
		
		# Cache the ticker dataframe to be utilised by this page/page
		scope.tickers[ticker][page]['df'] = ticker_df

		if ticker not in scope.pages[page]['tickers_with_add_cols']:
		# add ticker to the loaded_ticker list
			scope.pages[page]['tickers_with_add_cols'].append(ticker)
		
		# Set the status to false to prevent refreshing unnecesarily
		scope.tickers[ticker][page]['replace_df'] = False


def replace_specific_app_columns(scope, page, ticker):

	type_of_column_adder = scope.tickers[ticker][page]['type_col_adder']
	scope.pages[page]['render']['verdicts'] = False
				
	if type_of_column_adder != None:			
	# Some apps/pages do not have any column adders
		for column_adder, status in scope.tickers[ticker][page]['column_adders'].items():
			if status == True:	
			# Only replace the columns if requested to do so for this column adder
				ticker_df = scope.tickers[ticker][page]['df']
				# Call the column adding function for this column_adder
				scope[type_of_column_adder][column_adder]['add_columns']['function'](scope, column_adder, ticker, ticker_df)
				# Set the status to false to prevent refreshing unnecesarily
				scope.tickers[ticker][page]['column_adders'][column_adder] = False

				if type_of_column_adder == 'trials':
					# set stutus to recalc overall verdict for this ticker
					scope.tickers[ticker][page]['replace_verdict'] = True
					# Store the most date recent test result - it should be the first row
					scope.tickers[ticker][page]['trials'][column_adder] = ticker_df[column_adder].iloc[0]














