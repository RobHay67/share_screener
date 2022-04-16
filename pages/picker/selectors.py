from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers
from widgets.ticker import select_a_ticker

from pages.picker.ticker_list import create_screener_ticker_list, create_ticker_list


# from pages.picker.ticker_list import create_screener_ticker_list


def render_selectors(scope):

	page = scope.pages['display_page']
	
	selected_tickers_status = False

	if page != 'screener':
		# One of the Single Ticker Pages - Single / Volume / Research or Intra-Day

		with scope.col1: select_a_ticker(scope)

		ticker = scope.pages[page]['selectors']['ticker']

		if ticker != 'select a ticker' :
			selected_tickers_status = True
			create_ticker_list(scope, ticker)
						
	
	if page == 'screener':	
		# Screener Page (Potentially Multiple Tickers depending on the dropdown selections)
		
		with scope.col1: select_tickers(scope)
		with scope.col2: select_industries(scope)
		with scope.col2: select_a_market(scope)

		market 		= scope.pages['screener']['selectors']['market'] != 'select entire market'
		industries 	= len(scope.pages['screener']['selectors']['industries']) != 0
		tickers 	= len(scope.pages['screener']['selectors']['tickers']) != 0
		

		if market or industries or tickers: 
			selected_tickers_status = True
			create_screener_ticker_list(scope)

	return selected_tickers_status



