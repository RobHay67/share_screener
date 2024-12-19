




def create_ticker_list_to_load(scope):

	page = scope.pages['display']
	already_loaded_list = list(scope.tickers.keys())

	list_of_tickers_to_load = []

	for ticker in scope.pages[page]['worklist']:
		if ticker not in scope.tickers_missing['local']:
			if ticker not in already_loaded_list:
				list_of_tickers_to_load.append(ticker)

	return list_of_tickers_to_load