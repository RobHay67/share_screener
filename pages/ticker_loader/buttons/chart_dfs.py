import streamlit as st




def chart_dfs_button(scope):
	
	page 					= scope.pages['display_page']
	ticker_list 			= scope.pages[page]['ticker_list']
	chart_df_ticker_count	= len(scope.pages[page]['dfs'])
	total_chart_df_rows	  	= 0

	for ticker in ticker_list:
		if ticker in scope.pages[page]['dfs']: 
		# if ticker in scope.data['ticker_files']:
			chart_df_row_count 	 = len(scope.pages[page]['dfs'][ticker])
			total_chart_df_rows += chart_df_row_count

	chart_dfs_button_message 	= (str(chart_df_ticker_count) + ' Charting dfs - rows = ' + str(total_chart_df_rows))
	
	return st.button(chart_dfs_button_message)


