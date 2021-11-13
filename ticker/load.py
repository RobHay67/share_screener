import os
import pandas as pd

from web.results import render_results
from ticker.path import generate_path_for_share_data_file

# ==============================================================================================================================================================
# Ticker Data : loaders and savers
# ==============================================================================================================================================================
def load_ticker_data_files( scope ):
	render_results( scope, passed='LOADED Share Data Files > ', failed='MISSING Share Data Files for > ', passed_2='na' )

	# scope.downloaded_loaded_list = []					# TODO - I dont beleive we need to reset these lists - they should just grow with the session
	# scope.downloaded_missing_list = []				# TODO - I dont beleive we need to reset these lists - they should just grow with the session
	
	for ticker in scope.ticker_list['multi']:
		generate_path_for_share_data_file(scope, ticker )
		if os.path.exists( scope.path_share_data_file ):
			load_a_single_ticker(scope, ticker )
			scope.downloaded_loaded_list.append(ticker)
			render_results( scope, ticker, result='passed' )
		else:
			scope.downloaded_missing_list.append(ticker)
			render_results( scope, ticker, result='failed' )
	render_results(scope, 'Finished', final_print=True )

def load_a_single_ticker( scope, ticker ): # DONE
	share_data_file = pd.read_csv (  
									scope.path_share_data_file, 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = scope.share_data_usecols,
									# index_col   = 'date', 
									dtype       = scope.share_data_dtypes,
									parse_dates = scope.share_data_dates,
									)
	scope.share_data_files[ticker] = share_data_file









