import os

from config.results.results import store_result
from data.tickers.model.ticker_path import path_for_ticker_file
from data.tickers.model.read_csv import load_ticker
from pages.view.results import view_results
from pages.model.data_status import redo_ohlc_data_all_pages_one_ticker

def load_tickers(scope):
	
	page = scope.pages['display_page']
	ticker_list = scope.pages[page]['ticker_list']

	store_result(	scope, 
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
				store_result( scope, ticker, result='passed' )
				redo_ohlc_data_all_pages_one_ticker(scope, ticker, True)
			else:																					# The expected Local file is not available
				print ( '\033[95m' + ticker.ljust(10) + '> missing local ticker file \033[0m')
				scope.data['download']['missing_list'].append(ticker)
				store_result( scope, ticker, result='failed' )
				redo_ohlc_data_all_pages_one_ticker(scope, ticker, False)
			
		# else:
		# 	print ( '\033[92m' + ticker.ljust(10) + '> skipping as ticker already loaded into < scope.data['ticker_files'] > \033[0m')

		


	store_result(scope, 'Finished', final_print=True )
	
	view_results(scope)

	


