

import pandas as pd
from tickers.schema import ticker_file_usecols



def scope_download_variables(scope):
	scope.yf = {}
	scope_yf_config(scope)


def scope_yf_config(scope):
	# Reset back to these values after each download
	# scope.yf['download_these_industries'] = ['random_tickers']
	# Batch specific params and data is stored here
	# scope.yf['batch_no']				= 0	
	# scope.yf['batch_industry']			= ''
	scope.yf['batch_ticker_string']		= ''			# Using This
	scope.yf['batch_type']				= ''			# Using this in new one
	scope.yf['batch_data'] 				= {}			# Using this in new one
	scope.yf['batch_errors'] 			= {}			# We still get this so lets keep it
	# Entire Download run is stored here
	# scope.yf['ticker_list'] 			= []	
	scope.yf['data'] 					= pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		
	scope.yf['errors'] 					= {}
	scope.yf['intervals']				= ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y']
	scope.yf['downloaded_data']			= False

