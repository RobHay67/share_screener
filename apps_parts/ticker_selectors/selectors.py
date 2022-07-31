from widgets.ticker import select_a_ticker
from widgets.search import search_ticker_by_name

from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers


from apps_parts.ticker_selectors.ticker_list import update_ticker_list


def render_ticker_selectors(scope):

	app = scope.apps['display_app']

	if app != 'screener':
		# One of the Single Ticker Pages - Single / Volume / Research or Intra-Day

		with scope.col1: 
			select_a_ticker(scope)
			search_ticker_by_name(scope)
	
	if app == 'screener':	
		# Screener app (Potentially Multiple Tickers depending on the dropdown selections)
		
		with scope.col1: select_tickers(scope)
		with scope.col1: search_ticker_by_name(scope)
		with scope.col2: select_industries(scope)
		with scope.col2: select_a_market(scope)

	selected_tickers_status = update_ticker_list(scope)

	return selected_tickers_status



