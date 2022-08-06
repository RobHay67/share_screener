



def scope_ticker_files(scope):


	# TODO - replace this with just the tickers
	scope.ticker_files = {}
	scope.tickers = {}


def scope_download_variables(scope):

	scope.download 					= {}
	scope.download['days'] 			= 7
	scope.download['industries'] 	= ['random_tickers']

	scope.download['yf_files']		= {}
	scope.download['yf_anomolies'] 	= {}
	scope.download['missing_list'] 	= []