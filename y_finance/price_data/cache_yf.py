import pandas as pd


def cache_yf_batch_data(scope):

	# cache a list of tickers for later reporting
	yf_ticker_list = scope.yf['batch_ticker_string'].split(' ')
	scope.yf['ticker_list'].extend(yf_ticker_list)
	
	# cache the downloaded data for later processing and reporting
	scope.yf['data'] = pd.concat([scope.yf['data'], scope.yf['batch_data']], sort=False)

	# cache the download errors for later reporting
	scope.yf['errors'].update(scope.yf['batch_errors'])


