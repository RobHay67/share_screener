# Add keys to scope.tickers object
# Ready to house : 
#  - ticker date in df 
# Add appropriate column adders state information
# This function only generates the empty containers and default values. 
# Data is added by other functions.


def scope_ticker_files(scope):
	scope.tickers = {}


def scope_new_ticker(scope, ticker):

	scope.tickers[ticker] = {}
	
	# To store the raw ticker data
	scope.tickers[ticker]['df'] = {}

	# Ticker Config for each Application / Page
	for app in scope.apps['app_list']:
		scope.tickers[ticker][app] = {}
		scope.tickers[ticker][app]['df'] = {}					# to store the dataframe for this page
		scope.tickers[ticker][app]['replace_df'] = True			# does the df need replace
		scope.tickers[ticker][app]['type_col_adder'] = None   	# relevant type of col_adder - 'charts' or 'trials'
		scope.tickers[ticker][app]['column_adders'] = {}		# dict of col_adder functions for this page

		# To Store Test (trial) Results for the screener page
		if app == 'screener':

			scope.tickers[ticker][app]['verdict'] = None
			scope.tickers[ticker][app]['replace_verdict'] = False
			scope.tickers[ticker][app]['trials'] = {}
			for trial in scope.trial_config['trial_list']:
				scope.tickers[ticker][app]['trials'][trial] = None


