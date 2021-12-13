
def create_chart_df(scope, ticker_list):
	
	page 				= scope.page_to_display
	analysis_row_limit 	= int(scope.analysis_row_limit)
	
	if page != 'screener':
		for ticker in ticker_list:
			if scope.pages[page]['refresh_ticker_df'][ticker] == True:										# so we only refresh if we have been asked to
				if ticker in scope.ticker_data_files:														# if its not in here, it will not be available
					print ( '\033[93m' + ticker + ' < create_chart_df    > adding ticker to chart_df where page = ' + page + '\033[0m')
					chart_df = scope.ticker_data_files[ticker].copy()
					chart_df.sort_values(by=['date'], inplace=True, ascending=True)		
					if analysis_row_limit != None : 
						chart_df = chart_df.head(analysis_row_limit) 										# limit analysis to user specified row limit

					for chart in scope.charts.keys():														# Check if need additional columns for any selected charts
						if scope.charts[chart]['active'] == True:											# User has selected to display this chart
							if scope.charts[chart]['data_cols'] != None:									# This chart has additional columns (config contains the column details)
								if scope.charts[chart]['data_cols']['function'] != None:					# Some chart use the existing OHLCV columns
									scope.charts[chart]['data_cols']['function'](scope, chart_df, chart)	# Call the column adding function
					
					scope.pages[page]['chart_df'][ticker] = chart_df										# store the chart_df along with any additional columns that have been added				
					
					scope.pages[page]['refresh_ticker_df'][ticker] = False									# reset STATUS to prevent unnecesary updates
				else:
					print ( '\033[91m' + ticker + ' < create_chart_df    > ticker file missing from scope.pages[page][screener_df]\033[0m')
			else:
				print ( '\033[92m' + ticker + ' < create_chart_df    > refresh not requested \033[0m')


