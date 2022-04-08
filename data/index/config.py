
from data.index.load import load_ticker_index_file


def scope_index(scope):
	scope.data['ticker_index'] = {}			
	load_ticker_index_file(scope)



