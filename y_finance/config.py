

import pandas as pd
from tickers.schema import ticker_file_usecols



def scope_download_variables(scope):
	scope.yf = {}
	scope_yf_config(scope)


def scope_yf_config(scope):
	# Reset back to these values after each download
	scope.yf['download_these_industries'] = ['random_tickers']
	# Batch specific params and data is stored here
	scope.yf['batch_no']				= 0
	scope.yf['batch_industry']			= ''
	scope.yf['batch_ticker_string']		= ''
	scope.yf['batch_type']				= ''
	scope.yf['batch_data'] 				= {}
	scope.yf['batch_errors'] 			= {}
	# Entire Download run is stored here
	scope.yf['ticker_list'] 			= []	
	scope.yf['data'] 					= pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		
	scope.yf['errors'] 					=  {}
	scope.yf['interval']				= ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y']

