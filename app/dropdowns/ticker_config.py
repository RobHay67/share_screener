


def refresh_ticker_dropdown_for_config(scope):
	list_of_loaded_tickers = list(scope.tickers.keys())
	list_of_loaded_tickers.insert(0, 'select a ticker')
	scope.pages['dropdowns']['config_ticker'] = list_of_loaded_tickers.copy()