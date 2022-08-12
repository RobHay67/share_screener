
import streamlit as st


def screener_dfs_button(scope):

	# This will be a count of the tickers that have been selcted
	# for this app for mining

	app 						= scope.apps['display_app']
	ticker_list 				= scope.apps[app]['mined_tickers']
	screener_df_ticker_count 	= len(ticker_list)
	total_screener_df_rows	 	= 0

	for ticker in ticker_list:
		screener_df_row_count	= len(scope.tickers[ticker]['apps'][app]['df'])
		total_screener_df_rows 	+= screener_df_row_count

	analysis_dfs_button_message 	= (str(screener_df_ticker_count) + ' trial (' + str(total_screener_df_rows) + ' rows)')

	return st.button(analysis_dfs_button_message)

