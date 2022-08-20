


def set_download_failure_status(scope, ticker):

	# SO the download has failed and we need to update the missing_tickers list
	scope.missing_tickers['cloud'].append(ticker)
	# if ticker not in scope.missing_tickers['list']:
	
	
	# however, we may still have local data for this ticker which 
	# overrides the need to store this status in the total list

	if ticker not in scope.missing_tickers['list']:
		scope.missing_tickers['list'].append(ticker)



def set_download_new_data_status(scope, ticker):
	# we may not have had any local data (ie its a new ticker)
	# so we need to rest the local load status and change
	# the overall status


	if ticker in scope.missing_tickers['local']:
		scope.missing_tickers['local'].remove(ticker)

	if ticker in scope.missing_tickers['list']:
		scope.missing_tickers['list'].remove(ticker)
