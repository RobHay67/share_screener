




def save_ticker_event(scope, ticker):

	# so we must have data to save... right???

	if ticker in scope.missing_tickers['local']:
		scope.missing_tickers['local'].remove(ticker)

	if ticker in scope.missing_tickers['list']:
		scope.missing_tickers['list'].remove(ticker)