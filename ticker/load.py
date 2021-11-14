import os
import pandas as pd

from web.results import render_results
from ticker.path import generate_path_for_share_data_file


from ticker.schema import ticker_file_usecols, ticker_file_dtypes, ticker_file_dates

# ==============================================================================================================================================================
# Ticker Data : loaders and savers
# ==============================================================================================================================================================
def load_multiple_ticker_files( scope ):
	render_results( scope, 
					passed='LOADED Share Data Files > ', 
					failed='MISSING Share Data Files for > ', 
					passed_2='na' 
					)
	
	for ticker in scope.ticker_list['multi']:
		generate_path_for_share_data_file(scope, ticker )
		verify_and_load(scope, ticker)
	
	render_results(scope, 'Finished', final_print=True )

def load_single_ticker_file(scope, ticker):
	
	render_results( scope, 
					passed='LOADED Share Data Files > ', 
					failed='MISSING Share Data Files for > ', 
					passed_2='na',
					)

	generate_path_for_share_data_file(scope, ticker )

	verify_and_load(scope, ticker)

	render_results(scope, 'Finished', final_print=True )

def verify_and_load(scope, ticker):
	if os.path.exists( scope.path_share_data_file ):
		actual_loader(scope, ticker )
		scope.downloaded_loaded_list.append(ticker)
		render_results( scope, ticker, result='passed' )
	else:
		scope.downloaded_missing_list.append(ticker)
		render_results( scope, ticker, result='failed' )

def actual_loader( scope, ticker ): # DONE
	share_data_file = pd.read_csv (  
									scope.path_share_data_file, 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = ticker_file_usecols,
									# index_col   = 'date', 
									dtype       = ticker_file_dtypes,
									parse_dates = ticker_file_dates,
									)
	scope.share_data_files[ticker] = share_data_file









