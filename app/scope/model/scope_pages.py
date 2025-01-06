

def scope_pages(scope):

	scope.pages = {}
	user_config_pages(scope)
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
								'testing',
								]
	scope.pages['ticker_values'] = ticker_value_schema
	scope.pages['render_config'] = None

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
		scope.pages[page]['worklist'] = []  			# formally known as scope.pages[page]['ticker_list']
		scope.pages[page]['worklist_long_desc'] = []
		scope.pages[page]['loaded_ticker_list'] = []		# list of every ticker loaded by this particular page - saves checking later

		scope.pages[page]['selectors'] = {
										'ticker'		: 'select a ticker',
										'tickers'		: [],
										'industries'	: [],
										'market'		: 'select market',
										'config_ticker'	: 'select a ticker',
										}
		
		scope.pages[page]['render'] = 	{
										'ticker_file':'Show/Hide Data',	# display the ticker files
										'page_config':False,			# display the application config
										'chart_settings':False,			# display the chart settings
										'overlay_settings':False,		# display the overlay settings
										'trial_settings':False,			# display the trial settings
										'strategy':False,				# display the strategy settings
										'ticker_config':False,			# display the ticker config
								}


def user_config_pages(scope):
	# These Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.pages['row_limit'] = 100
	scope.pages['display'] = 'streamlit_app'
	scope.pages['share_market'] = 'ASX'
	# scope.pages['share_market'] = 'USA'
	scope.pages['download_days'] = '5d'


def scope_ticker_search(scope):
	# company names for the ticker search
	scope.pages['ticker_search'] = {}
	scope.pages['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()



# ['open', 'high', 'low', 'close', 'volume']


ticker_value_schema = {
	'open'	:{'english':'Opening', 'long_english':'Opening Price'},
	'high'	:{'english':'Highest', 'long_english':'Highest Price'},
	'low'	:{'english':'Lowest', 'long_english':'Lowest Price'},
	'close'	:{'english':'Closing', 'long_english':'Closing Price'},
	'volume':{'english':'Volume', 'long_english':'Volume'},
}