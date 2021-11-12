import os
import pathlib
import pandas as pd

from web.results import render_results


# ==============================================================================================================================================================
# Ticker Data : loaders and savers
# ==============================================================================================================================================================
def load_ticker_data_files( scope ):
	render_results( scope, passed='LOADED Share Data Files > ', failed='MISSING Share Data Files for > ', passed_2='na' )

	# scope.downloaded_loaded_list = []					# TODO - I dont beleive we need to reset these lists - they should just grow with the session
	# scope.downloaded_missing_list = []				# TODO - I dont beleive we need to reset these lists - they should just grow with the session
	
	for ticker in scope.ticker_list:
		generate_path_for_share_data_file(scope, ticker )
		if os.path.exists( scope.path_share_data_file ):
			load_a_file(scope, ticker )
			scope.downloaded_loaded_list.append(ticker)
			render_results( scope, ticker, result='passed' )
		else:
			scope.downloaded_missing_list.append(ticker)
			render_results( scope, ticker, result='failed' )
	render_results(scope, 'Finished', final_print=True )

def load_a_file( scope, ticker ): # DONE
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

def save_tickers( scope ): # DONE
	render_results( scope, passed='Files SAVED > ', failed='na', passed_2='na' )
	for ticker in scope.share_data_files:
		generate_path_for_share_data_file(scope, ticker )
		save_ticker( scope, scope.share_data_files[ticker] )
		render_results( scope, ticker, result='passed' )
	render_results(scope, 'Finished', final_print=True )

def save_ticker( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.path_share_data_file, index=False )

# -----------------------------------------------------------------------------------------------------------------------------------
# share file path generator
# -----------------------------------------------------------------------------------------------------------------------------------

def generate_path_for_share_data_file( scope, ticker ):
	file_name = ( ticker.replace( '.', '_' ) ) + '.csv'
	file_path = pathlib.Path.home().joinpath( scope.folder_share_data, file_name )
	scope.path_share_data_file = file_path





