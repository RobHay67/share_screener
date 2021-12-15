import os

from config.model.set_results import store_results
from config.model.set_ticker_path import path_for_ticker_file
from tickers.model.read_csv import load_ticker
from pages.view.results import view_results
from config.model.set_page_df_refresh import set_refresh_df_for_ticker_in_all_pages

def load_tickers(scope, ticker_list):				# I will be provided with a single ticker or a list of tickers (both in a list object)
	
	page = scope.page_to_display

	store_results(	scope, 
					passed='Loaded Local files > ', 
					failed='Missing local files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		if ticker not in scope.ticker_data_files:					# We only need to load it if its not already loaded
			path_for_ticker_file(scope, ticker )

			if os.path.exists( scope.path_ticker_data_file ):										# A local file is available to load
				print ( '\033[92m' + ticker.ljust(10) + '> loading local ticker file \033[0m')
				load_ticker(scope, ticker )
				# scope.loaded_ticker_list.append(ticker)
				store_results( scope, ticker, result='passed' )
				set_refresh_df_for_ticker_in_all_pages(scope, ticker, True)
			else:																					# The expected Local file is not available
				print ( '\033[95m' + ticker.ljust(10) + '> missing local ticker file \033[0m')
				scope.downloaded_missing_list.append(ticker)
				store_results( scope, ticker, result='failed' )
				set_refresh_df_for_ticker_in_all_pages(scope, ticker, False)


		else:
			print ( '\033[92m' + ticker.ljust(10) + '> skipping as ticker already loaded into < scope.ticker_data_files > \033[0m')

		


	store_results(scope, 'Finished', final_print=True )
	
	view_results(scope)

	


