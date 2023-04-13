from tickers.config import scope_missing_ticker_error

def missing_file_event(scope, ticker):
	# There is no local file so record this fact
	# to prevent further attempts to load the local file

	scope.tickers['missing']['local'].append(ticker)
	scope.tickers['missing']['list'].append(ticker)

	# Cache Error
	if ticker not in scope.tickers['missing']['errors']:
		scope_missing_ticker_error(scope, ticker)
	scope.tickers['missing']['errors'][ticker]['load'] = 'Missing Local file'



