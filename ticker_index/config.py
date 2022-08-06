

from ticker_index.load import load_ticker_index_file


def scope_index_file(scope):

	scope.ticker_index = {}	

	load_ticker_index_file(scope)




