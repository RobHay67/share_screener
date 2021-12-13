import streamlit as st


def ticker_file_button(scope, ticker_list):
	
	no_of_loaded_files 		= len(list(scope.ticker_data_files.keys()))
	total_loaded_rows		= 0	
	
	for ticker in ticker_list:
		if ticker in scope.ticker_data_files:
			loaded_df_row_count 	= int(len(scope.ticker_data_files[ticker]))
			total_loaded_rows 		+= loaded_df_row_count

	loaded_dfs_button_message 	= (str(no_of_loaded_files) + ' Loaded dfs - rows = ' + str(total_loaded_rows))

	return st.button(loaded_dfs_button_message)