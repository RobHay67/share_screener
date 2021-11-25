import streamlit as st


def download_button(scope):

	download_button_msg = 'Download most recent ' + str(int(scope.download_days)) + ' day'
	download_button_msg = 'Download ' + str(int(scope.download_days)) + ' most recent day'
	if scope.download_days > 1: download_button_msg += 's'

	return st.button(download_button_msg)

def clear_messages_button(scope):
	st.button('Clear any Messages')

def ticker_file_button(scope, ticker_list):
	
	no_of_loaded_files 		= len(list(scope.ticker_data_files.keys()))
	total_loaded_rows		= 0	
	
	for ticker in ticker_list:
		if ticker in scope.ticker_data_files:
			loaded_df_row_count 	= int(len(scope.ticker_data_files[ticker]))
			total_loaded_rows 		+= loaded_df_row_count

	loaded_dfs_button_message 	= ('Loaded dfs = ' + str(no_of_loaded_files) + ' rows = ' + str(total_loaded_rows))

	return st.button(loaded_dfs_button_message)

def analysis_dfs_button(scope, page, ticker_list):

	analysis_df_ticker_count = len(scope.pages[page]['analysis_df'])
	total_analysis_df_rows	 = 0

	for ticker in ticker_list:
		# if ticker in scope.ticker_data_files:
		if ticker in scope.pages[page]['analysis_df']:
			analysis_df_row_count 	= len(scope.pages[page]['analysis_df'][ticker])
			total_analysis_df_rows 	+= analysis_df_row_count

	analysis_dfs_button_message 	= ('Analysis dfs = ' + str(analysis_df_ticker_count)  	+ ' rows = ' + str(total_analysis_df_rows))

	return st.button(analysis_dfs_button_message)

def chart_dfs_button(scope, page, ticker_list):
	chart_df_ticker_count = len(scope.pages[page]['chart_df'])
	total_chart_df_rows	  = 0

	for ticker in ticker_list:
		if ticker in scope.ticker_data_files:
			chart_df_row_count 	 = len(scope.pages[page]['chart_df'][ticker])
			total_chart_df_rows += chart_df_row_count

	chart_dfs_button_message 	= ('Charting dfs = ' + str(chart_df_ticker_count)  		+ ' rows = ' + str(total_chart_df_rows))
	
	return st.button(chart_dfs_button_message)


