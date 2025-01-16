import time
from app.scope.model.schema_page import page_schema


def scope_config(scope):

	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] 	= time.time()
	
	scope.config['page_schema'] = page_schema
	scope.config['page_list'] = list(scope.config['page_schema'].keys())
	user_config_pages(scope)

	scope.config['display_config_group'] = None

	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
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


def scope_seach_for_ticker(scope):
	# company names for the ticker search
	scope.config['ticker_search'] = {}
	scope.config['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()




