import logging

def create_ticker_list_to_load(scope):
	logging.debug("create_ticker_list_to_load")
	page = scope.display['page']
	already_loaded_list = list(scope.tickers.keys())

	list_of_tickers_to_load = []
	for ticker in scope.page[page]['selected_tickers']:
		if ticker not in scope.ticker_schema['missing']['local']:
			if ticker not in already_loaded_list:
				list_of_tickers_to_load.append(ticker)
	return list_of_tickers_to_load