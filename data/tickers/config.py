



def scope_ticker_files(scope):


	# TODO - replace this with just the tickers
	scope.data['ticker_files'] = {}

	scope.data['tickers'] = {}


def scope_download_variables(scope):

	scope.data['download'] 					= {}
	scope.data['download']['days'] 			= 7
	scope.data['download']['industries'] 	= ['random_tickers']

	scope.data['download']['yf_files']		= {}
	scope.data['download']['yf_anomolies'] 	= {}
	scope.data['download']['missing_list'] 	= []