import logging
from page.worklists.single_selector import page_with_single_selector
from page.worklists.multi_selector import page_with_multiple_selectors
from page.worklists.long_desc import build_worklist_with_long_description

def build_list_of_selected_tickers_for_page(scope):
	logging.debug("build_list_of_selected_tickers_for_page")
	# Create a ticker list based on what has been chosen in the Page Selectors
	# most detailed/largest selection takes precedence 
	#  	ie industry selection trumps a single ticker selection
	# note that 'random_tickers' is the default for industry_list (special codes runs off this)
	
	page = scope.display['page']
	
	# Default Values
	ticker_list = []

	match page:
		case 'screener':
			ticker_list = page_with_multiple_selectors(scope, ticker_list)
		case _:
			ticker_list = page_with_single_selector(scope, page, ticker_list)	
	
	# Store the ticker_list in the Page selected_tickers
	ticker_list.sort()
	scope.page[page]['selected_tickers'] = ticker_list
	build_worklist_with_long_description(scope)














