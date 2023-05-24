

import pandas as pd
from tickers.schema import ticker_file_usecols



def scope_download_variables(scope):
	scope.yf = {}
	scope_yf_config(scope)
	set_yf_period(scope)



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


def set_yf_period(scope):
	
	# set appropriate period for YF download
	# valid periods = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
	scope.yf['period'] = str(int(scope.pages['download_days'])) + 'd' 

	# Setting can be changed for each user - so called by the restore user code

