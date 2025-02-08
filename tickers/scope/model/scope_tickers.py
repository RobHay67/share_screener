import logging


def scope_tickers(scope):
	logging.warning("scope_tickers")
	scope.tickers = {}


def scope_for_new_ticker_data(scope, ticker):
	logging.warning("scope_for_new_ticker_data")
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
		scope.tickers[ticker][page]['df'] = {}					# container to store the dataframe for this page
		scope.tickers[ticker][page]['replace_df'] = True		# status to flag replacement of entire page dataframe
		scope.tickers[ticker][page]['schema_group'] = None   	# relevant type of col_adder - 'charts' or 'trials'
		scope.tickers[ticker][page]['re_run_functions'] = {}	# dict of col_adder functions (key) and Status to 
																# - indicate if the col_adder need to be replaced (value True or False)

	# To Store Test (trial) Results for the SCREENER page
	page = 'screener'
	scope.tickers[ticker][page]['verdicts'] = {}
	scope.tickers[ticker][page]['verdicts']['overall_verdict'] = None		# the overall result from all tests - they need to all pass
	scope.tickers[ticker][page]['verdicts']['re_run_trials'] = False			# if this verdict needs to be determined again
	scope.tickers[ticker][page]['verdicts']['trial_verdicts'] = {}				# create a dict of all possible tests which is
	for trial in scope.trials['trial_list']:									#   then utilised to save that test result
		scope.tickers[ticker][page]['verdicts']['trial_verdicts'][trial] = None	#   which will be a pass or fail result
	
