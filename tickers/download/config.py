
import pandas as pd
from tickers.schema import ticker_file_usecols




def scope_download_variables(scope):
	scope.download = {}
	base_config_download(scope)
	reset_yf_download_config(scope)


def reset_yf_download_config(scope):
	# Reset back to these values after each download
	scope.download['yf_download_these_industries'] = ['random_tickers']
	# Batch specific params and data is stored here
	scope.download['yf_batch_no']		= 0
	scope.download['yf_batch_industry']	= ''
	scope.download['yf_batch_ticker_string']	= ''
	scope.download['yf_batch_type']	= ''
	scope.download['yf_batch_data'] = {}
	scope.download['yf_batch_errors'] = {}
	# Entire Download run is stored here
	scope.download['yf_ticker_list'] 	= []	
	scope.download['yf_data'] 			= pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		
	scope.download['yf_errors'] 		=  {}


def base_config_download(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.download['days'] = 7
	set_yf_period(scope)

	


def set_yf_period(scope):
	# set appropriate period for YF download
	# valid periods = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
	scope.download['yf_period'] = str(int(scope.download['days'])) + 'd' 




