
from page.scope.model.dropdowns.markets import build_market_dropdown_list
from page.scope.model.dropdowns.industries import build_inductry_dropdown_list
from page.scope.model.dropdowns.tickers import build_ticker_dropdown_list

def refresh_ticker_selector_lists(scope):
	# Repopulate the scope with the latest information for the dropdown lists
	# THis function only needs running after the ticker index has been loaded/downloaded

	build_market_dropdown_list(scope)
	build_inductry_dropdown_list(scope)
	build_ticker_dropdown_list(scope)

	
	#
	

	





