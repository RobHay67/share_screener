import logging
import time
from page.scope.model.schema import page_schema


def scope_config(scope):
	logging.debug("scope_config")
	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] 	= time.time()
	
	scope.config['page_schema'] = page_schema
	scope.config['page_list'] = list(scope.config['page_schema'].keys())
	scope_config_for_users_settings(scope)

	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['ohlcv_columns'] = ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	


def scope_config_for_users_settings(scope):
	logging.debug("scope_config_for_users_settings")
	# These Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.config['row_limit'] = 100
	scope.config['share_market'] = 'ASX'
	# scope.config['share_market'] = 'USA'
	scope.config['download_days'] = '5d'


def scope_seach_for_ticker(scope):
	logging.debug("scope_seach_for_ticker")
	# company names for the ticker search
	scope.config['ticker_search'] = {}
	scope.config['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()




