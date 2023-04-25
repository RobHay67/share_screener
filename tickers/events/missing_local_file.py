from tickers.config import scope_missing_ticker_error

def missing_file_event(scope, ticker):
	# There is no local file so record this fact
	# to prevent further attempts to load the local file

	scope.tickers_missing['local'].append(ticker)
	scope.tickers_missing['list'].append(ticker)

	# Cache Error
	if ticker not in scope.tickers_missing['errors']:
		scope_missing_ticker_error(scope, ticker)
	scope.tickers_missing['errors'][ticker]['load'] = 'Missing Local file'



