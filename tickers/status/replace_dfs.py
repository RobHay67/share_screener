




def replace_dfs(scope):
	
	app 				= scope.apps['display_app']
	page_row_limit 		= int(scope.apps['row_limit'])
	page_ticker_list 	= scope.apps[app]['ticker_list']
	# config_group		= 'trials' if app == 'screener' else 'charts'
	loaded_tickers		= list(scope.ticker_files.keys())

	for ticker in page_ticker_list:
		
		replace_ticker_df_status = scope.apps[app]['replace_dfs'][ticker]

		# Check if we have been requested to renew the ticker data for this ticker
		if  replace_ticker_df_status == True:

				# Check that there is share data available for this ticker
				# before attempting to copy that share date for use by this app
				# (function will fail if ticker data is not available) 

				if ticker in loaded_tickers: 
					# print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to app df where app = ' + app + '\033[0m')
					
					ticker_df = scope.ticker_files[ticker].copy()
									
					# limit no of rows for the page_df (speeds up app rendering)
					if page_row_limit != None : 
						ticker_df = ticker_df.head(page_row_limit) 									
					
					# Store the ticker dataframe for use by the app
					scope.apps[app]['dfs'][ticker] = ticker_df

					# reset replace_df status to prevent unnecesary updates		
					set_replace_df_status_for_ticker_and_page(scope, app, ticker, new_status=False)

				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope[ticker_files] \033[0m')


# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE TICKER and a SINGLE app
# -------------------------------------------------------------

def set_replace_df_status_for_ticker_and_page(scope, app, ticker, new_status=False):
	scope.apps[app]['replace_dfs'][ticker] = new_status
	
	# TODO - delete this later - just for making sure we are not doing unnecesary updates
	print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
	print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(print_status) )



