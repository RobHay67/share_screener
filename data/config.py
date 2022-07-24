
from data.index.load import load_ticker_index_file


def scope_data(scope):

	scope.data = {}

	scope.data['ticker_index'] = {}	
	

	load_ticker_index_file(scope)
	# scope.initial_load = False			# Prevent session_state from re-running during its use

	# company names for the ticker search
	scope.data['ticker_search'] = {}
	scope.data['ticker_search'] = (scope.data['ticker_index']['company_name']).to_dict()


	# TODO - replace this with just the tickers
	scope.data['ticker_files'] = {}

	scope.data['tickers'] = {}





	scope.data['download'] 					= {}
	scope.data['download']['days'] 			= 7
	scope.data['download']['industries'] 	= ['random_tickers']

	scope.data['download']['yf_files']		= {}
	scope.data['download']['yf_anomolies'] 	= {}
	scope.data['download']['missing_list'] 	= []

	