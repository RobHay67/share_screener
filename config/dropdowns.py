

from config.markets.config import markets



def refresh_dropdown_lists(scope):
	# print ( '\033[91m' + 'Dropdown Lists have been repopulated' + '\033[0m' )

	# Repopulate the scope with the latest information for the dropdown lists
	# THis function should only be run after the ticker index has been loaded

	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, 'select entire market')
	scope.config['dropdowns']['markets'] = list_of_markets
	
	list_of_industries = scope.data['ticker_index']['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.config['dropdowns']['industries'] = list_of_industries
	
	list_of_tickers = scope.data['ticker_index'].index.values.tolist()
	scope.config['dropdowns']['tickers'] = list_of_tickers

	alt_ticker_list = scope.data['ticker_index'].index.values.tolist()
	alt_ticker_list.insert(0, 'select a ticker')
	scope.config['dropdowns']['ticker'] = alt_ticker_list
	
	

