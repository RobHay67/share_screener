import os

from config.model.set_results import store_results
from config.model.set_ticker_path import path_for_ticker_file
from ticker.model.read_csv import load_ticker
from pages.view.results import view_results
from config.model.set_page_df_refresh import set_refresh_df_for_ticker_in_all_pages

def load_tickers(scope, ticker_list):				# I will be provided with a single ticker or a list of tickers (both in a list object)
	
	page = scope.page_to_display

	store_results(	scope, 
					passed='Loaded files > ', 
					failed='Missing files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		if ticker not in scope.ticker_data_files:					# We only need to load it if its not already loaded
			path_for_ticker_file(scope, ticker )

			if os.path.exists( scope.path_ticker_data_file ):
				print ( '\033[96m' + ticker + ' < load_tickers > loading ticker file\033[0m')
				load_ticker(scope, ticker )
				scope.downloaded_loaded_list.append(ticker)
				store_results( scope, ticker, result='passed' )
				set_refresh_df_for_ticker_in_all_pages(scope, ticker)
			else:
				print ( '\033[91m' + ticker + ' < load_tickers > local File not available\033[0m')
				scope.downloaded_missing_list.append(ticker)
				store_results( scope, ticker, result='failed' )
		else:
			print ( '\033[92m' + ticker + ' skipping < load_tickers > as ticker already loaded into scope.ticker_data_files \033[0m')

		


	store_results(scope, 'Finished', final_print=True )
	
	view_results(scope)

	


