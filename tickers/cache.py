

def cache_ticker_file(scope, ticker, ticker_data_file):

	# This event is triggered when new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information


	# Sort ticker file into ascending order
	ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)	

	# Store the ticker data in ['df']
	scope.tickers[ticker] = {}
	scope.tickers[ticker]['df'] = ticker_data_file

	# Config for each APP
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
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.chart_config['column_adders'].copy()

		if app == 'screener':
			scope.tickers[ticker]['apps'][app]['type_col_adder'] = 'trials'
			scope.tickers[ticker]['apps'][app]['column_adders'] = scope.trial_config['column_adders'].copy()



# Sample scope.
# TICKER 		= 'CBA.AX'
# dataframe 	= 'DataFrame'
# app1 		= 'volume'
# app2 		= 'screener'


# sample_scope = 'tickers':{
# 					TICKER:{
# 							'df': dataframe,
# 							'apps': {
# 									app1:{
# 											'df'				:dataframe,
# 											'replace_df'		:True,			# True or False,
# 											'type_column_adder'	:None, 			# None, 'charts' or 'trials'
# 											'column_adders'		:{},
# 										},
# 									app2:{
# 											'df'				:dataframe,
# 											'replace_df'		:True,			# True or False,
# 											'type_column_adder'	:None, 			# None, 'charts' or 'trials'
# 											'column_adders': {
# 																'trend_open': False, 
# 																'trend_high': True, 
# 																'trend_low': False, 
# 																'trend_close': True, 
# 																'trend_volume': False,
# 															},
# 										},
# 									},
# 							},
# 						}

