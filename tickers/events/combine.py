




def set_data_status(scope, ticker):

	# This event is triggered when new ticker data has been successfully downloaded
	# and combined with the existing loaded date
	# App dataframes will require refreshing
	# Column  adders will require refreshing as well

	for app in scope.apps['app_list']:

		scope.tickers[ticker]['apps'][app]['replace_df'] = True

		if app == 'single':
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.chart_config['column_adders'].copy()

		if app == 'screener':
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.trial_config['column_adders'].copy()




