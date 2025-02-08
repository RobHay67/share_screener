import logging
from tickers.scope.model.scope_ticker_schema import scope_missing_ticker_error


def fail_local_load_event(scope, ticker):
	logging.error(f"fail_local_load_event {ticker=}")
	# There is no local file so record this fact
	# to prevent further attempts to load the local file

	scope.ticker_schema['missing']['local'].append(ticker)
	scope.ticker_schema['missing']['list'].append(ticker)

	# Cache Error
	if ticker not in scope.ticker_schema['missing']['errors']:
		scope_missing_ticker_error(scope, ticker)
	scope.ticker_schema['missing']['errors'][ticker]['load'] = 'Missing Local file'

	# Remove Ticker from Load list
	page=scope.display['page']
	scope.page[page]['list_load_tickers']

