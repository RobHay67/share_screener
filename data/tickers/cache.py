





def cache_ticker_file(scope,ticker, ticker_data_file):

	# Sort ticker file into ascending order
	ticker_data_file.sort_values(by=['date'], inplace=True, ascending=False)	
	
	
	# TODO tickers - delete
	scope.data['ticker_files'][ticker] = ticker_data_file


	scope.data['tickers'][ticker] = {}

	scope.data['tickers'][ticker]['file'] = ticker_data_file

	scope.data['tickers'][ticker]['replace_df'] = True
	scope.data['tickers'][ticker]['replace_columns'] = True
