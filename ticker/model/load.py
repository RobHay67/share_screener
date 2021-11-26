import os

from pages.view.results import results
from ticker.helpers.path import generate_path_for_share_data_file
from ticker.model.read_csv import load_ticker
from ticker.views.results import view_results

def load_tickers(scope, ticker_list):				# will be given a single ticker or a list of tickers
	page = scope.page_to_display

	results(scope, 
			passed='Loaded files > ', 
			failed='Missing files > ', 
			passed_2='na',
			)

	for ticker in ticker_list:
		if ticker not in scope.ticker_data_files:					# Ensure it has not already been loaded
			print ( '\033[93m' + ticker + ' > loading ticker file\033[0m')
			generate_path_for_share_data_file(scope, ticker )

			if os.path.exists( scope.path_ticker_data_file ):
				load_ticker(scope, ticker )
				scope.downloaded_loaded_list.append(ticker)
				results( scope, ticker, result='passed' )
			else:
				scope.downloaded_missing_list.append(ticker)
				results( scope, ticker, result='failed' )
			
			# reset STATUS to prevent unnecesary updates
			scope.pages[page]['refresh_analysis_df'] = True
			scope.pages[page]['refresh_chart_df'] 	 = True
		# else:
		# 	print ( '\033[92m' + ticker + ' > skipping load\033[0m')

	results(scope, 'Finished', final_print=True )
	
	view_results(scope)

	


