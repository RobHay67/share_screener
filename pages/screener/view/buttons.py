import streamlit as st


def execute_screening_button(scope):

	# screener_df_ticker_count = len(scope.pages[page]['df'])
	# total_analysis_df_rows	 = 0

	# for ticker in ticker_list:
	# 	# if ticker in scope.data['ticker_files']:
	# 	if ticker in scope.pages[page]['df']:
	# 		analysis_df_row_count 	= len(scope.pages[page]['df'][ticker])
	# 		total_analysis_df_rows 	+= analysis_df_row_count

	# analysis_dfs_button_message 	= ('Analysis dfs = ' + str(screener_df_ticker_count)  	+ ' rows = ' + str(total_analysis_df_rows))

	return st.button('Determine Tickers meeting the above Criteria', key='75')