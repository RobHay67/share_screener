import os

from progress.cache import cache_progress
from files.path import path_for_ticker_file
from tickers.load import load_ticker
from tickers.cache import cache_ticker_data
from partials.messages.progress import render_progress_messages
from tickers.status.missing_local_file import set_missing_status

def load_tickers(scope):
	
	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['worklist']

	cache_progress(	scope, 
					passed='Loaded Local files > ', 
					failed='Missing local files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		# Attempt to load unless we already know the file is missing
		if ticker not in scope.missing_tickers['local']:
			
			path_for_ticker_file(scope, ticker )

			# Check that a local file is available to load
			if os.path.exists( scope.files['paths']['ticker_data'] ):										
				ticker_data = load_ticker(scope, ticker )
				cache_ticker_data(scope, ticker, ticker_data)
				cache_progress( scope, ticker, result='passed' )
			else:
				# The expected Local file is not available
				set_missing_status(scope, ticker)															
				cache_progress( scope, ticker, result='failed' )

	cache_progress(scope, 'Finished', final_print=True )
	
	render_progress_messages(scope)

	


