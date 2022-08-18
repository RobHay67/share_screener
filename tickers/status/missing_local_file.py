




def set_missing_status(scope, ticker):
	# There is no local file so record this fact
	# to prevent further attempts to load the local file

	scope.missing_tickers['local'].append(ticker)
	scope.missing_tickers['list'].append(ticker)


	# scope.download['missing_list'].append(ticker)