import streamlit as st


def screener_dfs_button(scope, page, ticker_list):

	screener_df_ticker_count = len(scope.pages[page]['screener_df'])
	total_screener_df_rows	 = 0

	for ticker in ticker_list:
		# if ticker in scope.ticker_data_files:
		if ticker in scope.pages[page]['screener_df']:
			screener_df_row_count 	= len(scope.pages[page]['screener_df'][ticker])
			total_screener_df_rows 	+= screener_df_row_count

	analysis_dfs_button_message 	= (str(screener_df_ticker_count) + 'Screener dfs - rows = ' + str(total_screener_df_rows))

	return st.button(analysis_dfs_button_message)