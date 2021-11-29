
def create_chart_df(scope, ticker_list):
	
	page = scope.page_to_display

	

	# so we only refresh if we have been asked to
	for ticker in ticker_list:
		if scope.pages[page]['refresh_chart_df'][ticker] == True:
			if ticker in scope.pages[page]['analysis_df']:												# if its not in here, it will not be available
				print ( '\033[93m' + ticker + ' < create_chart_df >  is being added to chart_df \033[0m')
				chart_df = scope.pages[page]['analysis_df'][ticker].copy()
				chart_df.sort_values(by=['date'], inplace=True, ascending=True)		

				for chart in scope.charts.keys():														# Check if need additional columns for any selected charts
					if scope.charts[chart]['active'] == True:											# User has selected to display this chart
						if scope.charts[chart]['data_cols'] != None:									# This chart has additional columns (config contains the column details)
							scope.charts[chart]['data_cols']['function'](scope, chart_df, chart)		# Call the column adding function
				
				# store the chart_df along with any additional columns that have been added
				scope.pages[page]['chart_df'][ticker] = chart_df									
				
				# reset STATUS to prevent unnecesary updates
				scope.pages[page]['refresh_chart_df'][ticker] = False
			else:
				print ( '\033[91m' + ticker + ' < create_chart_df > ticker file missing from scope.pages[page][analysis_df]\033[0m')
		else:
			print ( '\033[92m' + ticker + ' < create_chart_df > refresh not requested\033[0m')


