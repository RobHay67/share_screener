import streamlit as st




def chart_dfs_button(scope):
	
	# This will be a count of the tickers that have been selcted
	# for this app for mining


	app 					= scope.apps['display_app']
	# ticker_list 			= scope.apps[app]['selected_tickers']
	ticker_list 			= scope.apps[app]['mined_tickers']
	# chart_df_ticker_count	= len(scope.apps[app]['dfs'])
	chart_df_ticker_count	= len(ticker_list)
	total_chart_df_rows	  	= 0

	for ticker in ticker_list:
		chart_df_row_count	= len(scope.tickers[ticker]['apps'][app]['df'])
		# if ticker in scope.apps[app]['dfs']: 
		# chart_df_row_count 	 = len(scope.apps[app]['dfs'][ticker])
		total_chart_df_rows += chart_df_row_count

	chart_dfs_button_message 	= (str(chart_df_ticker_count) + ' chart (' + str(total_chart_df_rows) + ' rows)')
	
	return st.button(chart_dfs_button_message)


