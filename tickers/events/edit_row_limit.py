

def set_data_status(scope):

	# This event is triggered when the user sets a new row limit for
	# every app - there is only a singlr global row limit
	#
	# App dataframes will require refreshing
	# Column  adders will require refreshing as well

	print('editing the row limit')
	
	for ticker in scope.tickers.keys():
		for app in scope.apps['app_list']:

			scope.tickers[ticker]['apps'][app]['replace_df'] = True

			if app == 'single':
				scope.tickers[ticker]['apps'][app]['column_adders'] = scope.chart_config['column_adders'].copy()

			if app == 'screener':
				scope.tickers[ticker]['apps'][app]['column_adders'] = scope.trial_config['column_adders'].copy()







