
import streamlit as st


def render_available_dataframes(scope):

	page = scope.display_page

	selected_ticker = scope.pages[page]['render']['ticker_file'].split("---")
	ticker = selected_ticker[0]

	col1,col2=st.columns([4,8])

	if ticker in scope.tickers.keys():
		with col1:render_dataframe(scope, page, ticker, 'ticker_file')
		with col2:render_dataframe(scope, page, ticker, 'with_added_columns')



def render_dataframe(scope, page, ticker, type_df):

	if type_df == 'ticker_file':
		df = scope.tickers[ticker]['df']
		prefix='raw ticker file    >'

	if type_df == 'with_added_columns':
		df = scope.tickers[ticker][page]['df']
		prefix='with added columns >'

	# TODO - maybe set the index to be the date range for better scrollability

	no_of_rows = str(len(df))
	my_expander = st.expander(label=(prefix+ticker+' (' + no_of_rows + ')'), expanded=False )
	my_expander.dataframe(df, 2000, 2000)	

