import logging
import pandas as pd


def consolidate_downloaded_ticker_data(scope):
	logging.debug("consolidate_downloaded_ticker_data")
	# Add the batch data to the yf['data'] object
	# 	- essentially add all batches together for
	# 		later processing
	
	# Amalgamate the downloaded BATCH data for later processing
	if not scope.yf['all_data'].empty:
		# Future Warning : concat does not work with empty dataframes
		scope.yf['all_data'] = pd.concat([scope.yf['all_data'], scope.yf['batch_data']], sort=False)
	else:
		scope.yf['all_data'] = scope.yf['batch_data'].copy()

	# Amalgamate the download BATCH errors for later reporting
	scope.yf['all_errors'].update(scope.yf['batch_errors'])


