from tickers.scope.model.scope_ticker_schema import scope_missing_ticker_error


def fail_download_event(scope, ticker, zero_volume=False):

	# So the download has failed and we need to update the 
	# missing tickers list
	
	if ticker not in scope.ticker_schema['missing']['cloud']:
		scope.ticker_schema['missing']['cloud'].append(ticker)	
	
	# however, we may still have local data for this ticker which 
	# overrides the need to store this status in the total list

	if ticker not in scope.ticker_schema['missing']['list']:
		scope.ticker_schema['missing']['list'].append(ticker)

	# Cache Download Error
	if ticker not in scope.ticker_schema['missing']['errors']:
		scope_missing_ticker_error(scope, ticker)

	if zero_volume:
		error_message = 'Zero volume - no trading activity'
	else:
		error_message = scope.yf['all_errors'][ticker]

	scope.ticker_schema['missing']['errors'][ticker]['yf'] = error_message




