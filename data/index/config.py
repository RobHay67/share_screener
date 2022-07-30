

from data.index.load import load_ticker_index_file


def scope_index_file(scope):

	scope.data['ticker_index'] = {}	

	load_ticker_index_file(scope)



def scope_ticker_search(scope):

	# company names for the ticker search
	scope.data['ticker_search'] = {}
	scope.data['ticker_search'] = (scope.data['ticker_index']['company_name']).to_dict()
