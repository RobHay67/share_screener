import logging
import time
from page.scope.schema import page_schema
from config.schemas.external_links import external_links
from config.schemas.markets import markets, public_holidays, opening_hours
from config.scope.dropdowns.markets import build_market_dropdown_list
from config.scope.dropdowns.industries import build_industry_dropdown_list
from config.scope.dropdowns.tickers import build_ticker_dropdown_list

def scope_config(scope):
	logging.warning("scope_config ==========================================")
	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] 	= time.time()
	
	# Schemas (General Config)
	scope.config['page_schema'] = page_schema
	scope.config['external_links'] = external_links
	scope.config['markets'] = markets
	scope.config['public_holidays'] = public_holidays
	scope.config['opening_hours'] = opening_hours

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
	logging.warning("scope_config_for_users_settings")
	# These Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.config['row_limit'] = 100
	scope.config['share_market'] = 'ASX' # 'USA'
	scope.config['download_days'] = '5d'


def scope_ticker_search(scope):
	logging.warning("scope_ticker_search")
	# company names for the ticker search
	scope.config['ticker_search'] = {}
	scope.config['ticker_search'] = (scope.ticker_index['df']['company_name']).to_dict()


def scope_dropdown_lists(scope):
	build_market_dropdown_list(scope)
	build_industry_dropdown_list(scope)
	build_ticker_dropdown_list(scope)



