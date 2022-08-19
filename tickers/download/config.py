
import pandas as pd
from tickers.schema import ticker_file_usecols




def scope_download_variables(scope):
	scope.download = {}
	base_config_download(scope)
	reset_yf_download_config(scope)


def reset_yf_download_config(scope):
	# Reset back to these values after each download
	scope.download['yf_industry_groups'] = ['random_tickers']
	scope.download['yf_ticker_string']	= ''
	scope.download['yf_schema']			= ''
	scope.download['yf_ticker_list'] 	= []
	scope.download['yf_data'] 			= pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		
	scope.download['yf_errors'] 		=  {}


def base_config_download(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.download['days'] = 7





