import logging
import streamlit as st


def add_page_dataframes(scope):
	logging.debug("add_page_dataframes")
	# Just the dataframes relevant for a particular page
	page = scope.display['page']

	selected_ticker = scope.page[page]['show']['ticker_file'].split("---")
	ticker = selected_ticker[0]

	col1,col2=st.columns([5,7])
	
	if ticker in scope.tickers.keys():
		with col1:add_page_df(scope, page, ticker, 'ticker_file')
		with col2:add_page_df(scope, page, ticker, 'with_added_columns')



def add_page_df(scope, page, ticker, type_df):
	logging.debug("add_page_df")
	if type_df == 'ticker_file':
		df = scope.tickers[ticker]['df']
		prefix='raw'

	if type_df == 'with_added_columns':
		df = scope.tickers[ticker][page]['df']
		prefix='added columns'

	logging.warning("maybe set the index to be the date range for better scrollability")
	no_of_rows = str(len(df))
	my_expander = st.expander(
		label=(
			ticker+ ' '+ prefix+' rows = ' + no_of_rows + ''), 
			expanded=True )
	my_expander.dataframe(df)	
