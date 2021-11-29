import os

from config.model.set_results import store_results
from config.model.set_ticker_path import path_for_ticker_file
from ticker.model.read_csv import load_ticker
from pages.view.results import view_results

def load_tickers(scope, ticker_list):				# will be given a single ticker or a list of tickers
	page = scope.page_to_display

	store_results(	scope, 
					passed='Loaded files > ', 
					failed='Missing files > ', 
					passed_2='na',
					)

	for ticker in ticker_list:
		if ticker not in scope.ticker_data_files:					# Ensure it has not already been loaded
			print ( '\033[93m' + ticker + ' > loading ticker file\033[0m')
			path_for_ticker_file(scope, ticker )

			if os.path.exists( scope.path_ticker_data_file ):
				load_ticker(scope, ticker )
				scope.downloaded_loaded_list.append(ticker)
				store_results( scope, ticker, result='passed' )
			else:
				scope.downloaded_missing_list.append(ticker)
				store_results( scope, ticker, result='failed' )
			
			# reset STATUS to prevent unnecesary updates
			scope.pages[page]['refresh_analysis_df'] = True
			scope.pages[page]['refresh_chart_df'] 	 = True
		# else:
		# 	print ( '\033[92m' + ticker + ' > skipping load\033[0m')

	store_results(scope, 'Finished', final_print=True )
	
	view_results(scope)

	


