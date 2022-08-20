import pandas as pd

from tickers.schema import ticker_file_usecols
from tickers.events.combine import set_data_status
from tickers.load.cache import cache_in_tickers
from tickers.events.download import set_download_failure_status, set_download_new_data_status
from tickers.download.save import save_ticker


def combine_cached_and_yf_data(scope):
	# concatenates any downloaded data with any loaded data 
	# resulting in a complete (hopefully) temporal transaction history for a ticker

	# iterate through the target tickers for the App
	app = scope.apps['display_app']
	for ticker in scope.apps[app]['worklist']:
				
		if ticker in scope.download['yf_data']['ticker'].unique():
			# we appear to have downloaded data (we may have nothing)
			
			# subset to specific ticker from the downloaded data
			ticker_data = scope.download['yf_data'][scope.download['yf_data']['ticker'] == ticker]			
			ticker_data = ticker_data[ticker_file_usecols]				# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]		# drop rows where volume is zero 
			
			if len(ticker_data)>0:
				# We may have no data after dropping the zero volume rows

				if ticker in scope.tickers.keys():	
					# we have exisiting ticker date to concatenate the downloaded data
					scope.tickers[ticker]['df'] = pd.concat([scope.tickers[ticker]['df'], ticker_data]).drop_duplicates(subset=['date'], keep='last')
					
					# sort the share data into date order ascending
					scope.tickers[ticker]['df'].sort_values(by=['date'], inplace=True, ascending=False)		
				else:
					# its brand new - so treat like a locally loaded file
					cache_in_tickers(scope, ticker, ticker_data)
					set_download_new_data_status(scope, ticker)

				save_ticker(scope, ticker)
				set_data_status(scope, ticker)
			else:
				print('\033[95m', ticker, ' downloaded but we dont have any data', '\033[0m')
				scope.download['yf_errors'].update({ticker:'downloaded ok, but after dropping 0 volume days contained no records'})
				set_download_failure_status(scope, ticker)
		else:
			print('\033[91m', ticker, ' failed to download', '\033[0m')
			set_download_failure_status(scope, ticker)	
		


def cache_yf_batch_data(scope):

	# cache a list of tickers for later reporting
	yf_ticker_list = scope.download['yf_batch_ticker_string'].split(' ')
	scope.download['yf_ticker_list'].extend(yf_ticker_list)
	
	# cache the downloaded data for later processing and reporting
	scope.download['yf_data'] = pd.concat([scope.download['yf_data'], scope.download['yf_batch_data']], sort=False)

	# cache the download errors for later reporting
	scope.download['yf_errors'].update(scope.download['yf_batch_errors'])
	print('='*100)
	print('cache download errors')
	print('-'*100)
	print(scope.download['yf_errors'])
	print('-'*100)






