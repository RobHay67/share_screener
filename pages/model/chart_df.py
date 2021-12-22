
def update_chart_dfs(scope):
	
	page 			= scope.page_to_display
	page_row_limit 	= int(scope.page_row_limit)
	ticker_list 	= scope.pages[page]['ticker_list']
	
	if page != 'screener':																			# works on all pages except the screener page
		for ticker in ticker_list:																	# iterate through each ticker for the page 
			if scope.pages[page]['add_ohlcv_data'][ticker] == True:									# so we only refresh if we have been asked to
				if ticker in scope.ticker_data_files:												# if data missing, function will not be able to run
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to chart_df where page = ' + page + '\033[0m')
					chart_df = scope.ticker_data_files[ticker].copy()								# short reference to the object being edited
					chart_df.sort_values(by=['date'], inplace=True, ascending=True)					# sort the df into the correct order for the charting
					if page_row_limit != None : 													# limit analysis to user specified row limit
						chart_df = chart_df.head(page_row_limit) 									
					scope.pages[page]['chart_df'][ticker] = chart_df								# store the chart_df for use by the page			
					scope.pages[page]['add_ohlcv_data'][ticker] = False								# reset page df STATUS to prevent unnecesary updates
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.ticker_data_files \033[0m')
			else:
				print ( '\033[96m' + ticker.ljust(10) + '> add_ohlcv_data not requested \033[0m')



def update_chart_metrics(scope):
	
	page 		= scope.page_to_display
	ticker_list = scope.pages[page]['ticker_list']

	if page != 'screener':																					# works on all pages except the screen page
		for ticker in ticker_list:																			# iterate through each ticker for the page
			if ticker in scope.pages[page]['chart_df'].keys():												# if data missing, function will not be able to run
				chart_df = scope.pages[page]['chart_df'][ticker]											# short reference to the object being edited
				for chart in scope.pages[page]['add_chart_data'][ticker].keys():							# iterate through available charts for this ticker and their run (or not) status
					chart_run_status  	= scope.pages[page]['add_chart_data'][ticker][chart]
					chart_has_metrics	= scope.charts[chart]['metrics']
					metric_has_function = scope.charts[chart]['metrics']['function']
					if chart_run_status==True and chart_has_metrics!=None and metric_has_function != None:	# Chart needs refreshing and has metrics and requires additional columns (function)
						scope.charts[chart]['metrics']['function'](scope, chart_df, chart)					# Call the column adding function
						scope.pages[page]['add_chart_data'][ticker][chart] = False							# reset Chart Data STATUS to prevent unnecesary updates


