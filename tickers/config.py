# Add keys to scope.tickers object
# Ready to house : 
#  - ticker date in df 
# Add appropriate column adders state information
# This function only generates the empty containers and default values. 
# Data is added by other functions.
# Also includes any missing ticker information in the scope.tickers_missing object



def scope_tickers(scope):
	scope.tickers = {}


def scope_new_ticker(scope, ticker):

	scope.tickers[ticker] = {}
	
	# To store the raw ticker data
	scope.tickers[ticker]['df'] = {}

	# Ticker Config for each Application / Page
	for page in scope.pages['page_list']:
		scope.tickers[ticker][page] = {}
		scope.tickers[ticker][page]['df'] = {}					# to store the dataframe for this page
		scope.tickers[ticker][page]['replace_df'] = True		# does the df need replace
		scope.tickers[ticker][page]['config_group'] = None   	# relevant type of col_adder - 'charts' or 'trials'
		scope.tickers[ticker][page]['replace_column'] = {}		# dict of col_adder functions for this page

		# To Store Test (trial) Results for the screener page
		if page == 'screener':

			scope.tickers[ticker][page]['verdict'] = None
			scope.tickers[ticker][page]['replace_verdict'] = False
			scope.tickers[ticker][page]['trials'] = {}
			for trial in scope.trials['trial_list']:
				scope.tickers[ticker][page]['trials'][trial] = None


def scope_tickers_missing(scope):
	# To Store the missing ticker information
	scope.tickers_missing = {
								'errors': {},
								'local' : [],
								'cloud' : [],
								'list'  : [],
								}
	
	
def scope_missing_ticker_error(scope, ticker):
	scope.tickers_missing['errors'][ticker] = {'load':None, 'yf':None}


