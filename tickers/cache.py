

def cache_ticker_file(scope,ticker, ticker_data_file):
	print('cache_ticker_file')

	# Sort ticker file into ascending order
	ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)	

	# New Method for storing the ticker information
	scope.tickers[ticker] = {}
	scope.tickers[ticker]['df'] = ticker_data_file
	scope.tickers[ticker]['replace_app_dfs'] = True
