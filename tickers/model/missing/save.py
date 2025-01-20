




def save_ticker_event(scope, ticker):

	# so we must have data to save... right???

	if ticker in scope.ticker_config['missing']['local']:
		scope.ticker_config['missing']['local'].remove(ticker)

	if ticker in scope.ticker_config['missing']['list']:
		scope.ticker_config['missing']['list'].remove(ticker)