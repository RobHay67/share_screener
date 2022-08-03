

from apps.data.status import set_replace_df_status_for_ticker_and_page, set_replace_col_adder_status_for_ticker_and_page


# Replace the ticker_data for this app (where status = True)



def replace_dfs(scope):
	
	app 				= scope.apps['display_app']
	page_row_limit 		= int(scope.apps['row_limit'])
	page_ticker_list 	= scope.apps[app]['ticker_list']
	# config_group		= 'trials' if app == 'screener' else 'charts'
	loaded_tickers		= list(scope.data['ticker_files'].keys())

	for ticker in page_ticker_list:
		
		replace_ticker_df_status = scope.apps[app]['replace_dfs'][ticker]

		# Check if we have been requested to renew the ticker data for this ticker
		if  replace_ticker_df_status == True:

				# Check that there is share data available for this ticker
				# before attempting to copy that share date for use by this app
				# (function will fail if ticker data is not available) 

				if ticker in loaded_tickers: 
					# print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to app df where app = ' + app + '\033[0m')
					
					ticker_df = scope.data['ticker_files'][ticker].copy()
									
					# limit no of rows for the page_df (speeds up app rendering)
					if page_row_limit != None : 
						ticker_df = ticker_df.head(page_row_limit) 									
					
					# Store the ticker dataframe for use by the app
					scope.apps[app]['dfs'][ticker] = ticker_df

					# reset replace_df status to prevent unnecesary updates		
					set_replace_df_status_for_ticker_and_page(scope, app, ticker, new_status=False)

				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.data[ticker_files] \033[0m')


def replace_cols(scope):

		# Replace the columns required for this ticker / chart 

		app 				= scope.apps['display_app']
		page_ticker_list 	= scope.apps[app]['ticker_list']
		config_group		= 'trials' if app == 'screener' else 'charts'
		loaded_tickers		= list(scope.data['ticker_files'].keys())

		for ticker in page_ticker_list:

			column_adders = list(scope.apps[app]['replace_cols'][ticker].keys())
			tickers_already_loaded_for_page = list(scope.apps[app]['dfs'].keys())

			for col_adder in column_adders:			
				replace_cols_status = scope.apps[app]['replace_cols'][ticker][col_adder]
				
				if replace_cols_status:

					call_col_adder = scope.apps[app]['replace_cols'][ticker][col_adder]

					# Check if we have been requested to renew the columns for this ticker
					if call_col_adder == True:

						if ticker in tickers_already_loaded_for_page:
							ticker_df				= scope.apps[app]['dfs'][ticker]
							column_adder			= scope[config_group][col_adder]['add_columns']

							# Column_Adder has a column_adder function (some are set to None as nothing is required)
							if column_adder != None:
								column_adder_function = scope[config_group][col_adder]['add_columns']['function']
								
								# Call the column adding function for this col_adder
								scope[config_group][col_adder]['add_columns']['function'](scope, col_adder, ticker, ticker_df)
							
						# reset replace_cols status to prevent unnecesary updates		
						set_replace_col_adder_status_for_ticker_and_page(scope, app, ticker, col_adder, False)


