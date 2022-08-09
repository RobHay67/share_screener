import streamlit as st
import pandas as pd

def screener_dfs_button(scope):

	app 						= scope.apps['display_app']
	ticker_list 				= scope.apps[app]['selected_tickers']
	screener_df_ticker_count 	= count_loaded_screener_dfs(scope)
	total_screener_df_rows	 	= 0

	for ticker in ticker_list:
		screener_df_row_count	= len(scope.tickers[ticker]['apps']['screener']['df'])
		total_screener_df_rows 	+= screener_df_row_count

	analysis_dfs_button_message 	= (str(screener_df_ticker_count) + ' trial (' + str(total_screener_df_rows) + ' rows)')

	return st.button(analysis_dfs_button_message)



def count_loaded_screener_dfs(scope):
	counter=0

	for ticker in scope.tickers.keys():
		if isinstance(scope.tickers[ticker]['apps']['screener']['df'], pd.DataFrame):
			counter+=1

	return counter