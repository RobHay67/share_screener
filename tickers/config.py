from pages.header.selectors import refresh_ticker_dropdown_for_config




def scope_tickers(scope):
	scope.tickers = {}



def create_dictionary_to_store_ticker_data(scope, ticker):

	# This function is triggered after NEW ticker data is either
	# - loaded 
	# or 
	# - downloaded (we may not have had local data)

	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information

	# This function only generates the empty objects with
	# the default values. Data is added by other functions.


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
	
	refresh_ticker_dropdown_for_config(scope)