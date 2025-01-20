from tickers.scope.model.scope_ticker_config import scope_missing_ticker_error


def fail_local_load_event(scope, ticker):
	# There is no local file so record this fact
	# to prevent further attempts to load the local file

	scope.ticker_config['missing']['local'].append(ticker)
	scope.ticker_config['missing']['list'].append(ticker)

	# Cache Error
	if ticker not in scope.ticker_config['missing']['errors']:
		scope_missing_ticker_error(scope, ticker)
	scope.ticker_config['missing']['errors'][ticker]['load'] = 'Missing Local file'



