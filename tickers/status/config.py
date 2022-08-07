
# Build the initial dictionary config for each ticker that is loaded
# TODO - for future, it might be easier to do this from a list of the loaded tickers - then we can save on generating the chart and trial dictionary part objects



def set_ticker_config(scope, ticker):

	# Add keys to the ticker to house the df and appropriate column adders information

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
			# add the charts to the single app
			for chart in scope.charts['chart_list']:
				# Add charts that require additional columns
				if scope.charts[chart]['add_columns'] != None:
					scope.tickers[ticker]['apps'][app]['column_adders'][chart] = scope.charts[chart]['active']
		
		if app == 'screener':
			scope.tickers[ticker]['apps'][app]['type_col_adder'] = 'trials'
			# add the trials to the screener app
			for trial in scope.trials['trial_list']:
				# Add trials that require additional columns
				if scope.trials[trial]['add_columns'] != None:
					scope.tickers[ticker]['apps'][app]['column_adders'][trial] = scope.trials[trial]['active']
		

