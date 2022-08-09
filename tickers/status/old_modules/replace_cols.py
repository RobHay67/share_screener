


# TODO delete this module as replaced by refresh_app_df_and_columns


def replace_cols(scope):

		# Replace the columns required for this ticker / chart 

		app 				= scope.apps['display_app']
		app_ticker_list 	= scope.apps[app]['ticker_list']
		config_group		= 'trials' if app == 'screener' else 'charts'
		loaded_tickers		= list(scope.tickers.keys())

		for ticker in app_ticker_list:

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



# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE TICKER and a SINGLE app
# -------------------------------------------------------------




def set_replace_col_adder_status_for_ticker_and_page(scope, app, ticker, col_adder, new_status):
	scope.apps[app]['replace_cols'][ticker][col_adder] = new_status

	# TODO - delete this later - just for making sure we are not doing unnecesary updates
	print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
	print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(80) + str(print_status) )


