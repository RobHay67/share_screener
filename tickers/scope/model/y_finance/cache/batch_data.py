
import pandas as pd



def cache_batch_data(scope):

	# Add the batch data to the yf['data'] object
	# 	- essentially add all batches together for
	# 		later process
	
	# Amalgamate the downloaded BATCH data for later processing
	scope.yf['data'] = pd.concat([scope.yf['data'], scope.yf['batch_data']], sort=False)

	# Amalgamate the download BATCH errors for later reporting
	scope.yf['errors'].update(scope.yf['batch_errors'])



