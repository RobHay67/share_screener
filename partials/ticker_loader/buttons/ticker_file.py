import streamlit as st


def ticker_files_button(scope):
	
	# How many tickers are available for the apps
	# this will be a count of the loaded (and download) files
	
	no_of_loaded_files 	= len(scope.tickers.keys())
	total_loaded_rows	= 0	
	
	for ticker in scope.tickers.keys():
		loaded_df_row_count = int(len(scope.tickers[ticker]['df']))
		total_loaded_rows += loaded_df_row_count

	file_desc = ' file (' if no_of_loaded_files == 1 else ' files ('

	loaded_dfs_button_message 	= (str(no_of_loaded_files) + file_desc + str(total_loaded_rows) + ' rows)')

	return st.button(loaded_dfs_button_message)