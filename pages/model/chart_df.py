
def update_chart_dfs(scope, ticker_list):
	
	page 				= scope.page_to_display
	page_row_limit 	= int(scope.page_row_limit)
	
	if page != 'screener':																					# works on all pages except the screen page
		for ticker in ticker_list:
			if scope.pages[page]['refresh_ticker_data'][ticker] == True:									# so we only refresh if we have been asked to
				if ticker in scope.ticker_data_files:														# if its not in here, it will not be available
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to chart_df where page = ' + page + '\033[0m')
					chart_df = scope.ticker_data_files[ticker].copy()
					chart_df.sort_values(by=['date'], inplace=True, ascending=True)		
					if page_row_limit != None : 
						chart_df = chart_df.head(page_row_limit) 										# limit analysis to user specified row limit

					# for chart in scope.charts.keys():														# Check if need additional columns for any selected charts
					# 	if scope.charts[chart]['active'] == True:											# User has selected to display this chart
					# 		if scope.charts[chart]['metrics'] != None:									# This chart has additional columns (config contains the column details)
					# 			if scope.charts[chart]['metrics']['function'] != None:					# Some chart use the existing OHLCV columns
					# 				scope.charts[chart]['metrics']['function'](scope, chart_df, chart)	# Call the column adding function
					
					scope.pages[page]['chart_df'][ticker] = chart_df										# store the chart_df along with any additional columns that have been added				
					
					scope.pages[page]['refresh_ticker_data'][ticker] = False									# reset STATUS to prevent unnecesary updates
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.ticker_data_files \033[0m')
			else:
				print ( '\033[96m' + ticker.ljust(10) + '> refresh_ticker_data not requested \033[0m')



def update_chart_metrics(scope, ticker_list):
	
	page 				= scope.page_to_display

	if page != 'screener':																					# works on all pages except the screen page
		for ticker in ticker_list:																			# iterate through each ticker for the page
			# we need to refer to the refresh_metrics at this point???
			if ticker in scope.pages[page]['chart_df'].keys():												# if data missing, function will not be able to run
				chart_df = scope.pages[page]['chart_df'][ticker]											# short reference to the object being edited
				for chart in scope.charts.keys():														# Check if need additional columns for any selected charts
					if scope.charts[chart]['active'] == True:											# User has selected to display this chart
						if scope.charts[chart]['metrics'] != None:									# This chart has additional columns (config contains the column details)
							if scope.charts[chart]['metrics']['function'] != None:					# Some chart use the existing OHLCV columns
								scope.charts[chart]['metrics']['function'](scope, chart_df, chart)	# Call the column adding function


				scope.pages[page]['refresh_metrics'][ticker] = False									# reset STATUS to prevent unnecesary updates
