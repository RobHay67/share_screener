


def update_missing_ticker_lists(scope, ticker):
	# we may not have had any local data (ie its a new ticker)
	# so we need to reset the local load status and change
	# the overall status


	if ticker in scope.tickers['missing']['local']:
		scope.tickers['missing']['local'].remove(ticker)
	
	if ticker in scope.tickers['missing']['cloud']:
		scope.tickers['missing']['cloud'].remove(ticker)

	if ticker in scope.tickers['missing']['list']:
		scope.tickers['missing']['list'].remove(ticker)