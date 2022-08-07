import os

from progress.store import cache_progress
from files.path import path_for_ticker_file
from tickers.load import load_ticker
from tickers.cache import cache_ticker_file
from partials.ticker_loader.messages import render_messages
# from tickers.status.load_ticker import set_replace_df_status_for_ticker
# from tickers.status.load_ticker import set_replace_col_status_for_ticker
from tickers.config import ticker_status



def load_tickers(scope):
	
	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['ticker_list']

	cache_progress(	scope, 
					passed='Loaded Local files > ', 
					failed='Missing local files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		# We only need to load if it has NOT previously been loaded into memory
		if ticker not in scope.ticker_files:					
			path_for_ticker_file(scope, ticker )

			# Check that a local file is available to load
			if os.path.exists( scope.files['paths']['ticker_data'] ):										
				print ( '\033[92m' + ticker.ljust(10) + '> loading local ticker file \033[0m')
				ticker_data_file = load_ticker(scope, ticker )

				cache_ticker_file(scope, ticker, ticker_data_file)
				ticker_status(scope, ticker)
				cache_progress( scope, ticker, result='passed' )
				# set_replace_df_status_for_ticker(scope, ticker, new_status=True)
				# set_replace_col_status_for_ticker(scope, ticker, new_status=False)
			else:
				# The expected Local file is not available - so report this																
				print ( '\033[95m' + ticker.ljust(10) + '> missing local ticker file \033[0m')
				scope.download['missing_list'].append(ticker)
				cache_progress( scope, ticker, result='failed' )
				# set_replace_df_status_for_ticker(scope, ticker, new_status=False)
				# set_replace_col_status_for_ticker(scope, ticker, new_status=False)		


	cache_progress(scope, 'Finished', final_print=True )
	
	render_messages(scope)

	


