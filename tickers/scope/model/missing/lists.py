


def update_missing_ticker_lists(scope, ticker):
	# we may not have had any local data (ie its a new ticker)
	# so we need to reset the local load status and change
	# the overall status


	if ticker in scope.tickers_missing['local']:
		scope.tickers_missing['local'].remove(ticker)
	
	if ticker in scope.tickers_missing['cloud']:
		scope.tickers_missing['cloud'].remove(ticker)

	if ticker in scope.tickers_missing['list']:
		scope.tickers_missing['list'].remove(ticker)