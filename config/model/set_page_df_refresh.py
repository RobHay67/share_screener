import streamlit as st




def set_refresh_df_for_ticker_in_all_pages(scope, ticker, refresh_status):
	# This occurs when we have loaded some ticker data or downloaded some new ticker data
	# sometimes we failed to load so we tag the refres as False to prevent the code from trying when the data is missing
	for page in scope.pages.keys():
		scope.pages[page]['refresh_ticker_df'][ticker] = refresh_status


def set_refresh_df_all_tickers_in_all_pages():
	# This only needs to run when the user has changed the number of analysis rows - ie from 1000 to say 3000
	for page in st.session_state.pages:
		for ticker in st.session_state.pages[page]['refresh_ticker_df'].keys():
			st.session_state.pages[page]['refresh_ticker_df'][ticker] = True



def set_refresh_chart_dfs_for_non_screener_pages(scope):
	# One of the Chart Metrics has changed
	for page in scope.pages.keys():
		if page != 'screener':
			for ticker in scope.pages[page]['refresh_ticker_df'].keys():
				scope.pages[page]['refresh_ticker_df'][ticker] = True



def set_refresh_screener_dfs_for_screener_page(scope):
	# One of the Screener Metrics has changed 		TODO - not yet using this one
	for ticker in scope.pages['screener']['refresh_ticker_df'].keys():
		scope.pages['screener']['refresh_ticker_df'][ticker] = True

