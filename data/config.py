
from data.index.load import load_ticker_index_file


def scope_data(scope):

	scope.data = {}

	scope.data['ticker_index'] = {}			
	load_ticker_index_file(scope)
	scope.initial_load = False			# Prevent session_state from re-running during its use


	scope.data['ticker_files'] = {}


	scope.data['download'] 					= {}
	scope.data['download']['days'] 			= 7
	scope.data['download']['industries'] 	= ['random_tickers']

	scope.data['download']['yf_files']		= {}
	scope.data['download']['yf_anomolies'] 	= {}
	scope.data['download']['missing_list'] 	= []

