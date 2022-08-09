
def set_app_config_for_ticker(scope, ticker):


	# This event is triggered when new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information

	print(scope.tickers[ticker]['df'].sample(10))

	# scope.tickers[ticker] = {}

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


		# add Column Adders for each type of app 
		# set initial values to the active status from charts and trials config

		if app == 'single':
			scope.tickers[ticker]['apps'][app]['type_col_adder'] = 'charts'
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.charts['column_adders'].copy()

		if app == 'screener':
			scope.tickers[ticker]['apps'][app]['type_col_adder'] = 'trials'
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.trials['column_adders'].copy()
		
		print('-'*55)
		for key,value in scope.tickers[ticker]['apps'][app].items():print (key)
		print('-'*55)
		# print(app)
		# print(scope.tickers[ticker]['apps'][app])


# CBA.AX    > loading local ticker file 
# single
# {'df': {}, 'replace_df': True, 'type_col_adder': 'charts', 'column_adders': {'macd': True, 'macd_vol': True, 'rsi': True, 'vol_osssy': False, 'stochastic': True, 'sma_1': False, 'sma_2': False, 'sma_3': False, 'ema_1': False, 'ema_2': False, 'ema_3': False, 'bollinger_bands': False, 'dividends': True}}
# intraday
# {'df': {}, 'replace_df': True, 'type_col_adder': None, 'column_adders': {}}
# volume
# {'df': {}, 'replace_df': True, 'type_col_adder': None, 'column_adders': {}}
# research
# {'df': {}, 'replace_df': True, 'type_col_adder': None, 'column_adders': {}}
# screener
# {'df': {}, 'replace_df': True, 'type_col_adder': 'trials', 'column_adders': {'trend_open': False, 'trend_high': True, 'trend_low': False, 'trend_close': False, 'trend_volume': False}}


# scope.tickers[CBA.AX]['apps'][screener]['replace_df']