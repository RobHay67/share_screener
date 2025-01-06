


def build_ticker_dropdown_list(scope):
	list_of_tickers = scope.ticker_index['df'].index.values.tolist()
	scope.pages['dropdowns']['tickers'] = list_of_tickers.copy()

	list_of_tickers.insert(0, 'select a ticker')
	scope.pages['dropdowns']['ticker'] = list_of_tickers.copy()
	