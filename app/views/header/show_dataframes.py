from tickers.scope.view.dataframes import show_page_dataframes

def show_dataframes(scope):
	page = scope.pages['display']
	if scope.pages[page]['render']['ticker_file'] != 'Show/Hide Data':
		show_page_dataframes(scope)