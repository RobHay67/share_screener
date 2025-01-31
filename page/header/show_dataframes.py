import logging
from tickers.scope.view.dataframes import show_page_dataframes

def show_dataframes(scope):
	logging.debug("show_dataframes")
	page = scope.display['page']
	if scope.page[page]['show']['ticker_file'] != 'Show/Hide Data':
		show_page_dataframes(scope)