import pandas as pd


def cache_yf_batch_data(scope):

	# cache a list of tickers for later reporting
	yf_ticker_list = scope.download['yf_batch_ticker_string'].split(' ')
	scope.download['yf_ticker_list'].extend(yf_ticker_list)
	
	# cache the downloaded data for later processing and reporting
	scope.download['yf_data'] = pd.concat([scope.download['yf_data'], scope.download['yf_batch_data']], sort=False)

	# cache the download errors for later reporting
	scope.download['yf_errors'].update(scope.download['yf_batch_errors'])


