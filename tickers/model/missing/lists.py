


def update_missing_ticker_lists(scope, ticker):
	# we may not have had any local data (ie its a new ticker)
	# so we need to reset the local load status and change
	# the overall status


	if ticker in scope.ticker_schema['missing']['local']:
		scope.ticker_schema['missing']['local'].remove(ticker)
	
	if ticker in scope.ticker_schema['missing']['cloud']:
		scope.ticker_schema['missing']['cloud'].remove(ticker)

	if ticker in scope.ticker_schema['missing']['list']:
		scope.ticker_schema['missing']['list'].remove(ticker)