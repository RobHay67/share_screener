import streamlit as st


def ticker_files_button(scope):

	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['ticker_list']

	no_of_loaded_files 	= len(list(scope.data['ticker_files'].keys()))
	total_loaded_rows	= 0	
	
	for ticker in ticker_list:
		if ticker in scope.data['ticker_files']:
			loaded_df_row_count = int(len(scope.data['ticker_files'][ticker]))
			total_loaded_rows 	+= loaded_df_row_count

	file_desc = ' file (' if no_of_loaded_files == 1 else ' files ('

	loaded_dfs_button_message 	= (str(no_of_loaded_files) + file_desc + str(total_loaded_rows) + ' rows)')

	return st.button(loaded_dfs_button_message)