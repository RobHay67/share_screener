from config.model.set_market import select_a_market
from config.model.set_industries import select_industries
from config.model.set_tickers import select_tickers
from config.model.set_ticker import select_a_ticker
from config.model.multi_ticker_list import update_multi_ticker_list



def ticker_selectors(scope,page):
	
	we_are_loading = False
	ticker_list = []

	if page != 'multi':
		with scope.col1: select_a_ticker(scope, page)

		ticker = scope.pages[page]['ticker_list'][0]

		if ticker != 'select a ticker':	
			we_are_loading = True
			scope.download_industries = ['random_tickers']									# used for y_finance downloading
			ticker_list = [scope.pages[page]['ticker_list'][0]]
	else:	# Multi Ticker Selectors Required
		with scope.col1: select_tickers(scope)
		with scope.col2: select_industries(scope)
		with scope.col2: select_a_market(scope)

		market 		= scope.pages['multi']['market'] != 'select entire market'
		industries 	= len(scope.pages['multi']['industries']) != 0
		tickers 	= len(scope.pages['multi']['tickers']) != 0

		if market or industries or tickers: 
			we_are_loading = True
			update_multi_ticker_list(scope)													# scope.download_industries is establised by this function
			ticker_list = scope.pages['multi']['ticker_list']


	return we_are_loading, ticker_list