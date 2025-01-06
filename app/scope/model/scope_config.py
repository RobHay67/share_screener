import time

def scope_config(scope):

	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] 	= time.time()
	
	user_config_pages(scope)
	scope.config['page_list'] = [ 
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
	scope.config['ticker_values'] = ticker_value_schema
	scope.config['display_config_group'] = None

	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['config_ticker'] = ['select a ticker']
	scope.config['dropdowns']['ohlcv_columns'] = ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	


def user_config_pages(scope):
	# These Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.config['row_limit'] = 100
	scope.config['display'] = 'streamlit_app'
	scope.config['share_market'] = 'ASX'
	# scope.config['share_market'] = 'USA'
	scope.config['download_days'] = '5d'


def scope_ticker_search(scope):
	# company names for the ticker search
	scope.config['ticker_search'] = {}
	scope.config['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()



# ['open', 'high', 'low', 'close', 'volume']


ticker_value_schema = {
	'open'	:{'english':'Opening', 'long_english':'Opening Price'},
	'high'	:{'english':'Highest', 'long_english':'Highest Price'},
	'low'	:{'english':'Lowest', 'long_english':'Lowest Price'},
	'close'	:{'english':'Closing', 'long_english':'Closing Price'},
	'volume':{'english':'Volume', 'long_english':'Volume'},
}