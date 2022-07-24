import os

from config.results.store import store_result
from data.tickers.model.ticker_path import path_for_ticker_file
from data.tickers.model.read_csv import load_ticker
from apps.ticker_loader.messages import view_result
from apps.data.status import set_replace_df_status_for_ticker, set_replace_col_status_for_ticker


def load_tickers(scope):
	
	page = scope.pages['display_page']
	ticker_list = scope.pages[page]['ticker_list']

	store_result(	scope, 
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
				load_ticker(scope, ticker )
				store_result( scope, ticker, result='passed' )
				set_replace_df_status_for_ticker(scope, ticker, new_status=True)
				set_replace_col_status_for_ticker(scope, ticker, new_status=False)
			else:
				# The expected Local file is not available - so report this																
				print ( '\033[95m' + ticker.ljust(10) + '> missing local ticker file \033[0m')
				scope.data['download']['missing_list'].append(ticker)
				store_result( scope, ticker, result='failed' )
				set_replace_df_status_for_ticker(scope, ticker, new_status=False)
				set_replace_col_status_for_ticker(scope, ticker, new_status=False)		


	store_result(scope, 'Finished', final_print=True )
	
	view_result(scope)

	


