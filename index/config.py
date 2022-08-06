

from index.load import load_ticker_index_file


def scope_index_file(scope):

	scope.ticker_index = {}	

	load_ticker_index_file(scope)



def scope_ticker_search(scope):

	# company names for the ticker search
	scope.ticker_search = {}
	scope.ticker_search = (scope.ticker_index['company_name']).to_dict()
