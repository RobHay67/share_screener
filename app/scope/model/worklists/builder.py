from app.scope.model.worklists.single_selector import single_selector_page
from app.scope.model.worklists.multi_selector import multi_selector_page
from app.scope.model.worklists.long_desc import refresh_worklist_long_description


def refresh_page_worklist(scope):
	
	# Create a ticker list based on what has been chosen in the Page Selectors
	# most detailed/largest selection takes precedence 
	#  	ie industry selection trumps a single ticker selection
	# note that 'random_tickers' is the default for industry_list (special codes runs off this)
	
	page = scope.pages['display']
	
	# Default Values
	ticker_list = []

	if page != 'screener':
		ticker_list = single_selector_page(scope, page, ticker_list)
	
	if page == 'screener':
		ticker_list = multi_selector_page(scope, ticker_list)
		
	# Store the Worklist
	ticker_list.sort()
	scope.pages[page]['worklist'] = ticker_list

	refresh_worklist_long_description(scope)














