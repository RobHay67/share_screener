import logging


def build_ticker_dropdown_list(scope):
	logging.warning("build_ticker_dropdown_list")
	list_of_tickers = scope.ticker_index['df'].index.values.tolist()
	scope.config['dropdowns']['tickers'] = list_of_tickers.copy()
	scope.config['dropdowns']['ticker'] = list_of_tickers.copy()
	