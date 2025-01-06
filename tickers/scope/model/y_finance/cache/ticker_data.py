from tickers.scope.model.schema import ticker_file_usecols
from tickers.scope.model.new import add_new_ticker
from tickers.scope.model.missing_tickers.lists import update_missing_ticker_lists
from tickers.scope.model.missing_tickers.failed_download import fail_download_event


def cache_entire_download(scope, ticker_download_list):
	# concatenates any downloaded data with any loaded data 
	# resulting in a complete (hopefully) temporal transaction history for a ticker

	# iterate through the target tickers for the Page
	for ticker in ticker_download_list:			
		if ticker in scope.yf['data']['ticker'].unique():
			# we appear to have downloaded data (we may have nothing)
			# subset to specific ticker from the downloaded data
			ticker_data = scope.yf['data'][scope.yf['data']['ticker'] == ticker]
			# standardise the columns
			ticker_data = ticker_data[ticker_file_usecols]
			# drop rows where volume is zero 		
			ticker_data = ticker_data[ticker_data['volume'] != 0]
			
			# We may not have any data after dropping the zero volume rows (above)
			if len(ticker_data)>0:
				update_missing_ticker_lists(scope, ticker)
				add_new_ticker(scope, ticker, ticker_data)
			else:
				# Ticker Downloaded ok but only contained dates with zero volume
				fail_download_event(scope, ticker, zero_volume=True)
		else:
			# Ticker Failed to download
			fail_download_event(scope, ticker)	