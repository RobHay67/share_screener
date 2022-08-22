




def add_ticker_event(scope, ticker):

	# This event is triggered after new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information
	# This function only generate the empty objects with
	# there default values. Data is added by other functions.


	# Store the ticker data in ['df']
	scope.tickers[ticker] = {}
	

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

