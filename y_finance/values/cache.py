import pandas as pd
from tickers.schema import ticker_file_usecols
from tickers.missing_tickers.lists import update_missing_ticker_lists
from tickers.new import add_new_ticker
from tickers.missing_tickers.failed_download import fail_download_event



def cache_batch_data(scope):

	# Add the batch data to the yf['data'] object
	# 	- essentially add all batches together for
	# 		later process

	# cache a list of tickers for later reporting
	yf_ticker_list = scope.yf['batch_ticker_string'].split(' ')
	scope.yf['ticker_list'].extend(yf_ticker_list)
	
	# cache the downloaded data for later processing and reporting
	scope.yf['data'] = pd.concat([scope.yf['data'], scope.yf['batch_data']], sort=False)

	# cache the download errors for later reporting
	scope.yf['errors'].update(scope.yf['batch_errors'])


def cache_entire_download(scope):
	# concatenates any downloaded data with any loaded data 
	# resulting in a complete (hopefully) temporal transaction history for a ticker

	page = scope.pages['display']


	# iterate through the target tickers for the Page
	for ticker in scope.pages[page]['worklist']:
				
		if ticker in scope.yf['data']['ticker'].unique():
			# we appear to have downloaded data (we may have nothing)
			
			# subset to specific ticker from the downloaded data
			ticker_data = scope.yf['data'][scope.yf['data']['ticker'] == ticker]			
			ticker_data = ticker_data[ticker_file_usecols]				# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]		# drop rows where volume is zero 
			
			if len(ticker_data)>0:
				# We may have no data after dropping the zero volume rows
				update_missing_ticker_lists(scope, ticker)
				add_new_ticker(scope, ticker, ticker_data)
			else:
				# Ticker Downloaded ok but only contained dates with zero volume
				fail_download_event(scope, ticker, zero_volume=True)
		else:
			# Ticker Failed to download
			fail_download_event(scope, ticker)	