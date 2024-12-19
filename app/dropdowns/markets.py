
from markets.schema import markets

def build_list_of_markets(scope):

	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, 'select market')
	scope.pages['dropdowns']['markets'] = list_of_markets