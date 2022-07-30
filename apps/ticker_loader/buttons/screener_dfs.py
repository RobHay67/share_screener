import streamlit as st


def screener_dfs_button(scope):

	app 						= ['display_app']
	ticker_list 				= scope.apps[app]['ticker_list']
	screener_df_ticker_count 	= len(scope.apps[app]['dfs'])
	total_screener_df_rows	 	= 0

	for ticker in ticker_list:
		# if ticker in scope.data['ticker_files']:
		if ticker in scope.apps[app]['dfs']:
			screener_df_row_count 	= len(scope.apps[app]['dfs'][ticker])
			total_screener_df_rows 	+= screener_df_row_count

	analysis_dfs_button_message 	= (str(screener_df_ticker_count) + ' test (' + str(total_screener_df_rows) + ' rows)')

	return st.button(analysis_dfs_button_message)