from markets.model.set_market import select_a_market
from markets.model.set_industries import select_industries
from picker.model.set_tickers import select_tickers
from picker.model.set_ticker import select_a_ticker
from data.tickers.model.set_multi_ticker_list import update_multi_ticker_list


# TODO ticker_list st

def ticker_selectors(scope,page):
	
	selected_tickers_so_lets_load = False
	ticker_list = []

	if page != 'screener':
		# One of the Single Ticker Pages - Single / Volume / Research

		with scope.col1: select_a_ticker(scope, page)

		ticker = scope.pages[page]['ticker_list'][0]

		if ticker != 'select a ticker':	
			selected_tickers_so_lets_load = True
			scope.data['download']['industries'] = ['random_tickers']									# used for y_finance downloading
			# ticker_list = [scope.pages[page]['ticker_list'][0]]
	else:	
		# Screener Page (Potentially Multiple Tickers)
		
		with scope.col1: select_tickers(scope)
		with scope.col2: select_industries(scope)
		with scope.col2: select_a_market(scope)

		market 		= scope.pages['screener']['market'] != 'select entire market'
		industries 	= len(scope.pages['screener']['industries']) != 0
		tickers 	= len(scope.pages['screener']['tickers']) != 0

		if market or industries or tickers: 
			selected_tickers_so_lets_load = True
			update_multi_ticker_list(scope)													# scope.data['download']['industries'] is establised by this function
			# ticker_list = scope.pages['screener']['ticker_list']

	# TODO - we should store the ticker_list in the scope[page][ticker_list] object


	return selected_tickers_so_lets_load