import os
import pathlib
import pandas as pd

from results.model.set_results import store_results


from tickers.model.set_ticker_path import path_for_ticker_file


def save_tickers(scope):
	page 		= scope.page_to_display
	ticker_list = scope.pages[page]['ticker_list']

	print(ticker_list)

	store_results( 	scope, 
				passed='Saved > ', 
				failed='Save Cancelled (no data) > ', 
				passed_2='na'
				)

	for ticker in ticker_list:
		if ticker in scope.ticker_data_files:						# if its not in here, it will not be available to save
			path_for_ticker_file(scope, ticker )
			save_ticker( scope, scope.ticker_data_files[ticker] )
			store_results( scope, ticker, result='passed' )
		else:
			store_results( scope, ticker, result='failed' )
	
	store_results(scope, 'Finished', final_print=True )



def save_ticker( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.path_ticker_data_file, index=False )



