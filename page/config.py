# from trials.config import trials_config
# from charts.config import charts_config


def scope_pages(scope):

	scope.pages = {}
	base_config_pages(scope)
	scope.pages['button_for_scope'] = None
	scope.pages['page_list'] = [ 
								'chart', 
								'intraday', 
								'volume', 
								'research', 
								'screener', 
								'websites', 
								'ticker_index', 
								'config',
								'logout',
								]

	# Dropdowns
	scope.pages['dropdowns'] = {}
	scope.pages['dropdowns']['markets'] = []
	scope.pages['dropdowns']['industries'] = []
	scope.pages['dropdowns']['tickers'] = []
	scope.pages['dropdowns']['ticker'] = []
	scope.pages['dropdowns']['config_ticker'] = ['select a ticker']
	scope.pages['dropdowns']['ohlcv_columns'] = ['open', 'high', 'low', 'close', 'volume']
	scope.pages['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	


	# ==========================================
	# variables for each page from the page list above
	for page in scope.pages['page_list']:
		scope.pages[page] = {}
		scope.pages[page]['search_results'] = {}
		scope.pages[page]['worklist'] = []  # formally known as scope.pages[page]['ticker_list']
		scope.pages[page]['worklist_dropdown'] = []
		scope.pages[page]['tickers_used_by_page'] = []
		
		scope.pages[page]['selectors'] = {
										'ticker'		: 'select a ticker',
										'tickers'		: [],
										'industries'	: [],
										'market'		: 'select market',
										'config_ticker'	: 'select a ticker',
										}
		
		scope.pages[page]['render'] = 	{
										'ticker_file':'Show/Hide Data',	# display the ticker files
										'app_config':False,				# display the application config
										'chart_settings':False,			# display the chart settings
										'overlay_settings':False,		# display the overlay settings
										'trial_settings':False,			# display the trial settings
										'strategy':False,				# display the strategy settings
								}


def base_config_pages(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.pages['row_limit'] = 100
	scope.pages['display'] = 'home'
	scope.pages['share_market'] = 'ASX'
	scope.pages['download_days'] = 7


def scope_ticker_search(scope):
	# company names for the ticker search
	scope.pages['ticker_search'] = {}
	scope.pages['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()
