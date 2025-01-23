

from app.scope.model.dropdowns.controller import refresh_ticker_selector_lists


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
	for page in scope.config['page_list']:
		scope.tickers[ticker][page] = {}
		scope.tickers[ticker][page]['df'] = {}					# to store the dataframe for this page
		scope.tickers[ticker][page]['replace_df'] = True		# does the df need replace
		scope.tickers[ticker][page]['schema_group'] = None   	# relevant type of col_adder - 'charts' or 'trials'
		scope.tickers[ticker][page]['replace_column'] = {}		# dict of col_adder functions for this page

	# To Store Test (trial) Results for the SCREENER page
	page = 'screener'
	scope.tickers[ticker][page]['verdicts'] = {}
	scope.tickers[ticker][page]['verdicts']['verdict'] = None				# the overall result from all tests - they need to all pass
	scope.tickers[ticker][page]['verdicts']['replace_verdict'] = False		# if this verdict needs to be determined again
	scope.tickers[ticker][page]['verdicts']['trials'] = {}					# create a dict of all possible tests which is
	for trial in scope.trials['trial_list']:								#   then utilised to save that test result
		scope.tickers[ticker][page]['verdicts']['trials'][trial] = None		#   which will be a pass or fail result
	
	refresh_ticker_selector_lists(scope)

