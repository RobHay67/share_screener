





def update_chart_dfs(scope):
	
	page 			= scope.pages['display_page']
	page_row_limit 	= int(scope.pages['row_limit'])
	
	# All pages have chart metrics, except for the screener page
	if page != 'screener':

		for ticker in scope.pages[page]['ticker_list']:
			
			# ====================================================================
			# Replace all of the share data for the ticker

			# Check if we have been requested to update the share_data for this ticker
			if scope.pages[page]['renew']['ticker_data'][ticker] == True:

				# Check that there is share data available for this ticker
				# before attempting to copy that share date for use by this page
				# (function will fail if ticker data is not available) 

				if ticker in scope.data['ticker_files']: 
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to chart_df where page = ' + page + '\033[0m')
					chart_df = scope.data['ticker_files'][ticker].copy()								# short reference to the object being edited
					chart_df.sort_values(by=['date'], inplace=True, ascending=True)					# sort the df into the correct order for the charting
					
					# limit no of rows for the page_df (speeds up page rendering)
					if page_row_limit != None : 
						chart_df = chart_df.tail(page_row_limit) 									
					
					# Store the page data for use by the page
					scope.pages[page]['df'][ticker] = chart_df

					# reset Share Data Refresh STATUS to prevent unnecesary updates				
					scope.pages[page]['renew']['ticker_data'][ticker] = False
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.data[ticker_files] \033[0m')


			# ====================================================================
			# Replace the columns / metrics required for this ticker / chart 

			# iterate through each chart being utilised by this page
			# for chart in scope.pages[page]['renew']['expanders'][ticker].keys():
				
			# 	# and check if we have been requested to update the metrics columns
			# 	if scope.pages[page]['renew']['expanders'][ticker][chart] == True:

			# 		# Check that the page share_data is present for this ticker before 
			# 		# attempting to make changes to its dataframe
			# 		# (function will fail if not present)
					
			# 		if ticker in scope.pages[page]['df'].keys():
						
			# 			chart_df = scope.pages[page]['df'][ticker]

			# 			# iterate through each chart being utilised by this ticker 
			# 			# and then execute (or not) the column adding function
						
			# 				chart_refresh_requested = scope.pages[page]['renew']['expanders'][ticker][chart]
			# 				chart_has_metric		= scope.config['expanders'][chart]['add_columns']
			# 				metric_has_function 	= scope.config['expanders'][chart]['add_columns']['function']
							
			# 				# Chart needs refreshing and has metrics and requires additional columns (function)
			# 				if chart_refresh_requested==True and chart_has_metric!=None and metric_has_function != None:	
								
			# 					# Call the metrics (column) adding function
			# 					scope.config['expanders'][chart]['add_columns']['function'](scope, chart_df, chart)		
								
			# 					# reset Chart Data Refresh STATUS to prevent unnecesary updates
			# 					scope.pages[page]['renew']['expanders'][ticker][chart] = False		







def update_chart_metrics(scope):
	
	page 		= scope.pages['display_page']

	# All pages have chart metrics, except for the screener page
	if page != 'screener':

		for ticker in scope.pages[page]['ticker_list']:
			
			# Check that the page share_data is present for this ticker before 
			# attempting to make changes to its dataframe
			# (function will fail if not present)
			
			if ticker in scope.pages[page]['df'].keys():
				
				chart_df = scope.pages[page]['df'][ticker]

				# iterate through each chart being utilised by this ticker 
				# and then execute (or not) the column adding function
				for chart in scope.pages[page]['renew']['expanders'][ticker].keys():
					chart_refresh_requested = scope.pages[page]['renew']['expanders'][ticker][chart]
					chart_has_metric		= scope.config['expanders'][chart]['add_columns']
					metric_has_function 	= scope.config['expanders'][chart]['add_columns']['function']
					
					# Chart needs refreshing and has metrics and requires additional columns (function)
					if chart_refresh_requested==True and chart_has_metric!=None and metric_has_function != None:	
						
						# Call the metrics (column) adding function
						scope.config['expanders'][chart]['add_columns']['function'](scope, chart_df, chart)		
						
						# reset Chart Data Refresh STATUS to prevent unnecesary updates
						scope.pages[page]['renew']['expanders'][ticker][chart] = False					


