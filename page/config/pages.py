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

	
	# ==========================================
	# variables for each page from the page list above
	for page in scope.pages['page_list']:
		scope.pages[page] = {}
		scope.pages[page]['search_results'] = {}
		scope.pages[page]['worklist'] = []  # formally known as scope.pages[page]['ticker_list']
		scope.pages[page]['worklist_dropdown'] = []
		scope.pages[page]['tickers_used_by_page'] = []
		
		scope.pages[page]['selectors'] = {
										'ticker'	: 'select a ticker',
										'tickers'	: [],
										'industries': [],
										'market'	: 'select market', 
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
