



def scope_ticker_files(scope):


	# TODO - replace this with just the tickers
	scope.ticker_files = {}

	scope.tickers = {}







def scope_download_variables(scope):

	scope.download 					= {}
	scope.download['days'] 			= 7
	scope.download['industries'] 	= ['random_tickers']

	scope.download['yf_files']		= {}
	scope.download['yf_anomolies'] 	= {}
	scope.download['missing_list'] 	= []



def ticker_status(scope, ticker):

	# So now we add the apps that might need to use this ticker

	scope.tickers[ticker]['apps'] = {}

	for app in scope.apps['app_list']:
		scope.tickers[ticker]['apps'][app] = {}

		scope.tickers[ticker]['apps'][app]['df'] = {}

		if app == 'single':
			for chart in scope.charts['chart_list']:
				scope.tickers[ticker]['apps'][app][chart] = scope.charts[chart]['active']
		
		if app == 'screener':
			for trial in scope.trials['trial_list']:
				scope.tickers[ticker]['apps'][app][trial] = scope.trials[trial]['active']
		
		
		
		
		print(scope.charts['chart_list'])

	# print(scope.tickers[ticker]['apps'])

