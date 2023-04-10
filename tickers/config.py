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
	for page in scope.pages['page_list']:
		scope.tickers[ticker][page] = {}
		scope.tickers[ticker][page]['df'] = {}					# to store the dataframe for this page
		scope.tickers[ticker][page]['replace_df'] = True		# does the df need replace
		scope.tickers[ticker][page]['config_group'] = None   	# relevant type of col_adder - 'charts' or 'trials'
		scope.tickers[ticker][page]['column_adders'] = {}		# dict of col_adder functions for this page

		# To Store Test (trial) Results for the screener page
		if page == 'screener':

			scope.tickers[ticker][page]['verdict'] = None
			scope.tickers[ticker][page]['replace_verdict'] = False
			scope.tickers[ticker][page]['trials'] = {}
			for trial in scope.trial_settings['trial_list']:
				scope.tickers[ticker][page]['trials'][trial] = None


