import logging


def reset_page_to_default_values(scope):
	logging.warning("reset_page_to_default_values")
	
	# Single pgae show settings
	scope.ticker_index['show']['industry_report'] = False

	for page in scope.config['page_list']:
		
		scope.page[page]['show']['trials'] 		= False
		scope.page[page]['show']['strategy'] 	= False
		scope.page[page]['show']['charts'] 		= False
		scope.page[page]['show']['overlays'] 	= False
		scope.page[page]['show']['config'] 		= None
		scope.page[page]['show']['ticker_file'] = 'Show/Hide Data'

		scope.page[page]['search_results'] 		= {}

		# Reset the ticker selectors
		scope.page[page]['selectors']['ticker'] = None
		scope.page[page]['selectors']['tickers'] = []
		scope.page[page]['selectors']['industries'] = []
		scope.page[page]['selectors']['market'] = None
		scope.page[page]['list_selected_tickers'] = []
