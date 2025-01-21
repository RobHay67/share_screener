




def save_ticker_event(scope, ticker):

	# so we must have data to save... right???

	if ticker in scope.ticker_schema['missing']['local']:
		scope.ticker_schema['missing']['local'].remove(ticker)

	if ticker in scope.ticker_schema['missing']['list']:
		scope.ticker_schema['missing']['list'].remove(ticker)