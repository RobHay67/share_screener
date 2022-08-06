





def cache_ticker_file(scope,ticker, ticker_data_file):

	# Sort ticker file into ascending order
	ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)	
	
	
	# TODO tickers - delete
	scope.ticker_files[ticker] = ticker_data_file


	scope.tickers[ticker] = {}

	scope.tickers[ticker]['file'] = ticker_data_file

	scope.tickers[ticker]['replace_df'] = True
	scope.tickers[ticker]['replace_columns'] = True
