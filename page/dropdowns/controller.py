
from page.dropdowns.markets import build_list_of_markets
from page.dropdowns.industries import build_list_of_industries
from page.dropdowns.tickers import build_list_of_tickers

def refresh_ticker_selector_lists(scope):
	# Repopulate the scope with the latest information for the dropdown lists
	# THis function only needs running after the ticker index has been loaded/downloaded

	build_list_of_markets(scope)
	build_list_of_industries(scope)
	build_list_of_tickers(scope)

	
	#
	

	





