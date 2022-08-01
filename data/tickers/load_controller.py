import os

from progress.store import cache_progress
from files.path import path_for_ticker_file
from data.tickers.load import load_ticker
from data.tickers.cache import cache_ticker_file
from apps_parts.ticker_loader.messages import render_messages
from apps.data.status import set_replace_df_status_for_ticker, set_replace_col_status_for_ticker


def load_tickers(scope):
	
	app = scope.apps['display_app']
	ticker_list = scope.apps[app]['ticker_list']

	cache_progress(	scope, 
					passed='Loaded Local files > ', 
					failed='Missing local files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		# We only need to load it has NOT previously been loading into data
		if ticker not in scope.data['ticker_files']:					
			path_for_ticker_file(scope, ticker )

			# Check that a local file is available to load
			if os.path.exists( scope.files['paths']['ticker_data'] ):										
				print ( '\033[92m' + ticker.ljust(10) + '> loading local ticker file \033[0m')
				ticker_data_file = load_ticker(scope, ticker )

				cache_ticker_file(scope,ticker, ticker_data_file)
				cache_progress( scope, ticker, result='passed' )
				set_replace_df_status_for_ticker(scope, ticker, new_status=True)
				set_replace_col_status_for_ticker(scope, ticker, new_status=False)
			else:
				# The expected Local file is not available - so report this																
				print ( '\033[95m' + ticker.ljust(10) + '> missing local ticker file \033[0m')
				scope.data['download']['missing_list'].append(ticker)
				cache_progress( scope, ticker, result='failed' )
				set_replace_df_status_for_ticker(scope, ticker, new_status=False)
				set_replace_col_status_for_ticker(scope, ticker, new_status=False)		


	cache_progress(scope, 'Finished', final_print=True )
	
	render_messages(scope)

	


