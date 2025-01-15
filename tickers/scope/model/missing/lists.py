


def update_missing_ticker_lists(scope, ticker):
	# we may not have had any local data (ie its a new ticker)
	# so we need to reset the local load status and change
	# the overall status


	if ticker in scope.ticker_config['missing']['local']:
		scope.ticker_config['missing']['local'].remove(ticker)
	
	if ticker in scope.ticker_config['missing']['cloud']:
		scope.ticker_config['missing']['cloud'].remove(ticker)

	if ticker in scope.ticker_config['missing']['list']:
		scope.ticker_config['missing']['list'].remove(ticker)