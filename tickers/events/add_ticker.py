
from tickers.config import scope_new_ticker


def add_ticker_event(scope, ticker):

	# This event is triggered after new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information
	# This function only generate the empty objects with
	# the default values. Data is added by other functions.


	scope_new_ticker(scope, ticker)


	# # Store the ticker data in ['df']
	# scope.tickers[ticker] = {}
	

	# # Config for each APP
	# scope.tickers[ticker] = {}

	# # Iterate through each Application
	# for app in scope.apps['app_list']:

	# 	# add a key for each app
	# 	scope.tickers[ticker][app] = {}

	# 	# add a 'df' key to house the app dataframe
	# 	scope.tickers[ticker][app]['df'] = {}
	# 	scope.tickers[ticker][app]['replace_df'] = True
	# 	scope.tickers[ticker][app]['type_col_adder'] = None
	# 	scope.tickers[ticker][app]['column_adders'] = {}

