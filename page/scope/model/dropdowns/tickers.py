import logging


def build_ticker_dropdown_list(scope):
	logging.debug("build_ticker_dropdown_list")
	list_of_tickers = scope.ticker_index['df'].index.values.tolist()
	scope.config['dropdowns']['tickers'] = list_of_tickers.copy()

	list_of_tickers.insert(0, 'select a ticker')
	scope.config['dropdowns']['ticker'] = list_of_tickers.copy()
	