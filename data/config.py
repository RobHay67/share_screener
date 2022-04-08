


# from data.index.config import scope_index
from data.index.load import load_ticker_index_file
# from data.tickers.config import scope_tickers
# from data.tickers.config import scope_download

def scope_data(scope):

	scope.data = {}

	# scope_index(scope)
	scope.data['ticker_index'] = {}			
	load_ticker_index_file(scope)
	scope.initial_load = False			# Prevent session_state from re-running during its use



	scope.data['ticker_files'] = {}

	# scope_download(scope)
# def scope_download(scope):
	scope.data['download'] 					= {}
	scope.data['download']['days'] 			= 7
	scope.data['download']['industries'] 	= []

	scope.data['download']['yf_files']		= {}
	scope.data['download']['yf_anomolies'] 	= {}
	scope.data['download']['missing_list'] 	= []









def scope_index(scope):
	scope.data['ticker_index'] = {}			
	load_ticker_index_file(scope)