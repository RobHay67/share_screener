
from tickers.config import scope_missing_ticker_error


def fail_download_event(scope, ticker, zero_volume=False):

	# SO the download has failed and we need to update the 
	# missing_tickers list
	
	if ticker not in scope.missing_tickers['cloud']:
		scope.missing_tickers['cloud'].append(ticker)	
	

	# however, we may still have local data for this ticker which 
	# overrides the need to store this status in the total list

	if ticker not in scope.missing_tickers['list']:
		scope.missing_tickers['list'].append(ticker)


	# Cache Download Error
	if ticker not in scope.missing_tickers['errors']:
		scope_missing_ticker_error(scope, ticker)

	if zero_volume:
		error_message = 'Zero volume - no trading activity'
	else:
		error_message = scope.download['yf_errors'][ticker]

	scope.missing_tickers['errors'][ticker]['yf'] = error_message


def download_data_event(scope, ticker):
	# we may not have had any local data (ie its a new ticker)
	# so we need to reset the local load status and change
	# the overall status


	if ticker in scope.missing_tickers['local']:
		scope.missing_tickers['local'].remove(ticker)
	
	if ticker in scope.missing_tickers['cloud']:
		scope.missing_tickers['cloud'].remove(ticker)

	if ticker in scope.missing_tickers['list']:
		scope.missing_tickers['list'].remove(ticker)

