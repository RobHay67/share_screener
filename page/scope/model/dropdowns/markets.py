import logging
from markets.schema import markets


def build_market_dropdown_list(scope):
	logging.debug("build_market_dropdown_list")
	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, 'select market')
	scope.config['dropdowns']['markets'] = list_of_markets