import pandas as pd
from tickers.scope.model.schema import ticker_file_usecols


def scope_download_variables(scope):
	scope.yf = {}
	scope.yf['periods']				= ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y']
	scope_yf_config(scope)
	scope_yf_batch_config(scope)


def scope_yf_config(scope):
	# seperate so it can be called at the begining of each download
	# All Downloaded ticker data (all batches) is tempporarily stored here
	scope.yf['all_data'] 	= pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		
	scope.yf['all_errors'] 	= {}


def scope_yf_batch_config(scope):
	# Reset back to these values after each download
	# Batch specific params and data is stored here
	scope.yf['batch_ticker_string']		= ''			# Using This
	scope.yf['batch_type']				= ''			# Using this in new one
	scope.yf['batch_data'] 				= {}			# Using this in new one
	scope.yf['batch_errors'] 			= {}			# We still get this so lets keep it
	
