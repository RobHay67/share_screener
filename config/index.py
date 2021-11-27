
from index.model.load import load_ticker_index_file


def scope_index(scope):
	scope.ticker_index = {}			
	load_ticker_index_file(scope)



