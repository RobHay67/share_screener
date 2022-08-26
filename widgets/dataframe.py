
import streamlit as st


button_prefix = {
					'tickers':{'singular':' file (' , 'plural':' files (' , 'scope':'scope.tickers'},
					'charts' :{'singular':' chart (', 'plural':' charts ('},
					'trials' :{'singular':' trial (', 'plural':' trials ('},
				}



def dataframe_button(scope, type_df):
	
	app = scope.apps['display_app']
	dfs_total = 0
	rows_total = 0

	if type_df=='tickers':
		# How many tickers are available for the apps
		# this will be a count of the loaded (and download) files
		ticker_list = scope.tickers.keys()
		
		# Number of rows
		for ticker in ticker_list:
			df_row_count = int(len(scope.tickers[ticker]['df']))
			rows_total += df_row_count
		
	if type_df in ['charts', 'trials']:
		# This will be a count of the tickers that have been selcted
		# for this app for mining
		ticker_list = scope.apps[app]['mined_tickers']
		
		# Number of rows
		for ticker in scope.apps[app]['mined_tickers']:
			df_row_count = len(scope.tickers[ticker][app]['df'])
			rows_total += df_row_count

	# Number of Dataframes
	dfs_total 	= len(ticker_list)

	# Determine button message prefix
	dfs_description = button_prefix[type_df]['singular'] if dfs_total == 1 else button_prefix[type_df]['plural']

	# construct button message
	button_message 	= (str(dfs_total) + dfs_description + str(rows_total) + ' rows)')

	return st.button(button_message)