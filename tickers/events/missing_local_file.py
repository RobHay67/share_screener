
from tickers.config import scope_missing_ticker_error



def missing_file_event(scope, ticker):
	# There is no local file so record this fact
	# to prevent further attempts to load the local file

	scope.missing_tickers['local'].append(ticker)
	scope.missing_tickers['list'].append(ticker)

	# Cache Error
	if ticker not in scope.missing_tickers['errors']:
		scope_missing_ticker_error(scope, ticker)
	scope.missing_tickers['errors'][ticker]['load'] = 'Missing Local file'



