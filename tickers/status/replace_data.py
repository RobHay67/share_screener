
# The primary code to refresh the App df
# and the app df columns 



def replace_app_df_and_columns(scope):

	app 				= scope.apps['display_app']
	app_row_limit 		= int(scope.apps['row_limit'])
	app_ticker_list 	= scope.apps[app]['ticker_list']
	loaded_tickers		= list(scope.tickers.keys())

	print(loaded_tickers)

	print('&'*99)

	for ticker in app_ticker_list:

		# Double Check if share data available for this ticker
		# (function will fail if ticker data is not available) 

		if ticker in loaded_tickers: 

			# Check if the app df require replacing
			if scope.tickers[ticker]['apps'][app]['replace_df'] == True:
			
				ticker_df = scope.tickers[ticker]['df'].copy()

				# limit no of rows for the APP df (speeds up app rendering)
				ticker_df = ticker_df.head(app_row_limit) 									
				
				# Store the ticker dataframe for use by the app
				scope.tickers[ticker]['apps'][app]['df'] = ticker_df
				
				# reset replace_app_dfs status to prevent unnecesary updates		
				scope.tickers[ticker]['apps'][app]['replace_df'] = False


			# Check if the app df columns require replacing

			type_of_column_adder = scope.tickers[ticker]['apps'][app]['type_col_adder']

			if type_of_column_adder != None:
				for column_adder, status in scope.tickers[ticker]['apps'][app]['column_adders'].items():
					if status == True:
						print('col_adder = ', column_adder, status)

						# shortcut to the column adding function
						column_add_function = scope[type_of_column_adder][column_adder]['add_columns']['function']
						
						# Call the column adding function for this col_adder
						column_add_function(scope, column_adder, ticker, ticker_df)

						# Set the status to false to prevent refreshing unnecesarily
						scope.tickers[ticker]['apps'][app]['column_adders'][column_adder] = False
						
		else:
			print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope[ticker_files] \033[0m')




	print('&'*99)



