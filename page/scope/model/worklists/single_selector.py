import logging

def single_selector_page(scope, page, ticker_list):
	logging.debug("single_selector_page")
	# one of the pages which allows for a single ticker to be selected
	ticker_list = []
	selected_ticker = scope.page[page]['selectors']['ticker']
	if selected_ticker != 'select a ticker' :
		ticker_list = [selected_ticker]
	return ticker_list

