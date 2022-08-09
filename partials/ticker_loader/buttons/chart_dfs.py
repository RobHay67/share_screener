import streamlit as st




def chart_dfs_button(scope):
	
	app 					= scope.apps['display_app']
	ticker_list 			= scope.apps[app]['selected_tickers']
	chart_df_ticker_count	= len(scope.apps[app]['dfs'])
	total_chart_df_rows	  	= 0

	for ticker in ticker_list:
		if ticker in scope.apps[app]['dfs']: 
			chart_df_row_count 	 = len(scope.apps[app]['dfs'][ticker])
			total_chart_df_rows += chart_df_row_count

	chart_dfs_button_message 	= (str(chart_df_ticker_count) + ' chart (' + str(total_chart_df_rows) + ' rows)')
	
	return st.button(chart_dfs_button_message)


