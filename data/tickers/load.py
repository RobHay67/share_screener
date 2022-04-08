import os

from results.model.set_results import store_results
from data.tickers.model.set_ticker_path import path_for_ticker_file
from data.tickers.model.read_csv import load_ticker
from pages.view.results import view_results
from pages.model.set_page_df_status import set_refresh_page_df_ticker

def load_tickers(scope):
	
	page = scope.pages['display_page']
	ticker_list = scope.pages[page]['ticker_list']

	store_results(	scope, 
					passed='Loaded Local files > ', 
					failed='Missing local files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		if ticker not in scope.data['ticker_files']:					# We only need to load it if its not already loaded
			path_for_ticker_file(scope, ticker )

			if os.path.exists( scope.files['paths']['ticker_data'] ):										# A local file is available to load
				print ( '\033[92m' + ticker.ljust(10) + '> loading local ticker file \033[0m')
				load_ticker(scope, ticker )
				store_results( scope, ticker, result='passed' )
				set_refresh_page_df_ticker(scope, ticker, True)
			else:																					# The expected Local file is not available
				print ( '\033[95m' + ticker.ljust(10) + '> missing local ticker file \033[0m')
				scope.data['download']['missing_list'].append(ticker)
				store_results( scope, ticker, result='failed' )
				set_refresh_page_df_ticker(scope, ticker, False)
			
		# else:
		# 	print ( '\033[92m' + ticker.ljust(10) + '> skipping as ticker already loaded into < scope.data['ticker_files'] > \033[0m')

		


	store_results(scope, 'Finished', final_print=True )
	
	view_results(scope)

	


