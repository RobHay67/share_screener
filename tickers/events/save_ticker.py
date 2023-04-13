




def save_ticker_event(scope, ticker):

	# so we must have data to save... right???

	if ticker in scope.tickers['missing']['local']:
		scope.tickers['missing']['local'].remove(ticker)

	if ticker in scope.tickers['missing']['list']:
		scope.tickers['missing']['list'].remove(ticker)