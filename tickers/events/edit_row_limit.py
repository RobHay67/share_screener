

def edit_row_limit_event(scope):

	# This event is triggered when the user sets a new row limit for
	# every page - there is only a singlr global row limit
	#
	# page dataframes will require refreshing
	# Column  adders will require refreshing as well
	
	for ticker in scope.tickers.keys():
		for page in scope.page['page_list']:

			scope.tickers[ticker][page]['replace_df'] = True

			if page == 'chart':
				scope.tickers[ticker][page]['column_adders'] = scope.chart_settings['column_adders'].copy()

			if page == 'screener':
				scope.tickers[ticker][page]['column_adders'] = scope.trial_settings['column_adders'].copy()







