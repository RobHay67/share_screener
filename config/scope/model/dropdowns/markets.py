import logging
from markets.schema import markets


def build_market_dropdown_list(scope):
	logging.warning("build_market_dropdown_list")
	list_of_markets = list(markets.keys())
	scope.config['dropdowns']['markets'] = list_of_markets