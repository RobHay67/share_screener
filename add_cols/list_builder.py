


def create_list_of_tickers_to_add_columns(scope, page):

	list_of_tickers_to_add_columns= []

	for ticker in scope.page[page]['worklist']:
		# Ensure ticker data available otherwise
		# function will fail on missing columns
		if ticker in list(scope.tickers.keys()): 
			list_of_tickers_to_add_columns.append(ticker)

	return list_of_tickers_to_add_columns


