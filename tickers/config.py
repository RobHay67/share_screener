
def scope_ticker_files(scope):
	scope.tickers = {}


def scope_new_ticker(scope, ticker):

	# Add keys to scope.tickers object
	# Ready to house : 
	#  - ticker date in df 
	# Add appropriate column adders state information
	# This function only generates the empty containers and default values. 
	# Data is added by other functions.

	scope.tickers[ticker] = {}
	
	# To store the raw ticker data
	scope.tickers[ticker]['df'] = {}

	# To Store Trial Results
	scope.tickers[ticker]['trials'] = {}
	for trial in scope.trial_config['trial_list']:
		scope.tickers[ticker]['trials'][trial] = None
	scope.tickers[ticker]['trials']['verdict'] = None


	# Ticker Config for each Application
	for app in scope.apps['app_list']:
		# add a key for each app
		scope.tickers[ticker][app] = {}
		# add a 'df' key to house the app dataframe
		# and other df and column management information
		scope.tickers[ticker][app]['df'] = {}
		scope.tickers[ticker][app]['replace_df'] = True
		scope.tickers[ticker][app]['type_col_adder'] = None   # 'charts' or 'trials'
		scope.tickers[ticker][app]['column_adders'] = {}

