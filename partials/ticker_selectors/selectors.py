from widgets.ticker import select_a_ticker
from widgets.search import search_ticker_by_name

from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers


from partials.ticker_selectors.ticker_list import update_ticker_list


def render_ticker_selectors(scope):

	app = scope.apps['display_app']

	with scope.col1: 
		search_ticker_by_name(scope)

	if app != 'screener':
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay

		with scope.col2:
			select_a_ticker(scope)
	
	if app == 'screener':	
		# Screener app (Potentially Multiple Tickers depending on the dropdown selections)
		
		with scope.col2: 
			select_tickers(scope)
		with scope.col2: 
			select_industries(scope)
		with scope.col2: 
			select_a_market(scope)

	we_have_selected_tickers = update_ticker_list(scope)

	return we_have_selected_tickers

