from tickers.scope.model.new import add_new_ticker
from tickers.scope.model.missing.lists import update_missing_ticker_lists
from tickers.scope.model.missing.failed_download import fail_download_event


def append_downloaded_data_to_scope_tickers(scope, ticker_download_list):
	# concatenates any downloaded data with any loaded data 
	# resulting in a complete (hopefully) temporal transaction history for a ticker

	# iterate through the target tickers for the Page
	for ticker in ticker_download_list:			
		if ticker in scope.yf['all_data']['ticker'].unique():
			# we appear to have downloaded data (we may have nothing)
			# subset to specific ticker from the downloaded data
			ticker_data = scope.yf['all_data'][scope.yf['all_data']['ticker'] == ticker]
			# standardise the columns
			ticker_data = ticker_data[scope.ticker_config['usecols']]
			# drop rows where volume is zero 		
			ticker_data = ticker_data[ticker_data['volume'] != 0]
			
			# Check we have data after dropping the zero volume rows (above)
			if len(ticker_data)>0:
				update_missing_ticker_lists(scope, ticker)
				add_new_ticker(scope, ticker, ticker_data)
			else:
				# Ticker Downloaded ok but only contained dates with zero volume
				fail_download_event(scope, ticker, zero_volume=True)
		else:
			# Ticker Failed to download at all
			fail_download_event(scope, ticker)	