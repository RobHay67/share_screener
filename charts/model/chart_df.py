
def create_chart_df(scope, ticker_list):
	
	page = scope.page_to_display


	if scope.pages[page]['refresh_chart_df'] == True:
		for ticker in ticker_list:
			print ( '\033[93m' + ticker + ' > create_chart_df is being rebuilt \033[0m')

			# if ticker in scope.ticker_data_files:
			if ticker in scope.pages[page]['analysis_df']:												# if its not in here, it will not be available
				chart_df = scope.pages[page]['analysis_df'][ticker].copy()
				chart_df.sort_values(by=['date'], inplace=True, ascending=True)		

				for chart in scope.charts.keys():														# Check if need additional columns for any selected charts
					if scope.charts[chart]['active'] == True:											# User has selected to display this chart
						if scope.charts[chart]['data_cols'] != None:									# This chart has additional columns (config contain the column details)
							scope.charts[chart]['data_cols']['function'](scope, chart_df, chart)		# Call the column adding function
				
				# store the chart_df along with any additional columns that have been added
				scope.pages[page]['chart_df'][ticker] = chart_df									
				
				# reset STATUS to prevent unnecesary updates
				scope.pages[page]['refresh_chart_df'] = False
	
	# else:
	# 	print ( '\033[92m' + 'create_chart_df is NOT being re-run \033[0m')


