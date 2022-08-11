
# The primary code to refresh the App df
# and the app df columns 



def refresh_app_df_and_columns(scope):

	app 				= scope.apps['display_app']
	app_row_limit 		= int(scope.apps['row_limit'])
	app_ticker_list 	= scope.apps[app]['selected_tickers']

	# Iterate through each ticker for the page

	for ticker in app_ticker_list:
		
		# Double Check if share data available for this ticker
		# (function will fail if ticker data is not available) 
		if ticker in list(scope.tickers.keys()): 
			
			# -------------------------------------------------------------------
			# Replace the App df if requested
			if scope.tickers[ticker]['apps'][app]['replace_df'] == True:
			
				ticker_df = scope.tickers[ticker]['df'].copy()

				# limit no of rows for the APP df (speeds up app rendering)
				ticker_df = ticker_df.head(app_row_limit) 									
				
				# Cache the ticker dataframe to be mined by this app
				scope.tickers[ticker]['apps'][app]['df'] = ticker_df

				# add ticker to the mined_ticker list
				if ticker not in scope.apps[app]['mined_tickers']:
					scope.apps[app]['mined_tickers'].append(ticker)
				
				# reset replace_app_dfs status to prevent unnecesary updates		
				scope.tickers[ticker]['apps'][app]['replace_df'] = False


			# Check if the app df columns require replacing

			type_of_column_adder = scope.tickers[ticker]['apps'][app]['type_col_adder']

			# Some apps do not have any column adder
			if type_of_column_adder != None:

				for column_adder, status in scope.tickers[ticker]['apps'][app]['column_adders'].items():
					
					# Only replace the columns if requested to do so for this column adder
					if status == True:
										
						# Call the column adding function for this column_adder
						scope[type_of_column_adder][column_adder]['add_columns']['function'](scope, column_adder, ticker, ticker_df)

						# Set the status to false to prevent refreshing unnecesarily
						scope.tickers[ticker]['apps'][app]['column_adders'][column_adder] = False
						
		else:
			print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope[ticker_files] \033[0m')

