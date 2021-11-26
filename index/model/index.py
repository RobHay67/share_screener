from index.model.load import load_ticker_index_file


def scope_index(scope):
	# Primary Application Objects
	scope.ticker_index = {}						# was previous ticker_index_file
	load_ticker_index_file(scope)





