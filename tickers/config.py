



def scope_ticker_files(scope):

	scope.tickers = {}


def scope_missing_tickers(scope):
	scope.missing_tickers = {}
	scope.missing_tickers['errors'] = {}
	scope.missing_tickers['local'] = []
	scope.missing_tickers['cloud'] = []
	scope.missing_tickers['list']  = []


def scope_missing_ticker_error(scope, ticker):
	scope.missing_tickers['errors'][ticker] = {'load':None, 'yf':None}



def scope_new_ticker(scope, ticker):

	# Add keys to scope.tickers object
	# ready to house : 
	#  - ticker date in df 
	# add appropriate column adders state information
	# This function only generates the empty containers and
	# default values. 
	# Data is added by other functions.


	# Store the ticker data in ['df']
	scope.tickers[ticker] = {}
	
	# To store the raw ticker data - all we have
	scope.tickers[ticker]['df'] = {}

	# To Store Trial Results
	scope.tickers[ticker]['trials'] = {}
	for trial in scope.trial_config['trial_list']:
		scope.tickers[ticker]['trials'][trial] = None


	# Ticker Config for each Application
	for app in scope.apps['app_list']:

		# add a key for each app
		scope.tickers[ticker][app] = {}

		# add a 'df' key to house the app dataframe
		scope.tickers[ticker][app]['df'] = {}
		scope.tickers[ticker][app]['replace_df'] = True
		scope.tickers[ticker][app]['type_col_adder'] = None
		scope.tickers[ticker][app]['column_adders'] = {}

	print(scope.tickers[ticker]['trials'])