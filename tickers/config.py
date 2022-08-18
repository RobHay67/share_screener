

def scope_ticker_files(scope):

	scope.tickers = {}

def scope_missing_tickers(scope):
	scope.missing_tickers = {}
	scope.missing_tickers['local'] = []
	scope.missing_tickers['cloud'] = []
	scope.missing_tickers['list']  = []


def scope_download_variables(scope):

	scope.download 					= {}
	base_config_download(scope)
	scope.download['industry_groups'] 	= ['random_tickers']
	scope.download['yf_files']		= {}
	scope.download['yf_anomolies'] 	= {}



def base_config_download(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.download['days'] 			= 7


