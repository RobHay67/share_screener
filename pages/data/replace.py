

from pages.data.status import set_replace_df_status_for_ticker_and_page, set_replace_col_adder_status_for_ticker_and_page


# Replace the ticker_data for this page (where status = True)



def replace_dfs(scope):
	
	page 				= scope.pages['display_page']
	page_row_limit 		= int(scope.pages['row_limit'])
	page_ticker_list 	= scope.pages[page]['ticker_list']
	# config_group		= 'tests' if page == 'screener' else 'charts'
	loaded_tickers		= list(scope.data['ticker_files'].keys())

	for ticker in page_ticker_list:
		
		replace_ticker_df_status = scope.pages[page]['replace_dfs'][ticker]

		# Check if we have been requested to renew the ticker data for this ticker
		if  replace_ticker_df_status == True:

				# Check that there is share data available for this ticker
				# before attempting to copy that share date for use by this page
				# (function will fail if ticker data is not available) 

				if ticker in loaded_tickers: 
					# print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to page df where page = ' + page + '\033[0m')
					
					ticker_df = scope.data['ticker_files'][ticker].copy()
					
					# sort the df into the correct order for the charting
					ticker_df.sort_values(by=['date'], inplace=True, ascending=True)
					
					# limit no of rows for the page_df (speeds up page rendering)
					if page_row_limit != None : 
						ticker_df = ticker_df.tail(page_row_limit) 									
					
					# Store the ticker dataframe for use by the page
					scope.pages[page]['dfs'][ticker] = ticker_df

					# reset replace_df status to prevent unnecesary updates		
					# set_replace_df_status_for_ticker(scope, ticker, new_status=False, caller='replace_dfs')
					set_replace_df_status_for_ticker_and_page(scope, page, ticker, new_status=False, caller='replace_dfs')

				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.data[ticker_files] \033[0m')


def replace_cols(scope):

		# Replace the columns required for this ticker / chart 

		page 				= scope.pages['display_page']
		page_ticker_list 	= scope.pages[page]['ticker_list']
		config_group		= 'tests' if page == 'screener' else 'charts'
		loaded_tickers		= list(scope.data['ticker_files'].keys())



		for ticker in page_ticker_list:

			column_adders = list(scope.pages[page]['replace_cols'][ticker].keys())
			tickers_already_loaded_for_page = list(scope.pages[page]['dfs'].keys())

			for col_adder in column_adders:
				

				replace_cols_status = scope.pages[page]['replace_cols'][ticker][col_adder]
				
				if replace_cols_status:

					call_col_adder = scope.pages[page]['replace_cols'][ticker][col_adder]

					# Check if we have been requested to renew the columns for this ticker
					if call_col_adder == True:

						if ticker in tickers_already_loaded_for_page:

							ticker_df				= scope.pages[page]['dfs'][ticker]
							column_adder			= scope.config[config_group][col_adder]['add_columns']
							column_adder_function 	= scope.config[config_group][col_adder]['add_columns']['function']

							# Column_Adder has a column_adder function
							if column_adder != None and column_adder_function != None:	
								
								# Call the column adding function for this col_adder
								scope.config[config_group][col_adder]['add_columns']['function'](scope, col_adder, ticker, ticker_df)
							
						# reset replace_cols status to prevent unnecesary updates		
						set_replace_col_adder_status_for_ticker_and_page(scope, page, ticker, col_adder, False, caller='replace_cols')



