

def edit_row_limit_event(scope):

	# This event is triggered when the user sets a new row limit for
	# every app - there is only a singlr global row limit
	#
	# App dataframes will require refreshing
	# Column  adders will require refreshing as well
	
	for ticker in scope.tickers.keys():
		for app in scope.apps['app_list']:

			scope.tickers[ticker][app]['replace_df'] = True

			if app == 'chart':
				scope.tickers[ticker][app]['column_adders'] = scope.chart_config['column_adders'].copy()

			if app == 'screener':
				scope.tickers[ticker][app]['column_adders'] = scope.trial_config['column_adders'].copy()







