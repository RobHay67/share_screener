




def save_ticker_event(scope, ticker):

	# so we must have data to save... right???

	if ticker in scope.tickers_missing['local']:
		scope.tickers_missing['local'].remove(ticker)

	if ticker in scope.tickers_missing['list']:
		scope.tickers_missing['list'].remove(ticker)