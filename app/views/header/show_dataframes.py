from tickers.scope.view.dataframes import show_page_dataframes

def show_dataframes(scope):
	page = scope.config['display']
	if scope.page[page]['render']['ticker_file'] != 'Show/Hide Data':
		show_page_dataframes(scope)