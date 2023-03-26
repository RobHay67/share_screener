




def cache_ticker_data(scope, ticker, ticker_data):

	# This event is triggered after new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information


	app = scope.apps['display_app']


	# Sort ticker file into ascending order
	ticker_data.sort_values(by=['date'], inplace=True, ascending=False)	

	# cache the ticker data in the primary object holder
	scope.tickers[ticker]['df'] = ticker_data	
		
	# add Column Adders for the type of app/page
	#  - type of column adder
	#  - and the current config template (dict of functions) 

	for app in scope.apps['app_list']:

		if app == 'chart':
			scope.tickers[ticker][app]['type_col_adder'] = 'charts'
			scope.tickers[ticker][app]['column_adders'] = scope.chart_config['column_adders'].copy()

		if app == 'screener':
			scope.tickers[ticker][app]['type_col_adder'] = 'trials'
			scope.tickers[ticker][app]['column_adders'] = scope.trial_config['column_adders'].copy()


