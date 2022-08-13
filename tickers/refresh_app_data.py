


# The primary code to 
# - refresh the App df
# - Refresh specific df columns 



def refresh_app_df_and_columns(scope):

	app 				= scope.apps['display_app']
	app_row_limit 		= int(scope.apps['row_limit'])
	app_ticker_list 	= scope.apps[app]['selected_tickers']

	for ticker in app_ticker_list:
		
		# Double Check if share data available for this ticker
		# (function will fail if ticker data is not available) 
		if ticker in list(scope.tickers.keys()): 
			
			# -------------------------------------------------------------------
			# Replace the App df if requested
			if scope.tickers[ticker]['apps'][app]['replace_df'] == True:
			
				ticker_df = scope.tickers[ticker]['df'].copy()

				ticker_df = ticker_df.head(app_row_limit) 	# limit no of rows for the APP df (speeds up app rendering)				
				
				scope.tickers[ticker]['apps'][app]['df'] = ticker_df	# Cache the ticker dataframe to be mined by this app

				# add ticker to the mined_ticker list
				if ticker not in scope.apps[app]['mined_tickers']:
					scope.apps[app]['mined_tickers'].append(ticker)
				
				# Set the status to false to prevent refreshing unnecesarily	
				scope.tickers[ticker]['apps'][app]['replace_df'] = False

			# -------------------------------------------------------------------
			# Replace specific columns in the app df if requested
			type_of_column_adder = scope.tickers[ticker]['apps'][app]['type_col_adder']

			
			if type_of_column_adder != None:			# Some apps do not have any column adder

				for column_adder, status in scope.tickers[ticker]['apps'][app]['column_adders'].items():
					
					if status == True:	# Only replace the columns if requested to do so for this column adder
										
						# Call the column adding function for this column_adder
						scope[type_of_column_adder][column_adder]['add_columns']['function'](scope, column_adder, ticker, ticker_df)

						# Set the status to false to prevent refreshing unnecesarily
						scope.tickers[ticker]['apps'][app]['column_adders'][column_adder] = False
						
		else:
			print ( '\033[91m' + ticker.ljust(10) + '> ticker file not in scope.tickers \033[0m')

