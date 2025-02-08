import logging




def save_ticker_event(scope, ticker):
	logging.warning("save_ticker_event")
	# so we must have data to save... right???

	if ticker in scope.ticker_schema['missing']['local']:
		scope.ticker_schema['missing']['local'].remove(ticker)

	if ticker in scope.ticker_schema['missing']['list']:
		scope.ticker_schema['missing']['list'].remove(ticker)