
# Build the initial dictionary config for each ticker that is loaded


def set_ticker_config(scope, ticker):

	# Add keys to the ticker to house the df and appropriate column adders state information

	scope.tickers[ticker]['apps'] = {}


	# Iterate through each Application
	for app in scope.apps['app_list']:

		# add a key for each app
		scope.tickers[ticker]['apps'][app] = {}

		# add a 'df' key to house the app dataframe
		scope.tickers[ticker]['apps'][app]['df'] = {}
		scope.tickers[ticker]['apps'][app]['replace_df'] = True
		scope.tickers[ticker]['apps'][app]['type_col_adder'] = None
		scope.tickers[ticker]['apps'][app]['column_adders'] = {}


		# add app specific additional column keys and set value to the active status from config

		if app == 'single':
			scope.tickers[ticker]['apps'][app]['type_col_adder'] = 'charts'
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.charts['column_adders'].copy()

		if app == 'screener':
			scope.tickers[ticker]['apps'][app]['type_col_adder'] = 'trials'
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.trials['column_adders'].copy()
		
