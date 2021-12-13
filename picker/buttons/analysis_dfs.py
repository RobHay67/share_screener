import streamlit as st


def screener_dfs_button(scope, page, ticker_list):

	screener_df_ticker_count = len(scope.pages[page]['screener_df'])
	total_analysis_df_rows	 = 0

	for ticker in ticker_list:
		# if ticker in scope.ticker_data_files:
		if ticker in scope.pages[page]['screener_df']:
			analysis_df_row_count 	= len(scope.pages[page]['screener_df'][ticker])
			total_analysis_df_rows 	+= analysis_df_row_count

	analysis_dfs_button_message 	= ('Analysis dfs = ' + str(screener_df_ticker_count)  	+ ' rows = ' + str(total_analysis_df_rows))

	return st.button(analysis_dfs_button_message)