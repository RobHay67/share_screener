import os

from files.path import path_for_ticker_file
from tickers.load.load import load_ticker
from tickers.load.cache import cache_in_tickers
from tickers.events.missing_local_file import set_missing_local_file_status


def load_tickers(scope):
	
	app = scope.apps['display_app']
	worklist = scope.apps[app]['worklist']
	missing_local_file_list = scope.missing_tickers['local']
	already_loaded_list = scope.apps[app]['mined_tickers']

	for ticker in worklist:
		if ticker not in missing_local_file_list:
			if ticker not in already_loaded_list:
				path_for_ticker_file(scope, ticker )

				# Check that a local file is available to load
				if os.path.exists( scope.files['paths']['ticker_data'] ):
					print('loading local >', ticker)								
					ticker_data = load_ticker(scope, ticker )
					cache_in_tickers(scope, ticker, ticker_data)
				else:
					print('missing local >', ticker)	
					# The expected Local file is not available
					set_missing_local_file_status(scope, ticker)															
	
	


