
def update_page_dfs(scope):
	
	page 				= scope.pages['display_page']
	page_row_limit 		= int(scope.pages['row_limit'])
	page_ticker_list 	= scope.pages[page]['ticker_list']
	config_group		= 'tests' if page == 'screener' else 'charts'
	loaded_tickers		= list(scope.data['ticker_files'].keys())

	
	for ticker in page_ticker_list:
		
		renew_ticker_data_status = scope.pages[page]['renew']['ticker_data'][ticker]

		
		# renew_expansions_for_ticker = list(scope.pages[page]['renew']['expanders']  [ticker].keys())
		# ====================================================================
		# Replace all of the ticker data for the ticker
		# ====================================================================

		# Check if we have been requested to renew the ticker data for this ticker
		if  renew_ticker_data_status == True:

				# Check that there is share data available for this ticker
				# before attempting to copy that share date for use by this page
				# (function will fail if ticker data is not available) 

				if ticker in loaded_tickers: 
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to page df where page = ' + page + '\033[0m')
					
					ticker_df = scope.data['ticker_files'][ticker].copy()
					
					# sort the df into the correct order for the charting
					ticker_df.sort_values(by=['date'], inplace=True, ascending=True)
					
					# limit no of rows for the page_df (speeds up page rendering)
					if page_row_limit != None : 
						ticker_df = ticker_df.tail(page_row_limit) 									
					
					# Store the page data for use by the page
					scope.pages[page]['df'][ticker] = ticker_df

					# reset Share Data Refresh STATUS to prevent unnecesary updates				
					scope.pages[page]['renew']['ticker_data'][ticker] = False
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.data[ticker_files] \033[0m')


		# ====================================================================
		# Replace the columns / metrics required for this ticker / chart 
		# ====================================================================

		expanders = list(scope.pages[page]['renew']['expanders'][ticker].keys())
		tickers_already_loaded_for_page = list(scope.pages[page]['df'].keys())

		for expander in expanders:
			
			renew_expander = scope.pages[page]['renew']['expanders'][ticker][expander]

			# Check if we have been requested to renew the metrics columns for this ticker
			if renew_expander == True:
				
				if ticker in tickers_already_loaded_for_page:

					ticker_df				= scope.pages[page]['df'][ticker]
					column_adder			= scope.config[config_group][expander]['add_columns']
					column_adder_function 	= scope.config[config_group][expander]['add_columns']['function']

					# Expansion has a column_adder which requires additional columns (ie. has a function)
					if column_adder != None and column_adder_function != None:	
						
						# Call the column adding function for this expander
						scope.config[config_group][expander]['add_columns']['function'](scope, ticker_df, expander)
						
						# reset the refresh.metric_cols STATUS to prevent unnecesary updates
						scope.pages[page]['renew']['expanders'][ticker][expander] = False	







# def update_chart_metrics(scope):
		# for ticker in scope.pages[page]['ticker_list']:
			
			# Check that the page share_data is present for this ticker before 
			# attempting to make changes to its dataframe
			# (function will fail if not present)
			
			# if ticker in scope.pages[page]['df'].keys():
				
				# chart_df = scope.pages[page]['df'][ticker]

				# iterate through each chart being utilised by this ticker 
				# and then execute (or not) the column adding function
				# for chart in scope.pages[page]['renew']['expanders'][ticker].keys():
					# chart_refresh_requested = scope.pages[page]['renew']['expanders'][ticker][chart]
					# chart_has_metric		= scope.config['expanders'][chart]['add_columns']
					# metric_has_function 	= scope.config['expanders'][chart]['add_columns']['function']
					
					# Chart needs refreshing and has metrics and requires additional columns (function)
					# if chart_refresh_requested==True and chart_has_metric!=None and metric_has_function != None:	
						
						# # Call the metrics (column) adding function
						# scope.config['expanders'][chart]['add_columns']['function'](scope, chart_df, chart)		
						
						# # reset Chart Data Refresh STATUS to prevent unnecesary updates
						# scope.pages[page]['renew']['expanders'][ticker][chart] = False					


